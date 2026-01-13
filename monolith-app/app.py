from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify({"module": "User"})

@app.route("/products")
def products():
    return jsonify({"module": "Product"})

@app.route("/orders")
def orders():
    return jsonify({"module": "Order"})

app.run(host="0.0.0.0", port=5000)
