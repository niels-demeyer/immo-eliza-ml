from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    # Create an instance of ImmoClass
    houses = ImmoClass("HOUSE")
    houses.train_model_random_forest()
    houses.save_model("houses", "random_forest")
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_random_forest()
    apartments.save_model("apartments", "random_forest")
