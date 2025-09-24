from app import db
from auth.domain.packages import Packages 
from auth.domain.receivers import Receivers
from auth.domain.senders import Senders

class PackagesDAO:
    @staticmethod
    def get_all():
        return Packages.query.all()

    @staticmethod
    def create(sender_id, receiver_id, delivery_address_id, description, status):
        new_package = Packages(
            sender_id=sender_id,
            receiver_id=receiver_id,
            delivery_address_id=delivery_address_id,
            description=description,
            status=status
        )
        db.session.add(new_package)
        db.session.commit()
        return new_package

    @staticmethod
    def get_by_id(package_id):
        return Packages.query.get(package_id)

    @staticmethod
    def update(package):
        db.session.commit()

    @staticmethod
    def delete(package_id):
        package = Packages.query.get(package_id)
        if package:
            db.session.delete(package)
            db.session.commit()
    @staticmethod
    def delete_by_receiver_id(receiver_id: int) -> bool:
        """Видалення всіх пакетів, пов'язаних з отримувачем."""
        try:
            packages = Packages.query.filter_by(receiver_id=receiver_id).all()
            for package in packages:
                db.session.delete(package)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error deleting packages for receiver_id {receiver_id}: {str(e)}")
        
    @staticmethod
    def get_all_with_receivers():
        """Отримати всі пакунки з інформацією про отримувачів."""
        return db.session.query(Packages, Receivers).join(Receivers).all()
    
    @staticmethod
    def get_all_with_senders():
        """Отримати всі пакунки з інформацією про відправників."""
        return db.session.query(Packages, Senders).join(Senders).all()