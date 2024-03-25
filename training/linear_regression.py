from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    # Create an instance of ImmoClass
    houses = ImmoClass("HOUSE")
    houses.train_model_linear()
    houses.save_model("linear")
    houses.print_model_results()
    houses.save_model_results()
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_linear()
    apartments.save_model("linear")
    apartments.print_model_results()
    apartments.save_model_results()
