from auth.dao.senders_dao import SendersDAO  
from flask import jsonify

class SendersService:
    @staticmethod
    def get_all_senders():
        try:
            senders = SendersDAO.get_all()
            return senders
        except Exception as e:
            raise Exception(f"Error retrieving senders: {str(e)}")

    @staticmethod
    def get_sender_by_id(sender_id: int):
        """Отримання відправника за ID."""
        try:
            sender = SendersDAO.get_by_id(sender_id)
            if not sender:
                raise ValueError("Sender not found.")
            return sender
        except Exception as e:
            raise Exception(f"Error retrieving sender: {str(e)}")
        
    @staticmethod
    def add_sender(full_name, phone, email):
        if not full_name or not phone or not email:
            raise ValueError("All fields are required.")
        
        try:
            new_sender = SendersDAO.create(full_name, phone, email)
            return new_sender
        except Exception as e:
            raise Exception(f"Error adding sender: {str(e)}")

    @staticmethod
    def update_sender(sender_id, full_name, phone, email):
        sender = SendersDAO.get_by_id(sender_id)
        if not sender:
            raise ValueError("Sender not found.")
        
        if full_name is not None:
            sender.full_name = full_name
        if phone is not None:
            sender.phone = phone
        if email is not None:
            sender.email = email
        
        try:
            SendersDAO.update(sender)
            return sender
        except Exception as e:
            raise Exception(f"Error updating sender: {str(e)}")

    @staticmethod
    def delete_sender(sender_id):
        # Перевірка існування відправника
        sender = SendersDAO.get_by_id(sender_id)
        if not sender:
            raise ValueError("Sender not found.")

        try:
            SendersDAO.delete(sender_id)
        except Exception as e:
            raise Exception(f"Error deleting sender: {str(e)}")
