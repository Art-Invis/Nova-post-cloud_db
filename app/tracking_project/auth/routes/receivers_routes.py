from flask import Blueprint
from auth.controllers.receivers_controller import (
    create_receiver_logic,
    get_receivers_logic,
    get_receiver_by_id_logic,
    update_receiver_logic,
    delete_receiver_logic,
    get_receivers_with_packages_logic,
)

receivers_blueprint = Blueprint('receivers', __name__)

@receivers_blueprint.route('/receivers', methods=['POST'])
def create_receiver():
    return create_receiver_logic()

@receivers_blueprint.route('/receivers', methods=['GET'])
def get_receivers():
    return get_receivers_logic()

@receivers_blueprint.route('/receivers/<int:receiver_id>', methods=['GET'])
def get_receiver_by_id(receiver_id):
    return get_receiver_by_id_logic(receiver_id)

@receivers_blueprint.route('/receivers/<int:receiver_id>', methods=['PUT'])
def update_receiver(receiver_id):
    return update_receiver_logic(receiver_id)

@receivers_blueprint.route('/receivers/<int:receiver_id>', methods=['DELETE'])
def delete_receiver(receiver_id):
    return delete_receiver_logic(receiver_id)

@receivers_blueprint.route('/receivers/with_packages', methods=['GET'])
def get_receivers_with_packages():
    return get_receivers_with_packages_logic()
