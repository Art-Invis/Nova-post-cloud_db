from auth.domain.models import db

class Branches(db.Model):
    __tablename__ = 'branches'

    branch_id = db.Column(db.Integer, primary_key=True)
    branch_ip = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    hours_id = db.Column(db.Integer, db.ForeignKey('operating_hours.hours_id', ondelete='CASCADE'), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    operating_hours = db.relationship('OperatingHours', backref=db.backref('branches', cascade='all, delete-orphan'))  # Каскадне видалення


    def __repr__(self):
        return f'<Branches {self.branch_id}, Address: {self.address}>'
