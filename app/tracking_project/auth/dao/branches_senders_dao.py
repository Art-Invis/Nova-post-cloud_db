from auth.domain.branches_senders import BranchesSenders
from auth.domain.models import db
import logging
from auth.domain.branches import Branches
from auth.domain.senders import Senders

class BranchesSendersDAO:
    @staticmethod
    def create(branch_id: int, sender_id: int) -> BranchesSenders:
        try:
            new_relation = BranchesSenders(branch_id=branch_id, sender_id=sender_id)
            db.session.add(new_relation)
            db.session.commit()
            return new_relation
        except Exception as e:
            logging.error(f"Error creating relation: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    def get_all() -> list:
        try:
            return BranchesSenders.query.all()
        except Exception as e:
            logging.error(f"Error retrieving all relations: {str(e)}")
            raise

    @staticmethod
    def get_by_branch_id(branch_id: int) -> list:
        try:
            return BranchesSenders.query.filter_by(branch_id=branch_id).all()
        except Exception as e:
            logging.error(f"Error retrieving relations by branch_id {branch_id}: {str(e)}")
            raise

    @staticmethod
    def get_by_sender_id(sender_id: int) -> list:
        try:
            return BranchesSenders.query.filter_by(sender_id=sender_id).all()
        except Exception as e:
            logging.error(f"Error retrieving relations by sender_id {sender_id}: {str(e)}")
            raise

    @staticmethod
    def delete(branch_id: int, sender_id: int) -> bool:
        try:
            relation = BranchesSenders.query.filter_by(branch_id=branch_id, sender_id=sender_id).first()
            if relation:
                db.session.delete(relation)
                db.session.commit()
                return True
            return False
        except Exception as e:
            logging.error(f"Error deleting relation for branch_id {branch_id} and sender_id {sender_id}: {str(e)}")
            db.session.rollback()
            return False

    @staticmethod
    def delete_by_branch_id(branch_id: int) -> bool:
        try:
            relations = BranchesSenders.query.filter_by(branch_id=branch_id).all()
            if relations:
                for relation in relations:
                    db.session.delete(relation)
                db.session.commit()
                return True
            return False
        except Exception as e:
            logging.error(f"Error deleting relations for branch_id {branch_id}: {str(e)}")
            db.session.rollback()
            return False

    @staticmethod
    def get_all_with_relations() -> list:
        try:
            return db.session.query(BranchesSenders).join(Branches).join(Senders).all()
        except Exception as e:
            logging.error(f"Error retrieving all branch-sender relations: {str(e)}")
            raise