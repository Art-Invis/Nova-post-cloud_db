from auth.domain.branches import Branches
from auth.domain.models import db

class BranchesDAO:
    @staticmethod
    def create(branch_ip, address, hours_id, phone):
        new_branch = Branches(branch_ip=branch_ip, address=address, hours_id=hours_id, phone=phone)
        db.session.add(new_branch)
        db.session.commit()
        return new_branch

    @staticmethod
    def get_all():
        return Branches.query.all()

    @staticmethod
    def get_by_id(branch_id):
        return Branches.query.get(branch_id)

    @staticmethod
    def update(branch_id, branch_ip, address, hours_id, phone):
        branch = Branches.query.get(branch_id)
        if branch:
            branch.branch_ip = branch_ip
            branch.address = address
            branch.hours_id = hours_id
            branch.phone = phone
            db.session.commit()
            return branch
        return None

    @staticmethod
    def delete(branch_id):
        branch = Branches.query.get(branch_id)
        if branch:
            db.session.delete(branch)
            db.session.commit()
