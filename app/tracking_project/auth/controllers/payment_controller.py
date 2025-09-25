from flask import request, jsonify
from app import app, db
from auth.service.payment_service import PaymentService

@app.route('/payment', methods=['GET'])
def get_all_payments():
    try:
        payments = PaymentService.get_all_payments()
        result = [
            {
                "payment_id": payment.payment_id,
                "package_id": payment.package_id,
                "amount": payment.amount,
                "payment_date": payment.payment_date,
                "payment_status": payment.payment_status
            } for payment in payments
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/payment/<int:payment_id>', methods=['GET'])
def get_payment_by_id(payment_id):
    try:
        payment = PaymentService.get_payment_by_id(payment_id)
        result = {
            "payment_id": payment.payment_id,
            "package_id": payment.package_id,
            "amount": payment.amount,
            "payment_date": payment.payment_date,
            "payment_status": payment.payment_status
        }
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/payment', methods=['POST'])
def add_payment():
    try:
        data = request.get_json()
        new_payment = PaymentService.add_payment(
            data['package_id'],
            data['amount'],
            data['payment_date'],
            data['payment_status']
        )
        return jsonify({"message": "Payment added successfully", "payment_id": new_payment.payment_id}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/payment/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    try:
        data = request.get_json()
        updated_payment = PaymentService.update_payment(
            payment_id,
            data.get('amount'),
            data.get('payment_status')
        )
        return jsonify({"message": "Payment updated successfully"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/payment/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    try:
        PaymentService.delete_payment(payment_id)
        return jsonify({"message": "Payment deleted successfully"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
