from auth.domain.receivers import Receivers  # Імпорт моделі Receivers
from auth.dao.receivers_dao import ReceiversDAO  # Імпорт DAO

class ReceiversService:
    
    @staticmethod
    def create_receiver(data):
        # Створюємо новий об'єкт Receivers
        new_receiver = Receivers(
            name=data['name'],
            phone=data['phone'],
            email=data['email']
        )
        return ReceiversDAO.create(new_receiver)

    @staticmethod
    def get_all_receivers() -> list:
        """Отримання всіх отримувачів."""
        try:
            return ReceiversDAO.get_all()
        except Exception as e:
            raise Exception(f"Error retrieving receivers: {str(e)}")

    @staticmethod
    def get_receiver_by_id(receiver_id: int) -> dict:
        """Отримання отримувача за ID."""
        try:
            receiver = ReceiversDAO.get_by_id(receiver_id)
            if not receiver:
                raise ValueError("Receiver not found.")
            return receiver
        except Exception as e:
            raise Exception(f"Error retrieving receiver: {str(e)}")

    @staticmethod
    def update_receiver(receiver_id: int, name: str, email: str, phone: str) -> bool:
        """Оновлення інформації про отримувача."""
        try:
            # Виклик DAO для оновлення інформації
            return ReceiversDAO.update(receiver_id, name, email, phone)
        except Exception as e:
            raise Exception(f"Error updating receiver: {str(e)}")

    @staticmethod
    def delete_receiver(receiver_id: int) -> bool:
        """Видалення отримувача за ID."""
        try:
            result = ReceiversDAO.delete(receiver_id)
            return result  # Повертає True, якщо видалення пройшло успішно
        except Exception as e:
            raise Exception(f"Error deleting receiver: {str(e)}")
        
    
    @staticmethod
    def get_all_receivers_with_packages():
        """
        Отримати всіх отримувачів разом із їхніми пакунками.
        """
        try:
            receivers = ReceiversDAO.get_all_with_packages()
            result = [
                {
                    "receiver_id": receiver.receiver_id,
                    "name": receiver.name,
                    "email": receiver.email,
                    "phone": receiver.phone,
                    "packages": [
                        {
                            "package_id": package.package_id,
                            "description": package.description,
                            "status": package.status,
                        }
                        for package in receiver.packages
                    ]
                }
                for receiver in receivers
            ]
            return result
        except Exception as e:
            raise Exception(f"Error retrieving receivers with packages: {str(e)}")