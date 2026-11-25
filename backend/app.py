from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MENU = [
    {"id": 1, "name": "Burger", "price": 5.0, "category": "Main"},
    {"id": 2, "name": "Pizza Slice", "price": 3.0, "category": "Main"},
    {"id": 3, "name": "Fries", "price": 2.0, "category": "Side"},
    {"id": 4, "name": "Orange Juice", "price": 2.0, "category": "Drink"},
]

@app.route("/api/menu")
def get_menu():
    return jsonify(MENU)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
