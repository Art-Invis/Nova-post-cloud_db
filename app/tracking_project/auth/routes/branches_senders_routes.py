from flask import Blueprint
from auth.controllers.branches_senders_controller import (
    get_branches_with_senders_logic,
    get_branches_and_senders_logic,
)

branches_senders_blueprint = Blueprint('branches_senders', __name__)

@branches_senders_blueprint.route('/branches_with_senders', methods=['GET'])
def get_branches_with_senders():
    return get_branches_with_senders_logic()

@branches_senders_blueprint.route('/branches_and_senders', methods=['GET'])
def get_branches_and_senders():
    return get_branches_and_senders_logic()
