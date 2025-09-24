from auth.domain.models import db

class Couriers(db.Model):
    __tablename__ = 'couriers'

    courier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    vehicle_type = db.Column(db.Enum('Car', 'Bike', 'Van'), nullable=False)

    def __repr__(self):
        return f'<Couriers {self.courier_id}>'