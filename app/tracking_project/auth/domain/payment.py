from app import db

class Payment(db.Model):
    __tablename__ = 'payment'

    payment_id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.package_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    payment_status = db.Column(db.Enum('Pending', 'Paid', 'Failed'), nullable=False)

    package = db.relationship('Packages', backref=db.backref('payments', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<Payment {self.payment_id}>'
