import importlib.util
import os
import streamlit as st

# Current file directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# File to import (ImmoClass)
file_to_import_immo = os.path.join(current_dir, "..", "training", "ImmoClass_file.py")
spec_immo = importlib.util.spec_from_file_location("ImmoClass", file_to_import_immo)
ImmoClass = importlib.util.module_from_spec(spec_immo)
spec_immo.loader.exec_module(ImmoClass)

# File to import (StreamlitClass)
from StreamlitClass_file import StreamlitClass


def estimate_price(input_data):
    if input_data["property_type"] == "APARTMENT":
        model = ImmoClass.ImmoClass("APARTMENT")  # Access the class through the module
        return model.predict_apartment(input_data)
    elif input_data["property_type"] == "HOUSE":
        model = ImmoClass.ImmoClass("HOUSE")  # Access the class through the module
        return model.predict_house(input_data)
    else:
        raise ValueError("Invalid property type")


def main():
    st.title("Real Estate App")

    # Create an instance of StreamlitClass
    streamlit = StreamlitClass()

    # Gather user input using the methods in StreamlitClass
    streamlit.select_property_type()
    streamlit.select_subproperty_type()
    streamlit.select_region()
    streamlit.select_province()
    streamlit.select_locality()
    streamlit.select_zip_code()
    streamlit.select_total_area_sqm()
    streamlit.select_surface_land_sqm()
    streamlit.select_nbr_frontages()
    streamlit.select_nbr_bedrooms()
    streamlit.select_equipped_kitchen()
    streamlit.select_fl_furnished()
    streamlit.select_fl_open_fire()
    streamlit.select_fl_terrace()
    streamlit.select_terrace_sqm()
    streamlit.select_fl_garden()
    streamlit.select_garden_sqm()
    streamlit.select_fl_swimming_pool()
    streamlit.select_fl_floodzone()
    streamlit.select_state_building()
    streamlit.select_primary_energy_consumption_sqm()
    streamlit.select_epc()
    streamlit.select_heating_type()
    streamlit.select_fl_double_glazing()
    streamlit.select_cadastral_income()

    # Get the input data
    input_data = streamlit.get_input_data()

    # # Display the input data
    # st.write(input_data)

    # Add a button for estimating the price
    if st.button("Estimate"):
        # Call the estimate_price function when the button is clicked
        estimated_price = estimate_price(input_data)
        # Display the estimated price
        st.write(f"Estimated price: {estimated_price}")


if __name__ == "__main__":
    main()
