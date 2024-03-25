from ImmoClass_file import ImmoClass

if __name__ == "__main__":
    houses = ImmoClass("HOUSE")
    houses.train_model_knn()
    houses.save_model("houses", "knn")
    apartments = ImmoClass("APARTMENT")
    apartments.train_model_knn()
