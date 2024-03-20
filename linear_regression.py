from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    # Create an instance of ImmoClass
    houses = ImmoClass("HOUSE")
    houses.train_model_linear()
    houses.print_model_results("linear")
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_linear()
    houses.print_model_results("linear")
