from flask import Blueprint, request, jsonify
from app import app
from auth.service.postmats_service import PostmatsService

postmats_blueprint = Blueprint('postmats', __name__)


@postmats_blueprint.route('/postmats', methods=['POST'])
def create_postmat():
    try:
        data = request.get_json()
   
        if not data.get('location') or not data.get('status') or not data.get('branch_id'):
            return jsonify({"error": "Location, status, and branch_id are required"}), 400
        
        new_postmat = PostmatsService.create_postmat(
            data['location'], data['status'], data['branch_id']
        )
        return jsonify({"message": "Postmat created successfully", "postmat_id": new_postmat.postmat_id}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@postmats_blueprint.route('/postmats', methods=['GET'])
def get_postmats():
    try:
        postmats = PostmatsService.get_all_postmats()
        result = [{"postmat_id": postmat.postmat_id, "location": postmat.location, "status": postmat.status, "branch_id": postmat.branch_id} for postmat in postmats]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['GET'])
def get_postmat_by_id(postmat_id):
    try:
        postmat = PostmatsService.get_postmat_by_id(postmat_id)
        if postmat:
            result = {
                "postmat_id": postmat.postmat_id,
                "location": postmat.location,
                "status": postmat.status,
                "branch_id": postmat.branch_id
            }
            return jsonify(result), 200
        else:
            return jsonify({"error": "Postmat not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['PUT'])
def update_postmat(postmat_id):
    try:
        data = request.get_json()
      
        if not data.get('location') or not data.get('status') or not data.get('branch_id'):
            return jsonify({"error": "Location, status, and branch_id are required"}), 400
        
        updated_postmat = PostmatsService.update_postmat(
            postmat_id, data['location'], data['status'], data['branch_id']
        )
        if updated_postmat:
            return jsonify({"message": "Postmat updated successfully"}), 200
        else:
            return jsonify({"error": "Postmat not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['DELETE'])
def delete_postmat(postmat_id):
    try:
        success = PostmatsService.delete_postmat(postmat_id)
        if success:
            return jsonify({"message": "Postmat deleted successfully"}), 200
        else:
            return jsonify({"error": "Postmat not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Error deleting postmat: {str(e)}"}), 500

app.register_blueprint(postmats_blueprint)