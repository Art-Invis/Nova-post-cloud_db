from flask import request, jsonify
from app import app, db
from auth.service.senders_service import SendersService

@app.route('/senders', methods=['GET'])
def get_senders():
    try:
        senders = SendersService.get_all_senders()
        result = [
            {
                "sender_id": sender.sender_id,
                "full_name": sender.full_name,
                "phone": sender.phone,
                "email": sender.email
            } for sender in senders
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/senders/<int:sender_id>', methods=['GET'])
def get_sender_by_id(sender_id):
    try:
        sender = SendersService.get_sender_by_id(sender_id)
        result = {
            "sender_id": sender.sender_id,
            "full_name": sender.full_name,
            "phone": sender.phone,
            "email": sender.email
        }
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/senders', methods=['POST'])
def add_sender():
    try:
        data = request.get_json()
        new_sender = SendersService.add_sender(
            data['full_name'],
            data['phone'],
            data['email']
        )
        return jsonify({"message": "Sender added successfully", "sender_id": new_sender.sender_id}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/senders/<int:sender_id>', methods=['PUT'])
def update_sender(sender_id):
    try:
        data = request.get_json()
        updated_sender = SendersService.update_sender(
            sender_id,
            data.get('full_name'),
            data.get('phone'),
            data.get('email')
        )
        return jsonify({"message": "Sender updated successfully"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/senders/<int:sender_id>', methods=['DELETE'])
def delete_sender(sender_id):
    try:
        SendersService.delete_sender(sender_id)
        return jsonify({"message": "Sender deleted successfully"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
