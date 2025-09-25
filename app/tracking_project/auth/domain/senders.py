from auth.domain.models import db

class Senders(db.Model):
    __tablename__ = 'senders'

    sender_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    

    def __repr__(self):
        return f'<Senders {self.sender_id}, Name: {self.full_name}>'
