from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify({"service": "User"})

app.run(host="0.0.0.0", port=5001)
