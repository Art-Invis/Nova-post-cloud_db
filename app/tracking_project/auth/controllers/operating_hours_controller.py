from flask import Blueprint, request, jsonify
from app import app
from auth.service.operating_hours_service import OperatingHoursService
from datetime import datetime

operating_hours_blueprint = Blueprint('operating_hours', __name__)

# Функція для валідації часу
def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, '%H:%M:%S')  
        return True
    except ValueError:
        return False

@operating_hours_blueprint.route('/operating_hours', methods=['POST'])
def create_operating_hours():
    try:
        data = request.get_json()
        if not validate_time_format(data['open_time']) or not validate_time_format(data['close_time']):
            return jsonify({"error": "Invalid time format. Expected format: HH:MM:SS"}), 400
        new_hours = OperatingHoursService.create_operating_hours(
            data['day'], data['open_time'], data['close_time']
        )
        return jsonify({"message": "Operating hours created successfully", "hours_id": new_hours.hours_id}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@operating_hours_blueprint.route('/operating_hours', methods=['GET'])
def get_operating_hours():
    try:
        hours = OperatingHoursService.get_all_operating_hours()
        result = [{"hours_id": hour.hours_id, "day": hour.day, "open_time": str(hour.open_time), "close_time": str(hour.close_time)} for hour in hours]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@operating_hours_blueprint.route('/operating_hours/<int:hours_id>', methods=['PUT'])
def update_operating_hours(hours_id):
    try:
        data = request.get_json()
        if not validate_time_format(data['open_time']) or not validate_time_format(data['close_time']):
            return jsonify({"error": "Invalid time format. Expected format: HH:MM:SS"}), 400
        updated_hours = OperatingHoursService.update_operating_hours(
            hours_id, data['day'], data['open_time'], data['close_time']
        )
        if updated_hours:
            return jsonify({"message": "Operating hours updated successfully"}), 200
        else:
            return jsonify({"error": "Operating hours not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@operating_hours_blueprint.route('/operating_hours/<int:hours_id>', methods=['DELETE'])
def delete_operating_hours(hours_id):
    try:
        success = OperatingHoursService.delete_operating_hours(hours_id)
        if success:
            return jsonify({"message": "Operating hours deleted successfully"}), 200
        else:
            return jsonify({"error": "Operating hours not found or in use"}), 404
    except Exception as e:
        return jsonify({"error": f"Error deleting operating hours: {str(e)}"}), 500


app.register_blueprint(operating_hours_blueprint)