from auth.dao.delivery_address_dao import DeliveryAddressDAO

class DeliveryAddressService:

    @staticmethod
    def get_all_addresses():
        return DeliveryAddressDAO.get_all_addresses()

    @staticmethod
    def get_address_by_id(address_id):
        return DeliveryAddressDAO.get_address_by_id(address_id)

    @staticmethod
    def create_address(address, delivery_instructions):
        return DeliveryAddressDAO.create_address(address, delivery_instructions)

    @staticmethod
    def update_address(address_id, address, delivery_instructions):
        return DeliveryAddressDAO.update_address(address_id, address, delivery_instructions)

    @staticmethod
    def delete_address(address_id):
        return DeliveryAddressDAO.delete_address(address_id)
