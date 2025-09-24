from auth.dao.couriers_dao import CouriersDAO

class CouriersService:
    @staticmethod
    def create_courier(name: str, phone: str, vehicle_type: str):
        if not name or not phone or not vehicle_type:
            raise ValueError("Name, phone, and vehicle type are required.")
        return CouriersDAO.create(name, phone, vehicle_type)

    @staticmethod
    def get_all_couriers() -> list:
        return CouriersDAO.get_all()

    @staticmethod
    def get_courier_by_id(courier_id: int):
        courier = CouriersDAO.get_by_id(courier_id)
        if not courier:
            raise ValueError("Courier not found.")
        return courier

    @staticmethod
    def update_courier(courier_id: int, name: str, phone: str, vehicle_type: str):
        return CouriersDAO.update(courier_id, name, phone, vehicle_type)

    @staticmethod
    def delete_courier(courier_id: int) -> bool:
        return CouriersDAO.delete(courier_id)
