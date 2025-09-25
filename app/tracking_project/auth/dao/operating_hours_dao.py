from auth.domain.operating_hours import OperatingHours
from auth.domain.models import db
from auth.domain.branches import Branches
from auth.domain.branches_senders import BranchesSenders

class OperatingHoursDAO:
    @staticmethod
    def create(day, open_time, close_time):
        new_hours = OperatingHours(day=day, open_time=open_time, close_time=close_time)
        db.session.add(new_hours)
        db.session.commit()
        return new_hours

    @staticmethod
    def get_all():
        return OperatingHours.query.all()

    @staticmethod
    def get_by_id(hours_id):
        return OperatingHours.query.get(hours_id)

    @staticmethod
    def update(hours_id, day, open_time, close_time):
        hours = OperatingHours.query.get(hours_id)
        if hours:
            hours.day = day
            hours.open_time = open_time
            hours.close_time = close_time
            db.session.commit()
            return hours
        return None

    @staticmethod
    def delete(hours_id: int) -> bool:
        try:
            hours = OperatingHours.query.get(hours_id)
            if not hours:
                return False  

            
            branches = Branches.query.filter_by(hours_id=hours_id).all()
            for branch in branches:
                
                BranchesSenders.query.filter_by(branch_id=branch.branch_id).delete()

            
            Branches.query.filter_by(hours_id=hours_id).delete()

           
            db.session.delete(hours)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()  
            raise Exception(f"Error deleting operating hours: {str(e)}")
