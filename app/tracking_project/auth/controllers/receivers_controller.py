from flask import request, jsonify
from app import app
from auth.service.receivers_service import ReceiversService

@app.route('/receivers', methods=['POST'])
def create_receiver():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'phone']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        new_receiver = ReceiversService.create_receiver(data)
        return jsonify({
            "message": "Receiver created successfully", 
            "receiver_id": new_receiver.receiver_id,
            "name": new_receiver.name,
            "email": new_receiver.email,
            "phone": new_receiver.phone
        }), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Error creating receiver: {str(e)}"}), 500

@app.route('/receivers', methods=['GET'])
def get_receivers():
    try:
        receivers = ReceiversService.get_all_receivers()
        result = [
            {
                "receiver_id": receiver.receiver_id,
                "name": receiver.name,
                "email": receiver.email,
                "phone": receiver.phone
            } for receiver in receivers
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving receivers: {str(e)}"}), 500


@app.route('/receivers/<int:receiver_id>', methods=['GET'])
def get_receiver_by_id(receiver_id):
    try:
        receiver = ReceiversService.get_receiver_by_id(receiver_id)
        if receiver:
            result = {
                "receiver_id": receiver.receiver_id,
                "name": receiver.name,
                "email": receiver.email,
                "phone": receiver.phone
            }
            return jsonify(result), 200
        else:
            return jsonify({"error": "Receiver not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Error retrieving receiver: {str(e)}"}), 500

@app.route('/receivers/<int:receiver_id>', methods=['PUT'])
def update_receiver(receiver_id):
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided for update"}), 400

        updated_receiver = ReceiversService.update_receiver(
            receiver_id, data.get('name'), data.get('email'), data.get('phone')
        )
        if updated_receiver:
            return jsonify({"message": "Receiver updated successfully"}), 200
        else:
            return jsonify({"error": "Receiver not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Error updating receiver: {str(e)}"}), 500

@app.route('/receivers/<int:receiver_id>', methods=['DELETE'])
def delete_receiver(receiver_id):
    try:
        success = ReceiversService.delete_receiver(receiver_id)
        if success:
            return jsonify({"message": "Receiver deleted successfully"}), 200
        else:
            return jsonify({"error": "Receiver not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Error deleting receiver: {str(e)}"}), 500