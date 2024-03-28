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

## Sources 📚

Data for this project was sourced from:

- [Immoweb](https://www.immoweb.be/): The primary source of data used in this project. Immoweb is Belgium's leading real estate website, providing listings for properties for sale and rent.
