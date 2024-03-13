import streamlit as st
import geopandas as gpd
import pandas as pd
import os
import json
from plotly import express as px
from plotly import graph_objs as go


class ImmoClass:
    def __init__(self):
        self.houses_data = None

        # load the data
        self.load_houses_data_pandas()

        # clean the data
        self.clean_data()

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
