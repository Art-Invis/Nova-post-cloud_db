from auth.dao.branches_senders_dao import BranchesSendersDAO

class BranchesSendersService:
    @staticmethod
    def create_relation(branch_id: int, sender_id: int):
        """Створити зв'язок між філією та відправником."""
        return BranchesSendersDAO.create(branch_id, sender_id)

    @staticmethod
    def get_senders_by_branch_id(branch_id: int):
        """Отримати всіх відправників для конкретної філії."""
        return BranchesSendersDAO.get_by_branch_id(branch_id)

    @staticmethod
    def get_branches_by_sender_id(sender_id: int):
        """Отримати всі філії для конкретного відправника."""
        return BranchesSendersDAO.get_by_sender_id(sender_id)

    @staticmethod
    def delete_relation(branch_id: int, sender_id: int) -> bool:
        """Видалити зв'язок між філією та відправником."""
        return BranchesSendersDAO.delete(branch_id, sender_id)

    @staticmethod
    def delete_relations_by_branch_id(branch_id: int) -> bool:
        """Видалити всі зв'язки для конкретної філії."""
        return BranchesSendersDAO.delete_by_branch_id(branch_id)

    @staticmethod
    def get_all_branch_sender_relations():
        """Отримати всі зв'язки між філіями та відправниками з інформацією про обидва."""
        return BranchesSendersDAO.get_all_with_relations()
