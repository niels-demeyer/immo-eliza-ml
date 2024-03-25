from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    # Create an instance of ImmoClass
    houses = ImmoClass("HOUSE")
    houses.train_model_xgboost()
    houses.save_model("xgboost")
    houses.print_model_results()
    houses.save_model_results()
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_xgboost()
    apartments.save_model("xgboost")
    apartments.print_model_results()
    apartments.save_model_results()
