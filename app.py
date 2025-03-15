from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello, Khyri!"})  # Returns JSON response

@app.route("/greeting/<name>")
def greeting(name):
    return jsonify({"message": f"Hello, {name}!"}) # Dynamic greeting

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)