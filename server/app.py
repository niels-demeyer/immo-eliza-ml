import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, jsonify
from training.ImmoClass_file import ImmoClass

# Create an instance of the Flask class
app = Flask(__name__)


# Define the routes for House
@app.route("/predict/house", methods=["POST"])
def predict_house():
    data = request.get_json()
    immo_house = ImmoClass("HOUSE")
    prediction = immo_house.predict_house(data)
    return jsonify({"predicted_price": prediction})


# Define the routes for Apartment
@app.route("/predict/apartment", methods=["POST"])
def predict_apartment():
    data = request.get_json()
    immo_apartment = ImmoClass("APARTMENT")
    prediction = immo_apartment.predict_apartment(data)
    return jsonify({"predicted_price": prediction})


if __name__ == "__main__":
    app.run(debug=True)
