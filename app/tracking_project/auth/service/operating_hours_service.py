from auth.dao.operating_hours_dao import OperatingHoursDAO

class OperatingHoursService:
    @staticmethod
    def create_operating_hours(day, open_time, close_time):
        # Додаткова бізнес-логіка перед створенням запису
        if not day or not open_time or not close_time:
            raise ValueError("Day, open time, and close time are required.")
        
        # Викликаємо DAO для створення запису
        return OperatingHoursDAO.create(day, open_time, close_time)

    @staticmethod
    def get_all_operating_hours():
        # Можливо, додаткова бізнес-логіка
        return OperatingHoursDAO.get_all()

    @staticmethod
    def update_operating_hours(hours_id, day, open_time, close_time):
        # Перевірка існування запису
        existing_hours = OperatingHoursDAO.get_by_id(hours_id)
        if not existing_hours:
            return None
        
        # Виклик DAO для оновлення
        return OperatingHoursDAO.update(hours_id, day, open_time, close_time)

    @staticmethod
    def delete_operating_hours(hours_id: int) -> bool:
        """Видалення робочих годин за ID."""
        return OperatingHoursDAO.delete(hours_id)
