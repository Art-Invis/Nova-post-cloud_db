from auth.domain.models import db

class PackageTracking(db.Model):
    __tablename__ = 'package_tracking'

    tracking_id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.package_id'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    timestap = db.Column(db.DateTime, nullable=False)

    package = db.relationship('Packages', backref=db.backref('tracking', cascade='all, delete-orphan'))
    branch = db.relationship('Branches', backref='tracking')

    def __repr__(self):
        return f'<PackageTracking {self.tracking_id}>'
