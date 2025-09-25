from auth.domain.senders import Senders
from auth.domain.models import db

class SendersDAO:
    @staticmethod
    def create(full_name, phone, email):
        new_sender = Senders(full_name=full_name, phone=phone, email=email)
        db.session.add(new_sender)
        db.session.commit()
        return new_sender

    @staticmethod
    def get_all():
        return Senders.query.all()

    @staticmethod
    def get_by_id(sender_id):
        return Senders.query.get(sender_id)

    @staticmethod
    def update(sender_id, full_name, phone, email):
        sender = Senders.query.get(sender_id)
        if sender:
            sender.full_name = full_name
            sender.phone = phone
            sender.email = email
            db.session.commit()
            return sender
        return None

    @staticmethod
    def delete(sender_id):
        sender = Senders.query.get(sender_id)
        if sender:
            db.session.delete(sender)
            db.session.commit()
