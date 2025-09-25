from flask import Blueprint
from auth.controllers.postmats_controller import (
    create_postmat_logic,
    get_postmats_logic,
    get_postmat_by_id_logic,
    update_postmat_logic,
    delete_postmat_logic,
)

postmats_blueprint = Blueprint('postmats', __name__)

@postmats_blueprint.route('/postmats', methods=['POST'])
def create_postmat():
    return create_postmat_logic()

@postmats_blueprint.route('/postmats', methods=['GET'])
def get_postmats():
    return get_postmats_logic()

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['GET'])
def get_postmat_by_id(postmat_id):
    return get_postmat_by_id_logic(postmat_id)

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['PUT'])
def update_postmat(postmat_id):
    return update_postmat_logic(postmat_id)

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['DELETE'])
def delete_postmat(postmat_id):
    return delete_postmat_logic(postmat_id)
