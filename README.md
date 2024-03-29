# Belgium Real Estate Dataset 🏡

## Description 📝

This project aims to make a price prediction model for real estate using machine learning.
You can check out the result via [this link.](https://immo-eliza-ml-niels-demeyer.streamlit.app/)

## Table of Contents

- [Installation ⚙️](#installation-⚙️)
- [Usage 🚀](#usage-🚀)
- [Sources 📚](#sources-📚)

## Installation ⚙️

**Prerequisites**

Ensure you have Git and Python installed on your system. Some commands in the manual may differ depending on the operating system and terminal used.

**Clone the repository using `git` command:**

    git clone git@github.com:niels-demeyer/immo-eliza-ml.git

**Navigate to the root of the repository using `cd` command**:

    cd immo-eliza-ml

**Install the required packages using `pip` command:**

    pip3 install -r requirements.txt

## Usage 🚀

**run the model files**

1. Choose the desired script based on the machine learning algorithm you want to use (KNN, Linear Regression, Random Forest Regression, or XGBoost Regression).
2. Run the script using the command line or terminal:
   - For KNN: `python knn.py`
   - For Linear Regression: `python linear_regression.py`
   - For Random Forest Regression: `python random_forest.py`
   - For XGBoost Regression: `python model_xgboost.py`
3. The script will create an instance of the respective machine learning algorithm for houses and apartments, train their models, save the models, print the model results, and save the results to pkl files.

**predict a property**

Define a property you want a prediction on in the `python predict.py` and the xgboost model will be used to give you a prediction.

## API 🌐

The results of the models can be served trough a flask api. This can be done in two ways: flask, docker

1. To serve the api locally with flask you can run `flask run app.py` in the `server` folder
2. You can also serve the api containerized by using the dockerfile. The port is set to 5000 so to test it out on your device `docker run -p 5000:5000 immo-eliza-api`

```
# Example of how you can make a request.
curl -X POST -H "Content-Type: application/json" -d '{"subproperty_type": "HOUSE","region": "Flanders","province": "Antwerp","locality": "Antwerp","zip_code": 2050,"total_area_sqm": 200.0,"surface_land_sqm": 100.0,"nbr_frontages": 2,"nbr_bedrooms": 3,"equipped_kitchen": "INSTALLED","fl_furnished": 0,"fl_open_fire": 0,"fl_terrace": 1,"terrace_sqm": 20.0,"fl_garden": 1,"garden_sqm": 50.0,"fl_swimming_pool": 0,"fl_floodzone": 0,"state_building": "NEW","primary_energy_consumption_sqm": 100.0,"epc": 200,"heating_type": "GAS","fl_double_glazing": 1,"cadastral_income": 2000}' http://127.0.0.1:5000/predict/house
```

## Streamlit 🌐

The most user friendly way to interact with the model is to use the [streamlit](https://immo-eliza-ml-niels-demeyer.streamlit.app/) application.

To run the streamlit application locally you need to use the command `streamlit run app.py` in the streamlit folder.

## Sources 📚

Data for this project was sourced from:

- [Immoweb](https://www.immoweb.be/): The primary source of data used in this project. Immoweb is Belgium's leading real estate website, providing listings for properties for sale and rent.
