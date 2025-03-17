from flask import Flask, jsonify

app = Flask(__name__)

# Define a custom error handler for 404 (Not Found) errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Define a custom error handler for 500 (Internal Srver Error)
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "An internal server error occurred"}), 500

@app.route("/")
def index():
    return jsonify({"message": "Hello, Khyri!"})  # Returns JSON response

@app.route("/greeting/<name>")
def greeting(name):
    return jsonify({"message": f"Hello, {name}!"}) # Dynamic greeting

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)