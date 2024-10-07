from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()  # Get the JSON data sent by the front-end
    name = data.get('name')  # Extract the 'name' value
    message = f"Hello, {name}! Welcome to our website!"  # Create the greeting message

    return jsonify({"message": message})  # Return the message as JSON response


if __name__ == '__main__':
    app.run(debug=True)
