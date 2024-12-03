from flask import Flask, request, jsonify
from logic import calculate_points
#from storage import receipt_store
import uuid

app = Flask(__name__)
# In-memory receipt data
receipt_store = {}

# Endpoint to process receipts
@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        # Parse JSON input
        receipt = request.get_json()

        # Validate receipt structure
        required_fields = {"retailer", "purchaseDate", "purchaseTime", "items", "total"}
        if not all(field in receipt for field in required_fields):
            return jsonify({"error": "Invalid receipt data"}), 400

        # Generate unique ID
        receipt_id = str(uuid.uuid4())

        # Calculate points
        points = calculate_points(receipt)

        # Store the receipt data in memory
        receipt_store[receipt_id] = points

        # Return the generated ID
        return jsonify({"id": receipt_id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve points
@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    # Check if the ID exists in the store
    if id not in receipt_store:
        return jsonify({"error": "Receipt not found"}), 404

    # Return the points
    points = receipt_store[id]
    return jsonify({"points": points}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
