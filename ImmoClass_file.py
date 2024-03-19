import streamlit as st
import os
from plotly import express as px
from plotly import graph_objs as go
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor


class ImmoClass:
    def __init__(self):
        self.houses_data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model_linear = None
        self.model_knn = None

        # load the data
        self.load_houses_data_pandas()

        # clean the data
        self.clean_data()

        # split the data
        self.split_data()

    # Load the houses data
    def load_houses_data_pandas(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"data\raw\properties.csv"
        file_path = os.path.join(script_dir, rel_path)
        self.houses_data = pd.read_csv(file_path)

    def clean_data(self):
        # Strip leading and trailing spaces from column names and make them lower case
        self.houses_data.columns = self.houses_data.columns.str.strip().str.lower()

        # Handle missing values
        # drop rows with missing price
        self.houses_data.dropna(subset=["price"], inplace=True)

        # Remove duplicates
        self.houses_data.drop_duplicates(inplace=True)

    def split_data(self):
        # Split the data into training and testing sets
        X = self.houses_data.drop("price", axis=1)
        y = self.houses_data["price"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    def create_preprocessor(self):
        # Define preprocessing for numeric columns (scale them)
        numeric_features = self.houses_data.select_dtypes(
            include=["int64", "float64"]
        ).columns
        numeric_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="mean")),
                ("scaler", StandardScaler()),
            ]
        )

        # Define preprocessing for categorical features (one-hot encode them)
        categorical_features = self.houses_data.select_dtypes(
            include=["object"]
        ).columns
        categorical_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="constant", fill_value="MISSING")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]
        )

        # Combine preprocessing steps
        self.preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ]
        )

    def apply_preprocessor(self):
        # Create the preprocessor
        self.create_preprocessor()

        # Preprocess the training and testing data
        X_train_preprocessed = self.preprocessor.fit_transform(self.X_train)
        X_test_preprocessed = self.preprocessor.transform(self.X_test)

    def knn_neighbors(self, n_neighbors):
        # Create the preprocessor
        self.create_preprocessor()

        # Preprocess the training and testing data
        X_train_preprocessed = self.preprocessor.transform(self.X_train)
        X_test_preprocessed = self.preprocessor.transform(self.X_test)

        # Define the model
        model = KNeighborsRegressor(n_neighbors=n_neighbors)

        # Train the model
        model.fit(X_train_preprocessed, self.y_train)

        # Save the trained model
        self.model_knn = model

        # Predict on the test set
        y_pred = model.predict(X_test_preprocessed)

        # Calculate and print the R^2 score
        r2 = r2_score(self.y_test, y_pred)
        print(f"R^2 score: {r2}")

        # Calculate and print the mean squared error
        mse = mean_squared_error(self.y_test, y_pred)
        print(f"Mean squared error: {mse}")

    def train_model_linear(self):
        # Create the preprocessor
        self.create_preprocessor()

        # Preprocess the training and testing data
        X_train_preprocessed = self.preprocessor.transform(self.X_train)
        X_test_preprocessed = self.preprocessor.transform(self.X_test)

        # Define the model
        model = LinearRegression()

        # Train the model
        model.fit(X_train_preprocessed, self.y_train)

        # Save the trained model
        self.model_linear = model

        # Print the model's coefficients and intercept
        print(f"Model coefficients for Linear Regression: {model.coef_}")
        print(f"Model intercept for Linear Regression: {model.intercept_}")

        # Predict on the test set
        y_pred = model.predict(X_test_preprocessed)

        # Calculate and print the R^2 score
        r2 = r2_score(self.y_test, y_pred)
        print(f"R^2 score for Linear Regression: {r2}")

        # Calculate and print the mean squared error
        mse = mean_squared_error(self.y_test, y_pred)
        print(f"Mean squared error for Linear Regression: {mse}")

    def streamlit_app(self):
        st.set_page_config(page_title="Belgium Real Estate Analysis", layout="wide")

        st.title("Belgium Real Estate Analysis")
        st.markdown(
            "This is a simple web app that shows the average price of houses per municipality in Belgium"
        )
