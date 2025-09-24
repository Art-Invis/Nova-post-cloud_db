from auth.domain.models import db

class Packages(db.Model):
    __tablename__ = 'packages'

    package_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('senders.sender_id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('receivers.receiver_id'), nullable=False)
    delivery_address_id = db.Column(db.Integer, db.ForeignKey('delivery_address.address_id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    sender = db.relationship('Senders', backref=db.backref('packages', cascade='all, delete-orphan'))
    receiver = db.relationship('Receivers', backref=db.backref('packages', cascade='all, delete-orphan'))
    delivery_address = db.relationship('DeliveryAddress', backref=db.backref('packages', cascade='all, delete-orphan'))


    def __repr__(self):
        return f'<Packages {self.package_id}>'
