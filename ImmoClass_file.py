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


class ImmoClass:
    def __init__(self):
        self.houses_data = None

        # load the data
        self.load_houses_data_pandas()

        # clean the data
        self.clean_data()

        # preprocess the data
        self.preprocess_data()

        # train the model
        self.train_model()

    # Load the houses data
    def load_houses_data_pandas(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"data\raw\properties.csv"
        file_path = os.path.join(script_dir, rel_path)
        self.houses_data = pd.read_csv(file_path)

    def clean_data(self):
        # Convert data types
        cols_to_convert = [
            "latitude",
            "longitude",
            "construction_year",
            "total_area_sqm",
            "surface_land_sqm",
            "terrace_sqm",
            "garden_sqm",
            "primary_energy_consumption_sqm",
            "cadastral_income",
        ]
        cols_to_convert = [
            col for col in cols_to_convert if col in self.houses_data.columns
        ]
        self.houses_data[cols_to_convert] = self.houses_data[cols_to_convert].apply(
            pd.to_numeric, errors="coerce"
        )
        self.houses_data[cols_to_convert] = self.houses_data[cols_to_convert].apply(
            pd.to_numeric, errors="coerce"
        )

        # Handle missing values

        # self.houses_data.fillna(self.houses_data.mean(), inplace=True)

        # Remove duplicates
        self.houses_data.drop_duplicates(inplace=True)

    def preprocess_data(self):
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
        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ]
        )

        # Apply transformations to the data
        self.houses_data = preprocessor.fit_transform(self.houses_data)

    def train_model(self):
        # Split the data into training and testing sets
        X = self.houses_data.drop("price", axis=1)
        y = self.houses_data["price"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Define the model
        model = LinearRegression()

        # Train the model
        model.fit(X_train, y_train)

        # Save the trained model
        self.model = model

        # Predict on the test set
        y_pred = model.predict(X_test)

        # Calculate and print the R^2 score
        r2 = r2_score(y_test, y_pred)
        print(f"R^2 score: {r2}")

        # Calculate and print the mean squared error
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean squared error: {mse}")

    def streamlit_app(self):
        st.set_page_config(page_title="Belgium Real Estate Analysis", layout="wide")

        st.title("Belgium Real Estate Analysis")
        st.markdown(
            "This is a simple web app that shows the average price of houses per municipality in Belgium"
        )

        # calculate average price
        if self.avg_price is None:
            self.avg_price = self.calculate_average_price("city", "price")

        # # plot the average price of houses per municipality
        st.subheader("Average price of houses per municipality")
        self.plot_most_expensive_houses_average()
        self.plot_most_expensive_houses_average_static()

        # plot the count of houses per municipality
        st.subheader("Count of houses per municipality")
        self.plot_count_houses()

        # plot the count of houses per province
        st.subheader("Count of houses per province")
        self.plot_count_houses_per_province()
