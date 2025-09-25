from flask import request, jsonify
from app import app
from auth.service.branches_senders_service import BranchesSendersService

@app.route('/branches_with_senders', methods=['GET'])
def get_branches_with_senders():
    """
    Endpoint to fetch branches along with their associated senders.
    """
    try:
        relations = BranchesSendersService.get_all_branch_sender_relations()
        result = []

        # Dictionary to group branches
        branches_dict = {}
        
        for relation in relations:
            branch_id = relation.branch.branch_id
            if branch_id not in branches_dict:
                branches_dict[branch_id] = {
                    "branch_id": branch_id,
                    "branch_address": relation.branch.address,
                    "branch_ip": relation.branch.branch_ip,
                    "phone": relation.branch.phone,
                    "senders": []
                }
            branches_dict[branch_id]["senders"].append({
                "sender_id": relation.sender.sender_id,
                "full_name": relation.sender.full_name,
                "phone": relation.sender.phone,
                "email": relation.sender.email
            })
        
        # Convert dictionary to list
        result = list(branches_dict.values())
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/branches_and_senders', methods=['GET'])
def get_branches_and_senders():
    """
    Endpoint to fetch both branches and senders with their mutual relationships.
    """
    try:
        relations = BranchesSendersService.get_all_branch_sender_relations()
        branch_result = {}
        sender_result = {}

        for relation in relations:
            branch_id = relation.branch.branch_id
            sender_id = relation.sender.sender_id

            # Populate branches data
            if branch_id not in branch_result:
                branch_result[branch_id] = {
                    "branch_id": branch_id,
                    "branch_address": relation.branch.address,
                    "branch_ip": relation.branch.branch_ip,
                    "phone": relation.branch.phone,
                    "senders": []
                }
            branch_result[branch_id]["senders"].append({
                "sender_id": sender_id,
                "full_name": relation.sender.full_name,
                "phone": relation.sender.phone,
                "email": relation.sender.email
            })

            # Populate senders data
            if sender_id not in sender_result:
                sender_result[sender_id] = {
                    "sender_id": sender_id,
                    "full_name": relation.sender.full_name,
                    "phone": relation.sender.phone,
                    "email": relation.sender.email,
                    "branches": []
                }
            sender_result[sender_id]["branches"].append({
                "branch_id": branch_id,
                "branch_address": relation.branch.address,
                "branch_ip": relation.branch.branch_ip,
                "phone": relation.branch.phone
            })

        response = {
            "branches": [
                {
                    "branch_id": branch["branch_id"],
                    "branch_address": branch["branch_address"],
                    "branch_ip": branch["branch_ip"],
                    "phone": branch["phone"],
                    "senders": branch["senders"]
                }
                for branch in branch_result.values()
            ],
            "senders": [
                {
                    "sender_id": sender["sender_id"],
                    "full_name": sender["full_name"],
                    "phone": sender["phone"],
                    "email": sender["email"],
                    "branches": sender["branches"]
                }
                for sender in sender_result.values()
            ]
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500