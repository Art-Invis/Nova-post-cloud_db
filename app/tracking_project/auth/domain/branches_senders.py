from auth.domain.models import db

class BranchesSenders(db.Model):
    __tablename__ = 'branches_senders'

    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id'), primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('senders.sender_id'), primary_key=True)

    # Зв'язок з моделями Branches та Senders
    branch = db.relationship('Branches', backref=db.backref('branches_senders', cascade='all, delete-orphan'))
    sender = db.relationship('Senders', backref=db.backref('branches_senders', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<BranchesSenders(branch_id={self.branch_id}, sender_id={self.sender_id})>'
