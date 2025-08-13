from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/send-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    print(f"Received data: {data}")
    return jsonify({'message': 'Data received successfully', 'received_data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
