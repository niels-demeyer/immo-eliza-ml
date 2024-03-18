from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import autosklearn.classification
import os
import pandas as pd


class ImmoClass:
    def __init__(self):
        self.houses_data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = autosklearn.classification.AutoSklearnClassifier()
        self.preprocessor = None

        # load the data
        self.load_houses_data_pandas()

        # clean the data
        self.clean_data()

        self.split_data()

        # preprocess the data
        self.preprocessor = self.create_preprocessor(self.X_train)
        self.X_train = self.preprocess_data(self.X_train)
        self.X_test = self.preprocess_data(self.X_test)

        # train the model
        self.train_model()

    # Load the houses data
    def load_houses_data_pandas(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"data\raw\properties.csv"
        file_path = os.path.join(script_dir, rel_path)
        self.houses_data = pd.read_csv(file_path)

    def clean_data(self):
        # Strip leading and trailing spaces from column names and make them lower case
        self.houses_data.columns = self.houses_data.columns.str.strip().str.lower()
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
        self.houses_data[cols_to_convert] = self.houses_data[cols_to_convert].apply(
            pd.to_numeric, errors="coerce"
        )

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.houses_data.drop("price", axis=1),
            self.houses_data["price"],
            test_size=0.2,
            random_state=42,
        )

    def create_preprocessor(self, X):
        numeric_features = X.select_dtypes(include=["int64", "cfloat"]).columns
        numeric_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]
        )

        categorical_features = X.select_dtypes(include=["object"]).columns
        categorical_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]
        )

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ]
        )

        return preprocessor

    def preprocess_data(self, X):
        return self.preprocessor.fit_transform(X)

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self, X):
        return self.model.predict(X)

    def check_performance(self):
        # Use the model to make predictions on the test data
        predictions = self.predict(self.X_test)

        # Calculate and print the mean squared error and the r2 score
        mse = mean_squared_error(self.y_test, predictions)
        r2 = r2_score(self.y_test, predictions)

        print(f"Mean Squared Error: {mse}")
        print(f"R2 Score: {r2}")
