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
file_to_import_streamlit = os.path.join(
    current_dir, "streamlit", "StreamlitClass_file.py"
)
spec_streamlit = importlib.util.spec_from_file_location(
    "StreamlitClass", file_to_import_streamlit
)
StreamlitClass = importlib.util.module_from_spec(spec_streamlit)
spec_streamlit.loader.exec_module(StreamlitClass)


def main():
    streamlit = StreamlitClass.StreamlitClass()
    st.title("Real Estate Price Prediction")

    property_type = streamlit.selectbox("Select Property Type", ["APARTMENT", "HOUSE"])
    immo = ImmoClass.ImmoClass(property_type)

    subproperty_type = st.selectbox(
        "Select Subproperty Type",
        [
            "APARTMENT",
            "HOUSE",
            "DUPLEX",
            "VILLA",
            "EXCEPTIONAL_PROPERTY",
            "FLAT_STUDIO",
            "GROUND_FLOOR",
            "PENTHOUSE",
            "FARMHOUSE",
            "APARTMENT_BLOCK",
            "COUNTRY_COTTAGE",
            "TOWN_HOUSE",
            "SERVICE_FLAT",
            "MANSION",
            "MIXED_USE_BUILDING",
            "MANOR_HOUSE",
            "LOFT",
            "BUNGALOW",
            "KOT",
            "CASTLE",
            "CHALET",
            "OTHER_PROPERTY",
            "TRIPLEX",
        ],
    )
    region = st.selectbox(
        "Region", ["Flanders", "Brussels-Capital", "Wallonia", "MISSING"]
    )
    province = st.selectbox(
        "Province",
        [
            "Antwerp",
            "East Flanders",
            "Brussels",
            "Walloon Brabant",
            "Flemish Brabant",
            "Liège",
            "West Flanders",
            "Hainaut",
            "Luxembourg",
            "Limburg",
            "Namur",
            "MISSING",
        ],
    )
    locality = st.selectbox(
        "Locality",
        [
            "Antwerp",
            "Gent",
            "Brussels",
            "Turnhout",
            "Nivelles",
            "Halle-Vilvoorde",
            "Liège",
            "Brugge",
            "Sint-Niklaas",
            "Veurne",
            "Verviers",
            "Mechelen",
            "Charleroi",
            "Dendermonde",
            "Bastogne",
            "Leuven",
            "Hasselt",
            "Mons",
            "Aalst",
            "Tournai",
            "Oostend",
            "Oudenaarde",
            "Philippeville",
            "Kortrijk",
            "Dinant",
            "Ieper",
            "Huy",
            "Marche-en-Famenne",
            "Namur",
            "Maaseik",
            "Mouscron",
            "Diksmuide",
            "Soignies",
            "Neufchâteau",
            "Arlon",
            "Tongeren",
            "Waremme",
            "Thuin",
            "Virton",
            "Ath",
            "Roeselare",
            "Tielt",
            "Eeklo",
            "MISSING",
        ],
    )
    zip_code = st.number_input("Zip Code")
    total_area_sqm = st.number_input("Total Area (sqm)")
    if property_type != "APARTMENT":
        surface_land_sqm = st.number_input("Surface Land (sqm)")
    nbr_frontages = st.number_input("Number of Frontages")
    nbr_bedrooms = st.number_input("Number of Bedrooms")
    equipped_kitchen = st.selectbox(
        "Equipped Kitchen",
        [
            "INSTALLED",
            "MISSING",
            "HYPER_EQUIPPED",
            "NOT_INSTALLED",
            "USA_UNINSTALLED",
            "USA_HYPER_EQUIPPED",
            "SEMI_EQUIPPED",
            "USA_INSTALLED",
            "USA_SEMI_EQUIPPED",
        ],
    )
    fl_furnished = st.checkbox("Furnished")
    fl_open_fire = st.checkbox("Open Fire")
    fl_terrace = st.checkbox("Terrace")
    terrace_sqm = st.number_input("Terrace Area (sqm)")
    fl_garden = st.checkbox("Garden")
    garden_sqm = st.number_input("Garden Area (sqm)")
    fl_swimming_pool = st.checkbox("Swimming Pool")
    fl_floodzone = st.checkbox("Floodzone")
    state_building = st.selectbox(
        "State of Building",
        [
            "MISSING",
            "AS_NEW",
            "GOOD",
            "TO_RENOVATE",
            "TO_BE_DONE_UP",
            "JUST_RENOVATED",
            "TO_RESTORE",
        ],
    )
    primary_energy_consumption_sqm = st.number_input("Primary Energy Consumption (sqm)")
    epc = st.selectbox(
        "EPC", ["C", "MISSING", "A", "A+", "D", "B", "E", "G", "F", "A++"]
    )
    heating_type = st.selectbox(
        "Heating Type",
        ["GAS", "MISSING", "FUELOIL", "PELLET", "ELECTRIC", "CARBON", "SOLAR", "WOOD"],
    )
    fl_double_glazing = st.checkbox("Double Glazing")
    cadastral_income = st.number_input("Cadastral Income")

    fl_furnished = int(fl_furnished)
    fl_open_fire = int(fl_open_fire)
    fl_terrace = int(fl_terrace)
    fl_garden = int(fl_garden)
    fl_swimming_pool = int(fl_swimming_pool)
    fl_floodzone = int(fl_floodzone)
    fl_double_glazing = int(fl_double_glazing)

    input_data = {
        "subproperty_type": subproperty_type,
        "region": region,
        "province": province,
        "locality": locality,
        "zip_code": zip_code,
        "total_area_sqm": total_area_sqm,
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
    if property_type == "HOUSE":
        input_data["surface_land_sqm"] = surface_land_sqm

    if st.button("Estimate"):
        if subproperty_type in ["HOUSE", "APARTMENT"]:
            prediction = immo.predict_house(input_data)
        else:
            prediction = immo.predict_apartment(input_data)

        st.write(f"Predicted price: {prediction}")


if __name__ == "__main__":
    main()
