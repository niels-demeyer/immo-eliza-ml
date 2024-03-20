from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    # Create an instance of ImmoClass
    houses = ImmoClass("HOUSE")
    houses.train_model_random_forest()
    houses.save_model("random_forest")
    houses.print_model_results()
    houses.save_model_results()
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_random_forest()
    apartments.save_model("random_forest")
    apartments.print_model_results()
    apartments.save_model_results()
