from auth.dao.payment_dao import PaymentDAO
from flask import jsonify

class PaymentService:
    @staticmethod
    def get_all_payments():
        try:
            payments = PaymentDAO.get_all()
            return payments
        except Exception as e:
            raise Exception(f"Error retrieving payments: {str(e)}")

    @staticmethod
    def get_payment_by_id(payment_id: int):
        """Отримання платіжного запису за ID."""
        try:
            payment = PaymentDAO.get_by_id(payment_id)
            if not payment:
                raise ValueError("Payment not found.")
            return payment
        except Exception as e:
            raise Exception(f"Error retrieving payment: {str(e)}")

    @staticmethod
    def add_payment(package_id, amount, payment_date, payment_status):
        if not package_id or not amount or not payment_date or not payment_status:
            raise ValueError("All fields are required.")

        try:
            new_payment = PaymentDAO.create(package_id, amount, payment_date, payment_status)
            return new_payment
        except Exception as e:
            raise Exception(f"Error adding payment: {str(e)}")

    @staticmethod
    def update_payment(payment_id, amount, payment_status):
        payment = PaymentDAO.get_by_id(payment_id)
        if not payment:
            raise ValueError("Payment not found.")

        if amount is not None:
            payment.amount = amount
        if payment_status is not None:
            payment.payment_status = payment_status

        try:
            PaymentDAO.update(payment)
            return payment
        except Exception as e:
            raise Exception(f"Error updating payment: {str(e)}")

    @staticmethod
    def delete_payment(payment_id):
        # Перевірка існування платежу
        payment = PaymentDAO.get_by_id(payment_id)
        if not payment:
            raise ValueError("Payment not found.")

        try:
            PaymentDAO.delete(payment_id)
        except Exception as e:
            raise Exception(f"Error deleting payment: {str(e)}")
