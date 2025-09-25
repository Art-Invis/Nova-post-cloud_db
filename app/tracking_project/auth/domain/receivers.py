from auth.domain.models import db

class Receivers(db.Model):
    __tablename__ = 'receivers'

    receiver_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Receivers {self.receiver_id}>'