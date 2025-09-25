from auth.domain.couriers import Couriers
from auth.domain.models import db
import logging

class CouriersDAO:
    @staticmethod
    def create(name: str, phone: str, vehicle_type: str) -> Couriers:
        try:
            new_courier = Couriers(name=name, phone=phone, vehicle_type=vehicle_type)
            db.session.add(new_courier)
            db.session.commit()
            return new_courier
        except Exception as e:
            logging.error(f"Error creating courier: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    def get_all() -> list:
        return Couriers.query.all()

    @staticmethod
    def get_by_id(courier_id: int) -> Couriers:
        return Couriers.query.get(courier_id)

    @staticmethod
    def update(courier_id: int, name: str, phone: str, vehicle_type: str) -> Couriers:
        courier = Couriers.query.get(courier_id)
        if courier:
            courier.name = name
            courier.phone = phone
            courier.vehicle_type = vehicle_type
            db.session.commit()
            return courier
        return None

    @staticmethod
    def delete(courier_id: int) -> bool:
        try:
            courier = Couriers.query.get(courier_id)
            if courier:
                db.session.delete(courier)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error deleting courier: {str(e)}")
            return False
