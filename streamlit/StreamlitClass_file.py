import streamlit as st


class StreamlitClass:
    def __init__(self):
        self.property_type = None
        self.subproperty_type = None
        self.region = None
        self.locality = None
        self.province = None
        self.zip_code = None
        self.total_area_sqm = None
        self.surface_land_sqm = None
        self.nbr_frontages = None
        self.nbr_bedrooms = None
        self.equipped_kitchen = None
        self.fl_furnished = None
        self.fl_open_fire = None
        self.fl_terrace = None
        self.terrace_sqm = None
        self.fl_garden = None
        self.garden_sqm = None
        self.fl_swimming_pool = None
        self.fl_floodzone = None
        self.state_building = None
        self.primary_energy_consumption_sqm = None
        self.epc = None
        self.heating_type = None
        self.fl_double_glazing = None
        self.cadastral_income = None

    def selectbox(self, label, options):
        return st.selectbox(label, options)

    def number_input(self, label, min_value=0, max_value=100, value=50):
        return st.slider(label, min_value, max_value, value)

    def checkbox(self, label):
        return st.checkbox(label)

    def convert_to_int(self, boolean_value):
        return int(boolean_value)

    def select_property_type(self):
        self.property_type = self.selectbox(
            "Select Property Type", ["APARTMENT", "HOUSE"]
        )

    def select_subproperty_type(self):
        self.subproperty_type = self.selectbox(
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

    def select_region(self):
        self.region = self.selectbox(
            "Region", ["Flanders", "Brussels-Capital", "Wallonia"]
        )

    def select_province(self):
        self.province = self.selectbox(
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
            ],
        )

    def select_locality(self):
        self.locality = self.selectbox(
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
            ],
        )

    def select_zip_code(self):
        self.zip_code = self.number_input("Zip Code")

    def select_total_area_sqm(self):
        self.total_area_sqm = self.number_input("Total Area (sqm)")

    def select_surface_land_sqm(self):
        self.surface_land_sqm = self.number_input("Surface Land (sqm)")

    def select_nbr_frontages(self):
        self.nbr_frontages = self.number_input("Number of Frontages")

    def select_nbr_bedrooms(self):
        self.nbr_bedrooms = self.number_input("Number of Bedrooms")

    def select_equipped_kitchen(self):
        self.equipped_kitchen = self.selectbox(
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

    def select_fl_furnished(self):
        self.fl_furnished = self.checkbox("Furnished")
        self.fl_furnished = self.convert_to_int(self.fl_furnished)

    def select_fl_open_fire(self):
        self.fl_open_fire = self.checkbox("Open Fire")
        self.fl_open_fire = self.convert_to_int(self.fl_open_fire)

    def select_fl_terrace(self):
        self.fl_terrace = self.checkbox("Terrace")
        self.fl_terrace = self.convert_to_int(self.fl_terrace)

    def select_terrace_sqm(self):
        self.terrace_sqm = self.number_input("Terrace Area (sqm)")

    def select_fl_garden(self):
        self.fl_garden = self.checkbox("Garden")
        self.fl_garden = self.convert_to_int(self.fl_garden)

    def select_garden_sqm(self):
        self.garden_sqm = self.number_input("Garden Area (sqm)")

    def select_fl_swimming_pool(self):
        self.fl_swimming_pool = self.checkbox("Swimming Pool")
        self.fl_swimming_pool = self.convert_to_int(self.fl_swimming_pool)

    def select_fl_floodzone(self):
        self.fl_floodzone = self.checkbox("Floodzone")
        self.fl_floodzone = self.convert_to_int(self.fl_floodzone)

    def select_state_building(self):
        self.state_building = self.selectbox(
            "State of Building",
            [
                "MISSING",
                "TO_BE_DONE_UP",
                "TO_RENOVATE",
                "GOOD",
                "JUST_RENOVATED",
                "TO_RESTORE",
                "NEW",
                "TO_FINISH",
            ],
        )

    def select_primary_energy_consumption_sqm(self):
        self.primary_energy_consumption_sqm = self.number_input(
            "Primary Energy Consumption (kWh/m²/year)"
        )

    def select_epc(self):
        self.epc = self.selectbox(
            "EPC", ["C", "MISSING", "A", "A+", "D", "B", "E", "G", "F", "A++"]
        )

    def select_heating_type(self):
        self.heating_type = self.selectbox(
            "Heating Type",
            [
                "GAS",
                "MISSING",
                "FUELOIL",
                "PELLET",
                "ELECTRIC",
                "CARBON",
                "SOLAR",
                "WOOD",
            ],
        )

    def select_fl_double_glazing(self):
        self.fl_double_glazing = self.checkbox("Double Glazing")
        self.fl_double_glazing = self.convert_to_int(self.fl_double_glazing)

    def select_cadastral_income(self):
        self.cadastral_income = self.number_input("Cadastral Income")

    def get_input_data(self):
        input_data = {
            "property_type": self.property_type,
            "subproperty_type": self.subproperty_type,
            "region": self.region,
            "province": self.province,
            "locality": self.locality,
            "zip_code": self.zip_code,
            "total_area_sqm": self.total_area_sqm,
            "surface_land_sqm": self.surface_land_sqm,
            "nbr_frontages": self.nbr_frontages,
            "nbr_bedrooms": self.nbr_bedrooms,
            "equipped_kitchen": self.equipped_kitchen,
            "fl_furnished": self.fl_furnished,
            "fl_open_fire": self.fl_open_fire,
            "fl_terrace": self.fl_terrace,
            "terrace_sqm": self.terrace_sqm,
            "fl_garden": self.fl_garden,
            "garden_sqm": self.garden_sqm,
            "fl_swimming_pool": self.fl_swimming_pool,
            "fl_floodzone": self.fl_floodzone,
            "state_building": self.state_building,
            "primary_energy_consumption_sqm": self.primary_energy_consumption_sqm,
            "epc": self.epc,
            "heating_type": self.heating_type,
            "fl_double_glazing": self.fl_double_glazing,
            "cadastral_income": self.cadastral_income,
        }

        return input_data
