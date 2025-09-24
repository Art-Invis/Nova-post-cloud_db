from auth.domain.postmats import Postmats
from auth.domain.models import db

class PostmatsDAO:
    @staticmethod
    def create(location, status, branch_id):
        new_postmat = Postmats(location=location, status=status, branch_id=branch_id)
        db.session.add(new_postmat)
        db.session.commit()
        return new_postmat

    @staticmethod
    def get_all():
        return Postmats.query.all()

    @staticmethod
    def get_by_id(postmat_id):
        return Postmats.query.get(postmat_id)

    @staticmethod
    def update(postmat_id, location, status, branch_id):
        postmat = Postmats.query.get(postmat_id)
        if postmat:
            postmat.location = location
            postmat.status = status
            postmat.branch_id = branch_id
            db.session.commit()
            return postmat
        return None

    @staticmethod
    def delete(postmat_id: int) -> bool:
        postmat = Postmats.query.get(postmat_id)
        if postmat:
            db.session.delete(postmat)
            db.session.commit()
            return True
        return False
