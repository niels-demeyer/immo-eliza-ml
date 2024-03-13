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

    # Load the houses data
    def load_houses_data_pandas(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"data\raw\properties.csv"
        file_path = os.path.join(script_dir, rel_path)
        self.houses_data = pd.read_csv(file_path)

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
