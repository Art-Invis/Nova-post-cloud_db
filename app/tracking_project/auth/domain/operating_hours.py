from auth.domain.models import db

class OperatingHours(db.Model):
    __tablename__ = 'operating_hours'

    hours_id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(50), nullable=False)
    open_time = db.Column(db.Time, nullable=False)
    close_time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f'<OperatingHours {self.hours_id}>'