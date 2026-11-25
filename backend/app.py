from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MENU = [
    {"id": 1, "name": "Burger", "price": 5.0, "category": "Main"},
    {"id": 2, "name": "Pizza Slice", "price": 3.0, "category": "Main"},
    {"id": 3, "name": "Fries", "price": 2.0, "category": "Side"},
    {"id": 4, "name": "Orange Juice", "price": 2.0, "category": "Drink"},
]

ORDERS = [
    {"id": 101, "customer": "Sara", "items": "Burger, Fries", "status": "Pending"},
    {"id": 102, "customer": "Ahmad", "items": "Pizza Slice, Orange Juice", "status": "Preparing"},
]

@app.route("/api/menu")
def get_menu():
    return jsonify(MENU)

@app.route("/api/orders", methods=["GET"])
def get_orders():
    return jsonify(ORDERS)

@app.route("/api/orders/<int:order_id>/status", methods=["PUT"])
def update_order_status(order_id):
    data = request.get_json()
    for order in ORDERS:
        if order["id"] == order_id:
            order["status"] = data.get("status", order["status"])
            return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)