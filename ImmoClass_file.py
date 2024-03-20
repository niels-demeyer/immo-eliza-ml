import streamlit as st
import os
import numpy as np
from plotly import express as px
from plotly import graph_objs as go
import pandas as pd
from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder,
    OrdinalEncoder,
    FunctionTransformer,
)
from sklearn.compose import (
    ColumnTransformer,
    make_column_transformer,
    make_column_selector,
)
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib
from xgboost import XGBRegressor
import json


class ImmoClass:
    def __init__(self, property_type):
        self.property_type = property_type
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model_linear = None
        self.model_random_forest = None
        self.model_knn = None
        self.models = {}
        self.model_results = {}

        # load the data
        self.load_data_pandas()

        # clean the data
        self.clean_data()

        # # describe the data
        # self.describe_data()

        # split the data
        self.split_data()

        # apply the preprocessor
        self.apply_preprocessor()

    # Load the data
    def load_data_pandas(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"data\raw\properties.csv"
        file_path = os.path.join(script_dir, rel_path)
        df = pd.read_csv(file_path)
        self.data = df

    def save_df(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"data\raw\houses.csv"
        file_path = os.path.join(script_dir, rel_path)
        self.data.to_csv(file_path, index=False)

    def clean_data(self):
        # Handle missing values
        # drop rows with missing price
        self.data = self.data.dropna(subset=["price"])

        # Remove duplicates
        self.data = self.data.drop_duplicates()

        # Remove the ID column
        self.data = self.data.drop(columns=["id"])

        if self.property_type == "APARTMENT":
            # Remove rows with missing values in the following columns
            self.data = self.data.drop(columns=["surface_land_sqm"])

        # Remove the longitudes and latitudes
        self.data = self.data.drop(columns=["longitude", "latitude"])

        # Remove the construction year
        self.data = self.data.drop(columns=["construction_year"])

        # Remove the propery_type
        self.data = self.data.drop(columns=["property_type"])

    def describe_data(self):
        # Display the first few rows of the dataset
        print(self.data.head())

        # Display the shape of the dataset
        print(
            f"The dataset has {self.data.shape[0]} rows and {self.data.shape[1]} columns"
        )

        # Display the data types of the dataset
        print(self.data.dtypes)

        # Display the number of missing values for each column
        print(self.data.isna().sum())

        # Display the statistics of the dataset
        print(self.data.describe())

    def split_data(self):
        # Split the data into training and testing sets
        X = self.data.drop("price", axis=1)
        y = self.data["price"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        print(f"Training set: {self.X_train.shape}")
        print(f"Testing set: {self.X_test.shape}")

    def create_preprocessor(self):
        # Define preprocessing for numeric columns (scale them)
        numeric_features = self.data.select_dtypes(include=["int64", "float64"]).columns
        numeric_features = numeric_features.drop(
            "price"
        )  # Exclude 'price' from numeric features

        numeric_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]
        )

        # Define preprocessing for categorical features (one-hot encode them)
        categorical_features = self.data.select_dtypes(include=["object"]).columns
        ordinal_columns = [
            "fl_double_glazing",
            "fl_swimming_pool",
            "fl_garden",
            "fl_floodzone",
            "fl_terrace",
            "fl_open_fire",
            "fl_furnished",
        ]

        # Exclude ordinal columns from categorical features
        categorical_features = [
            col for col in categorical_features if col not in ordinal_columns
        ]

        categorical_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="constant", fill_value="MISSING")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]
        )

        # Define preprocessing for ordinal features
        ordinal_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("ordinal", OrdinalEncoder()),
            ]
        )

        # Combine preprocessing steps
        self.preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
                ("ord", ordinal_transformer, ordinal_columns),
            ]
        )

    def apply_preprocessor(self):
        # Create the preprocessor
        self.create_preprocessor()

        # Preprocess the training and testing data
        self.X_train = self.preprocessor.fit_transform(self.X_train)
        self.X_test = self.preprocessor.transform(self.X_test)

    def train_model_knn(self):
        # Define the model
        model = KNeighborsRegressor()

        # Define the parameter values to test
        param_grid = {"n_neighbors": range(1, 3)}

        # Create the grid search object
        grid_search = GridSearchCV(model, param_grid, cv=5)

        # Fit the grid search
        grid_search.fit(self.X_train, self.y_train)

        # Print the best parameters
        print(grid_search.best_params_)

        # Save the trained model with best parameters
        self.model_knn = grid_search.best_estimator_

    def train_model_linear(self):
        # Define the model
        model = LinearRegression()

        # Train the model
        model.fit(self.X_train, self.y_train)

        # Save the trained model
        self.models["linear"] = model

        # Predict on the test set
        y_pred = model.predict(self.X_test)

        # Calculate the R^2 score
        r2 = r2_score(self.y_test, y_pred)

        # Calculate the mean squared error
        mse = mean_squared_error(self.y_test, y_pred)

        # Save the model results
        self.model_results["linear"] = {
            "coefficients": model.coef_,
            "intercept": model.intercept_,
            "r2_score": r2,
            "mse": mse,
        }

    def train_model_random_forest(self):
        # Define the model
        model = RandomForestRegressor(
            n_estimators=50, random_state=42, n_jobs=-1, max_depth=10
        )

        # Train the model
        model.fit(self.X_train, self.y_train)

        # Save the trained model
        self.models["random_forest"] = model

        # Predict on the test set
        y_pred = model.predict(self.X_test)

        # Calculate the R^2 score
        r2 = r2_score(self.y_test, y_pred)

        # Calculate the mean squared error
        mse = mean_squared_error(self.y_test, y_pred)

        # Save the model results
        self.model_results["random_forest"] = {
            "r2_score": r2,
            "mse": mse,
        }
        # print(
        #     f"Random forest model results for {self.property_type}: {self.model_results['random_forest']}"
        # )

    def train_model_xgboost(self):
        # Define the model
        model = XGBRegressor(n_estimators=100, learning_rate=0.05, n_jobs=-1)

        # Train the model
        model.fit(self.X_train, self.y_train)

        # Save the trained model
        self.models["xgboost"] = model

        # Predict on the test set
        y_pred = model.predict(self.X_test)

        # Calculate the R^2 score
        r2 = r2_score(self.y_test, y_pred)

        # Calculate the mean squared error
        mse = mean_squared_error(self.y_test, y_pred)

        # Save the model results
        self.model_results["xgboost"] = {
            "r2_score": r2,
            "mse": mse,
        }

    def save_model(self, model_type):
        # Check if the model type is valid
        if model_type not in self.models:
            print(f"Invalid model type: {model_type}")
            return

        # Save the model
        model = self.models[model_type]
        script_dir = os.path.dirname(__file__)
        name_output = model_type + ".pkl"
        rel_path = r"data\clean\\"
        file_path = os.path.join(script_dir, rel_path, name_output)
        joblib.dump(model, file_path)

    def print_model_results(self):
        for model_type, results in self.model_results.items():
            print(f"Model: {model_type}")
            for key, value in results.items():
                print(f"{key}: {value}")

    def save_model_results(self):
        # Convert numpy arrays in model results to lists
        for model_type, results in self.model_results.items():
            for key, value in results.items():
                if isinstance(value, np.ndarray):
                    results[key] = value.tolist()

        # Save the model results as a json file
        script_dir = os.path.dirname(__file__)
        rel_path = r"data\clean\model_results.json"
        file_path = os.path.join(script_dir, rel_path)

        # Load existing data
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                existing_data = json.load(f)
        else:
            existing_data = {}

        # Update existing data with new data
        for model_type, results in self.model_results.items():
            if self.property_type not in existing_data:
                existing_data[self.property_type] = {}
            if model_type in existing_data[self.property_type]:
                existing_data[self.property_type][model_type].append(results)
            else:
                existing_data[self.property_type][model_type] = [results]

        # Write updated data back to file
        with open(file_path, "w") as f:
            json.dump(existing_data, f)

    def streamlit_app(self):
        st.set_page_config(page_title="Belgium Real Estate Analysis", layout="wide")

        st.title("Belgium Real Estate Analysis")
        st.markdown(
            "This is a simple web app that shows the average price of houses per municipality in Belgium"
        )
