from app import db
from auth.domain.payment import Payment

class PaymentDAO:
    @staticmethod
    def get_all():
        return Payment.query.all()

    @staticmethod
    def create(package_id, amount, payment_date, payment_status):
        new_payment = Payment(
            package_id=package_id,
            amount=amount,
            payment_date=payment_date,
            payment_status=payment_status
        )
        db.session.add(new_payment)
        db.session.commit()
        return new_payment

    @staticmethod
    def get_by_id(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def update(payment):
        db.session.commit()

    @staticmethod
    def delete(payment_id):
        payment = Payment.query.get(payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()
