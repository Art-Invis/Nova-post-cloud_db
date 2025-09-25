from flask import request, jsonify
from app import app, db
from auth.service.packages_service import PackagesService  


@app.route('/packages', methods=['GET'])
def get_packages():
    try:
        packages = PackagesService.get_all_packages()
        result = [
            {
                "package_id": package.package_id,
                "description": package.description,
                "status": package.status
            } for package in packages
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/packages/<int:package_id>', methods=['GET'])
def get_package_by_id(package_id):
    try:
        package = PackagesService.get_package_by_id(package_id)
        result = {
            "package_id": package.package_id,
            "sender_id": package.sender_id,
            "receiver_id": package.receiver_id,
            "delivery_address_id": package.delivery_address_id,
            "description": package.description,
            "status": package.status
        }
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/packages', methods=['POST'])
def add_package():
    try:
        data = request.get_json()
        new_package = PackagesService.add_package(
            data['sender_id'],
            data['receiver_id'],
            data['delivery_address_id'],
            data['description'],
            data['status']
        )
        return jsonify({"message": "Package added successfully", "package_id": new_package.package_id}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    try:
        data = request.get_json()
        updated_package = PackagesService.update_package(
            package_id,
            data.get('description'),
            data.get('status')
        )
        return jsonify({"message": "Package updated successfully"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    try:
        PackagesService.delete_package(package_id)
        return jsonify({"message": "Package deleted successfully"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/packages/with_receivers', methods=['GET'])
def get_packages_with_receivers():
    try:
        packages_with_receivers = PackagesService.get_all_packages_with_receivers()
        return jsonify(packages_with_receivers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/packages/with_senders', methods=['GET'])
def get_packages_with_senders():
    try:
        packages_with_senders = PackagesService.get_all_packages_with_senders()
        return jsonify(packages_with_senders), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500