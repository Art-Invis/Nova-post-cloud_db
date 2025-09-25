from auth.dao.branches_dao import BranchesDAO
from auth.dao.branches_senders_dao import BranchesSendersDAO  # Імпортуємо DAO для branches_senders

class BranchesService:
    @staticmethod
    def create_branch(branch_ip, address, hours_id, phone):
        # Додаткова логіка валідації даних
        if not branch_ip or not address or not hours_id or not phone:
            raise ValueError("All fields are required.")
        
        # Виклик DAO для створення запису
        return BranchesDAO.create(branch_ip, address, hours_id, phone)

    @staticmethod
    def get_all_branches():
        # Виклик DAO для отримання всіх записів
        return BranchesDAO.get_all()

    @staticmethod
    def get_branch_by_id(branch_id):
        # Виклик DAO для отримання запису за ID
        return BranchesDAO.get_by_id(branch_id)

    @staticmethod
    def update_branch(branch_id, branch_ip, address, hours_id, phone):
        # Перевірка існування запису
        existing_branch = BranchesDAO.get_by_id(branch_id)
        if not existing_branch:
            return None
        
        # Оновлення запису через DAO
        return BranchesDAO.update(branch_id, branch_ip, address, hours_id, phone)

    @staticmethod
    def delete_branch(branch_id):
        # Перевірка існування запису перед видаленням
        existing_branch = BranchesDAO.get_by_id(branch_id)
        if not existing_branch:
            return None
        
        # Видалення запису через DAO
        return BranchesDAO.delete(branch_id)

    @staticmethod
    def delete_related_senders(branch_id):
        # Виклик DAO для видалення всіх записів з таблиці branches_senders, які залежать від branch_id
        related_senders = BranchesSendersDAO.get_by_branch_id(branch_id)
        for sender in related_senders:
            BranchesSendersDAO.delete(sender.sender_id)
        return True
