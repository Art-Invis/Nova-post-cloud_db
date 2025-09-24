from flask import Blueprint
from auth.controllers.delivery_address_controller import (
    create_address_logic,
    get_addresses_logic,
    get_address_by_id_logic,
    update_address_logic,
    delete_address_logic,
)

delivery_address_blueprint = Blueprint('delivery_addresses', __name__)

@delivery_address_blueprint.route('/addresses', methods=['POST'])
def create_address():
    return create_address_logic()

@delivery_address_blueprint.route('/addresses', methods=['GET'])
def get_addresses():
    return get_addresses_logic()

@delivery_address_blueprint.route('/addresses/<int:address_id>', methods=['GET'])
def get_address_by_id(address_id):
    return get_address_by_id_logic(address_id)

@delivery_address_blueprint.route('/addresses/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    return update_address_logic(address_id)

@delivery_address_blueprint.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    return delete_address_logic(address_id)
