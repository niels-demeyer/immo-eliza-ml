import importlib.util
import os
import streamlit as st

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Define the path of the file to import
file_to_import = os.path.join(current_dir, "..", "training", "ImmoClass_file.py")

# Use importlib to import the module
spec = importlib.util.spec_from_file_location("ImmoClass", file_to_import)
ImmoClass = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ImmoClass)


def main():
    st.title("Real Estate Price Prediction")

    property_type = st.selectbox("Select Property Type", ["HOUSE", "APARTMENT"])

    # Create an instance of ImmoClass
    immo = ImmoClass.ImmoClass(property_type)

    # Collect the necessary input data
    region = st.text_input("Region")
    province = st.text_input("Province")
    locality = st.text_input("Locality")
    zip_code = st.number_input("Zip Code")
    total_area_sqm = st.number_input("Total Area (sqm)")
    surface_land_sqm = st.number_input("Surface Land (sqm)")
    nbr_frontages = st.number_input("Number of Frontages")
    nbr_bedrooms = st.number_input("Number of Bedrooms")
    equipped_kitchen = st.selectbox(
        "Equipped Kitchen",
        [
            "NOT_INSTALLED",
            "SEMI_EQUIPPED",
            "USA_HYPER_EQUIPPED",
            "INSTALLED",
            "USA_INSTALLED",
            "HYPER_EQUIPPED",
        ],
    )
    fl_furnished = st.selectbox("Furnished", [0, 1])
    fl_open_fire = st.selectbox("Open Fire", [0, 1])
    fl_terrace = st.selectbox("Terrace", [0, 1])
    terrace_sqm = st.number_input("Terrace Area (sqm)")
    fl_garden = st.selectbox("Garden", [0, 1])
    garden_sqm = st.number_input("Garden Area (sqm)")
    fl_swimming_pool = st.selectbox("Swimming Pool", [0, 1])
    fl_floodzone = st.selectbox("Floodzone", [0, 1])
    state_building = st.selectbox(
        "State of Building",
        ["NEW", "TO_BE_DONE_UP", "GOOD", "JUST_RENOVATED", "TO_RENOVATE"],
    )
    primary_energy_consumption_sqm = st.number_input("Primary Energy Consumption (sqm)")
    epc = st.number_input("EPC")
    heating_type = st.selectbox(
        "Heating Type", ["GAS", "OIL", "ELECTRIC", "COAL", "WOOD", "SOLAR", "HEAT_PUMP"]
    )
    fl_double_glazing = st.selectbox("Double Glazing", [0, 1])
    cadastral_income = st.number_input("Cadastral Income")

    # Create the input dictionary
    input_data = {
        "subproperty_type": property_type,
        "region": region,
        "province": province,
        "locality": locality,
        "zip_code": zip_code,
        "total_area_sqm": total_area_sqm,
        "surface_land_sqm": surface_land_sqm,
        "nbr_frontages": nbr_frontages,
        "nbr_bedrooms": nbr_bedrooms,
        "equipped_kitchen": equipped_kitchen,
        "fl_furnished": fl_furnished,
        "fl_open_fire": fl_open_fire,
        "fl_terrace": fl_terrace,
        "terrace_sqm": terrace_sqm,
        "fl_garden": fl_garden,
        "garden_sqm": garden_sqm,
        "fl_swimming_pool": fl_swimming_pool,
        "fl_floodzone": fl_floodzone,
        "state_building": state_building,
        "primary_energy_consumption_sqm": primary_energy_consumption_sqm,
        "epc": epc,
        "heating_type": heating_type,
        "fl_double_glazing": fl_double_glazing,
        "cadastral_income": cadastral_income,
    }

    # Add a button for the prediction
    if st.button("Estimate"):
        # Call the appropriate prediction method
        if property_type == "HOUSE":
            prediction = immo.predict_house(input_data)
        else:
            prediction = immo.predict_apartment(input_data)

        st.write(f"Predicted price: {prediction}")


if __name__ == "__main__":
    main()
