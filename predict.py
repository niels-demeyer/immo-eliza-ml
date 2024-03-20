from ImmoClass_file import ImmoClass

# Define a dictionary called input_apartment with the following structure:
# input_apartment = {
#     'subproperty_type': 'value',  # Categorical
#     'region': 'value',  # Categorical
#     'province': 'value',  # Categorical
#     'locality': 'value',  # Categorical
#     'zip_code': value,  # Numeric
#     'total_area_sqm': value,  # Numeric
#     'surface_land_sqm': value,  # Numeric
#     'nbr_frontages': value,  # Numeric
#     'nbr_bedrooms': value,  # Numeric
#     'equipped_kitchen': 'value',  # Categorical
#     'fl_furnished': value,  # Ordinal (0 or 1)
#     'fl_open_fire': value,  # Ordinal (0 or 1)
#     'fl_terrace': value,  # Ordinal (0 or 1)
#     'terrace_sqm': value,  # Numeric
#     'fl_garden': value,  # Ordinal (0 or 1)
#     'garden_sqm': value,  # Numeric
#     'fl_swimming_pool': value,  # Ordinal (0 or 1)
#     'fl_floodzone': value,  # Ordinal (0 or 1)
#     'state_building': 'value',  # Categorical
#     'primary_energy_consumption_sqm': value,  # Numeric
#     'epc': value,  # Numeric
#     'heating_type': 'value',  # Categorical
#     'fl_double_glazing': value,  # Ordinal (0 or 1)
#     'cadastral_income': value  # Numeric
# }


if __name__ == "__main__":
    # define the input_apartment dictionary
    input_apartment = {
        "subproperty_type": "APARTMENT",  # Categorical
        "region": "Flanders",  # Categorical
        "province": "Antwerp",  # Categorical
        "locality": "Antwerp",  # Categorical
        "zip_code": 2050,  # Numeric
        "total_area_sqm": 100.0,  # Numeric
        "surface_land_sqm": 50.0,  # Numeric
        "nbr_frontages": 2,  # Numeric
        "nbr_bedrooms": 2,  # Numeric
        "equipped_kitchen": "INSTALLED",  # Categorical
        "fl_furnished": 0,  # Ordinal (0 or 1)
        "fl_open_fire": 0,  # Ordinal (0 or 1)
        "fl_terrace": 1,  # Ordinal (0 or 1)
        "terrace_sqm": 10.0,  # Numeric
        "fl_garden": 0,  # Ordinal (0 or 1)
        "garden_sqm": 0.0,  # Numeric
        "fl_swimming_pool": 0,  # Ordinal (0 or 1)
        "fl_floodzone": 0,  # Ordinal (0 or 1)
        "state_building": "NEW",  # Categorical
        "primary_energy_consumption_sqm": 100.0,  # Numeric
        "epc": 200,  # Numeric
        "heating_type": "GAS",  # Categorical
        "fl_double_glazing": 1,  # Ordinal (0 or 1)
        "cadastral_income": 1000,  # Numeric
    }
    input_house = {
        "subproperty_type": "HOUSE",  # Categorical
        "region": "Flanders",  # Categorical
        "province": "Antwerp",  # Categorical
        "locality": "Antwerp",  # Categorical
        "zip_code": 2050,  # Numeric
        "total_area_sqm": 200.0,  # Numeric
        "surface_land_sqm": 100.0,  # Numeric
        "nbr_frontages": 2,  # Numeric
        "nbr_bedrooms": 3,  # Numeric
        "equipped_kitchen": "INSTALLED",  # Categorical
        "fl_furnished": 0,  # Ordinal (0 or 1)
        "fl_open_fire": 0,  # Ordinal (0 or 1)
        "fl_terrace": 1,  # Ordinal (0 or 1)
        "terrace_sqm": 20.0,  # Numeric
        "fl_garden": 1,  # Ordinal (0 or 1)
        "garden_sqm": 50.0,  # Numeric
        "fl_swimming_pool": 0,  # Ordinal (0 or 1)
        "fl_floodzone": 0,  # Ordinal (0 or 1)
        "state_building": "NEW",  # Categorical
        "primary_energy_consumption_sqm": 100.0,  # Numeric
        "epc": 200,  # Numeric
        "heating_type": "GAS",  # Categorical
        "fl_double_glazing": 1,  # Ordinal (0 or 1)
        "cadastral_income": 2000,  # Numeric
    }
    # Create an instance of ImmoClass for house
    immo_house = ImmoClass("HOUSE")

    # Use the predict_house method with the input_house dictionary
    house = immo_house.predict_house(input_house)
    print(f"Predicted price for the house: {house}")
    # Create an instance of ImmoClass
    immo = ImmoClass("APARTMENT")
    # Use the predict_apartment method with the input_apartment dictionary
    apartment = immo.predict_apartment(input_apartment)
    print(f"Predicted price for the apartment: {apartment}")
