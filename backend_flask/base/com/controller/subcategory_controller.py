from flask import Flask, request, jsonify
from base.com.middleware.auth_middleware import token_required
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.dao.category_dao import CategoryDAO
from base import app
import traceback


# Get all categories (for dropdowns)
@app.route('/categories', methods=['GET'])
@token_required(required_roles=['admin'])
def get_categories():
    try:
        category_dao = CategoryDAO()
        categories = category_dao.view_category()
        return jsonify([cat.as_dict() for cat in categories]), 200
    except Exception as e:
        print("ERROR in get_categories:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal server error"}), 500


# Add new subcategory
@app.route('/subcategories', methods=['POST'])
@token_required(required_roles=['admin'])
def add_subcategory():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()

        # Basic validation
        required = ["subcategory_name", "subcategory_description", "subcategory_category_id"]
        if not all(key in data for key in required):
            return jsonify({"error": "Missing required fields"}), 400

        subcategory_vo = SubCategoryVO()
        subcategory_vo.subcategory_name = data["subcategory_name"]
        subcategory_vo.subcategory_description = data["subcategory_description"]
        subcategory_vo.subcategory_category_id = data["subcategory_category_id"]

        dao = SubCategoryDAO()
        dao.insert_subcategory(subcategory_vo)

        return jsonify({"message": "Subcategory added successfully"}), 201

    except Exception as e:
        print("ERROR in add_subcategory:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal server error"}), 500


# Get all subcategories
@app.route('/subcategories', methods=['GET'])
@token_required(required_roles=['admin'])
def get_subcategories():
    try:
        dao = SubCategoryDAO()
        subcategories = dao.view_subcategory()
        return jsonify([sc.as_dict() for sc in subcategories]), 200
    except Exception as e:
        print("ERROR in get_subcategories:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal server error"}), 500


# Update a subcategory
@app.route('/subcategories/<int:subcategory_id>', methods=['PUT'])
@token_required(required_roles=['admin'])
def update_subcategory(subcategory_id):
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()
        dao = SubCategoryDAO()

        try:
            success = dao.update_subcategory(subcategory_id, data)
        except Exception as e:
            print("DAO update error:", str(e))
            return jsonify({"error": "Update failed"}), 500

        return jsonify({"message": "Updated successfully" if success else "Not found"}), 200

    except Exception as e:
        print("ERROR in update_subcategory:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal server error"}), 500


# Delete a subcategory
@app.route('/subcategories/<int:subcategory_id>', methods=['DELETE'])
@token_required(required_roles=['admin'])
def delete_subcategory(subcategory_id):
    try:
        dao = SubCategoryDAO()

        try:
            success = dao.delete_subcategory(subcategory_id)
        except Exception as e:
            print("DAO delete error:", str(e))
            return jsonify({"error": "Delete failed"}), 500

        return jsonify({"message": "Deleted successfully" if success else "Not found"}), 200

    except Exception as e:
        print("ERROR in delete_subcategory:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal server error"}), 500
