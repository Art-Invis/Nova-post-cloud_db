from auth.domain.receivers import Receivers
from auth.domain.models import db

class ReceiversDAO:
    @staticmethod
    def create(receiver: Receivers) -> Receivers:
        db.session.add(receiver)
        db.session.commit()
        return receiver

    @staticmethod
    def get_all() -> list:
        return Receivers.query.all()

    @staticmethod
    def get_by_id(receiver_id: int) -> Receivers:
        return Receivers.query.get(receiver_id)

    @staticmethod
    def update(receiver_id: int, name: str, email: str, phone: str) -> bool:
        """Оновлення інформації про отримувача."""
        try:
            receiver = Receivers.query.get(receiver_id)
            if not receiver:
                return False  
            
            receiver.name = name
            receiver.email = email
            receiver.phone = phone
            
            db.session.commit()  
            return True  
        except Exception as e:
            db.session.rollback()  
            raise Exception(f"Error updating receiver: {str(e)}")
    @staticmethod
    def delete(receiver_id: int) -> bool:
        receiver = Receivers.query.get(receiver_id)
        if receiver:
            db.session.delete(receiver)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_all_with_packages():
        """
        Отримати всіх отримувачів разом із їхніми пакунками.
        """
        return Receivers.query.options(db.joinedload('packages')).all()
