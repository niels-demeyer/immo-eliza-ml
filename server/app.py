import sys
import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from training.ImmoClass_file import ImmoClass

# Create an instance of the Flask class
app = Flask(__name__)
CORS(app)  # Enable CORS on your Flask application


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
    app.run(host="0.0.0.0", debug=True)
