from flask import Blueprint
from auth.controllers.operating_hours_controller import (
    create_operating_hours_logic,
    get_operating_hours_logic,
    update_operating_hours_logic,
    delete_operating_hours_logic,
)

operating_hours_blueprint = Blueprint('operating_hours', __name__)

@operating_hours_blueprint.route('/operating_hours', methods=['POST'])
def create_operating_hours():
    return create_operating_hours_logic()

@operating_hours_blueprint.route('/operating_hours', methods=['GET'])
def get_operating_hours():
    return get_operating_hours_logic()

@operating_hours_blueprint.route('/operating_hours/<int:hours_id>', methods=['PUT'])
def update_operating_hours(hours_id):
    return update_operating_hours_logic(hours_id)

@operating_hours_blueprint.route('/operating_hours/<int:hours_id>', methods=['DELETE'])
def delete_operating_hours(hours_id):
    return delete_operating_hours_logic(hours_id)
