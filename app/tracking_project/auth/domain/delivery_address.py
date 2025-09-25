from auth.domain.models import db

class DeliveryAddress(db.Model):
    __tablename__ = 'delivery_address'

    address_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    delivery_instructions = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<DeliveryAddress {self.address_id}>'