from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    # Create an instance of ImmoClass
    houses = ImmoClass("HOUSE")
    houses.train_model_random_forest()
    houses.print_model_results("random_forest")
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_random_forest()
    apartments.print_model_results("random_forest")
