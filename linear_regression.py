from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    # Create an instance of ImmoClass
    houses = ImmoClass("HOUSE")
    houses.train_model_linear()
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_linear()
