from auth.dao.postmats_dao import PostmatsDAO

class PostmatsService:
    @staticmethod
    def create_postmat(location, status, branch_id):
        # Валидация данных
        if not location or not status or not branch_id:
            raise ValueError("Location, status, and branch_id are required.")
        
        # Создание нового поштомата через DAO
        return PostmatsDAO.create(location, status, branch_id)

    @staticmethod
    def get_all_postmats():
        return PostmatsDAO.get_all()

    @staticmethod
    def get_postmat_by_id(postmat_id):
        return PostmatsDAO.get_by_id(postmat_id)

    @staticmethod
    def update_postmat(postmat_id, location, status, branch_id):
        # Проверка существования поштомата
        existing_postmat = PostmatsDAO.get_by_id(postmat_id)
        if not existing_postmat:
            return None
        
        # Обновление поштомата
        return PostmatsDAO.update(postmat_id, location, status, branch_id)

    @staticmethod
    def delete_postmat(postmat_id: int) -> bool:
        """Удаление поштомата по ID."""
        return PostmatsDAO.delete(postmat_id)
