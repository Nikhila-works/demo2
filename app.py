from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a simple route for GET
@app.route('/niki', methods=['GET'])
def get_data():
    # Sample data to return
    data = {
        "message": "Hello, this is your GET API response!",
        "success": True,
        "data": {
            "id": 1,
            "name": "Sample Item Charith"
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
