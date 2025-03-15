from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello, Khyri!"})  # Returns JSON response

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
