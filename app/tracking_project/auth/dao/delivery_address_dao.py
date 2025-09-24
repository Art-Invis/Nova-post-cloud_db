from auth.domain.models import db
from auth.domain.delivery_address import DeliveryAddress
class DeliveryAddressDAO:

    @staticmethod
    def get_all_addresses():
        return DeliveryAddress.query.all()

    @staticmethod
    def get_address_by_id(address_id):
        return DeliveryAddress.query.get(address_id)

    @staticmethod
    def create_address(address, delivery_instructions):
        new_address = DeliveryAddress(address=address, delivery_instructions=delivery_instructions)
        db.session.add(new_address)
        db.session.commit()
        return new_address

    @staticmethod
    def update_address(address_id, address, delivery_instructions):
        existing_address = DeliveryAddress.query.get(address_id)
        if existing_address:
            existing_address.address = address
            existing_address.delivery_instructions = delivery_instructions
            db.session.commit()
        return existing_address

    @staticmethod
    def delete_address(address_id):
        address = DeliveryAddress.query.get(address_id)
        if address:
            db.session.delete(address)
            db.session.commit()
        return address