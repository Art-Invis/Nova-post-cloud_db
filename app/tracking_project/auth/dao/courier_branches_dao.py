from auth.domain.models import db
from auth.domain.courier_branches import CourierBranches


class CourierBranchesDAO:
    @staticmethod
    def create(courier_id, branch_id):
        new_relation = CourierBranches(courier_id=courier_id, branch_id=branch_id)
        db.session.add(new_relation)
        db.session.commit()
        return new_relation

    @staticmethod
    def get_all():
        return CourierBranches.query.all()

    @staticmethod
    def get_by_courier_id(courier_id):
        return CourierBranches.query.filter_by(courier_id=courier_id).all()

    @staticmethod
    def get_by_branch_id(branch_id):
        return CourierBranches.query.filter_by(branch_id=branch_id).all()

    @staticmethod
    def delete(courier_id, branch_id):
        relation = CourierBranches.query.filter_by(courier_id=courier_id, branch_id=branch_id).first()
        if relation:
            db.session.delete(relation)
            db.session.commit()
            return True
        return False
