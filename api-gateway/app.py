from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "API Gateway is running!"

# Example route to forward requests to user-service
@app.route('/users')
def users():
    try:
        # Forward request to the user-service container
        resp = requests.get('http://host.docker.internal:5001/users')
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Example route for monolith-app
@app.route('/monolith')
def monolith():
    try:
        resp = requests.get('http://host.docker.internal:5000/')
        return jsonify({"message": resp.text})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

