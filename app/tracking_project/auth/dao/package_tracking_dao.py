from auth.domain.package_tracking import PackageTracking
from auth.domain.models import db

class PackageTrackingDAO:
    @staticmethod
    def create(package_id, branch_id, status, timestap):
        new_tracking = PackageTracking(package_id=package_id, branch_id=branch_id, status=status, timestap=timestap)
        db.session.add(new_tracking)
        db.session.commit()
        return new_tracking

    @staticmethod
    def get_all():
        return PackageTracking.query.all()

    @staticmethod
    def get_by_id(tracking_id):
        return PackageTracking.query.get(tracking_id)

    @staticmethod
    def update(tracking_id, package_id, branch_id, status, timestap):
        tracking = PackageTracking.query.get(tracking_id)
        if tracking:
            tracking.package_id = package_id
            tracking.branch_id = branch_id
            tracking.status = status
            tracking.timestap = timestap
            db.session.commit()
            return tracking
        return None

    @staticmethod
    def delete(tracking_id):
        tracking = PackageTracking.query.get(tracking_id)
        if tracking:
            db.session.delete(tracking)
            db.session.commit()
