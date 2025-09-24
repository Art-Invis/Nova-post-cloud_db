from auth.domain.models import db

class Postmats(db.Model):
    __tablename__ = 'postmats'

    postmat_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id', ondelete='CASCADE'), nullable=False)

    branch = db.relationship('Branches', backref='postmats')

    def __repr__(self):
        return f'<Postmats {self.postmat_id}>'
