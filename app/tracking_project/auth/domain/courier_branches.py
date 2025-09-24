from auth.domain.models import db

class CourierBranches(db.Model):
    __tablename__ = 'courier_branches'

    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'), primary_key=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id'), primary_key=True)

    courier = db.relationship('Couriers', backref=db.backref('courier_branches', cascade='all, delete-orphan'))
    branch = db.relationship('Branches', backref=db.backref('courier_branches', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<CourierBranches {self.courier_id}, {self.branch_id}>'