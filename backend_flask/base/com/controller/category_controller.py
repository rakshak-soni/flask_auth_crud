from flask import request, jsonify
from base.com.vo.category_vo import CategoryVO
from base.com.dao.category_dao import CategoryDAO
from base.com.middleware.auth_middleware import token_required
from base import app
import traceback


def handle_unexpected_error(e):
    print("UNEXPECTED ERROR:", str(e))
    print(traceback.format_exc())
    return jsonify({"error": "Internal server error"}), 500


@app.route('/insert_category', methods=['POST'])
@token_required(required_roles=['admin'])
def insert_category():
    try:
        data = request.get_json()

        if data is None:
            return jsonify({"error": "Invalid JSON format"}), 400

        category_name = data.get('category_name')
        category_description = data.get('category_description')

        if not category_name or not category_description:
            return jsonify({"error": "All fields required"}), 400

        try:
            category_vo = CategoryVO()
            category_vo.category_name = category_name
            category_vo.category_description = category_description

            category_dao = CategoryDAO()
            category_dao.insert_category(category_vo)
        except Exception as db_error:
            print("Database Error in insert_category:", str(db_error))
            return jsonify({"error": "Database error"}), 500

        return jsonify({"message": "Category added successfully"}), 201

    except Exception as e:
        return handle_unexpected_error(e)



@app.route('/view_category', methods=['GET'])
def view_category():
    try:
        dao = CategoryDAO()

        try:
            category_list = dao.view_category()
        except Exception as db_error:
            print("Database Error in view_category:", str(db_error))
            return jsonify({"error": "Database error"}), 500

        return jsonify([i.as_dict() for i in category_list]), 200

    except Exception as e:
        return handle_unexpected_error(e)



@app.route('/edit_category/<int:category_id>', methods=['GET'])
@token_required(required_roles=['admin'])
def edit_category(category_id):
    try:
        dao = CategoryDAO()

        try:
            category = dao.edit_category(category_id)
        except Exception as db_error:
            print("Database Error in edit_category:", str(db_error))
            return jsonify({"error": "Database error"}), 500

        if not category:
            return jsonify({"error": "Category not found"}), 404

        return jsonify(category.as_dict()), 200

    except Exception as e:
        return handle_unexpected_error(e)



@app.route('/update_category', methods=['PUT'])
@token_required(required_roles=['admin'])
def update_category():
    try:
        data = request.get_json()

        if data is None:
            return jsonify({"error": "Invalid JSON format"}), 400

        required_fields = ['category_id', 'category_name', 'category_description']
        if any(data.get(f) is None for f in required_fields):
            return jsonify({"error": "All fields required"}), 400

        vo = CategoryVO()
        vo.category_id = data.get('category_id')
        vo.category_name = data.get('category_name')
        vo.category_description = data.get('category_description')

        dao = CategoryDAO()

        try:
            dao.update_category(vo)
        except Exception as db_error:
            print("Database Error in update_category:", str(db_error))
            return jsonify({"error": "Database error"}), 500

        return jsonify({"message": "Category updated successfully"}), 200

    except Exception as e:
        return handle_unexpected_error(e)



@app.route('/delete_category/<int:category_id>', methods=['DELETE'])
@token_required(required_roles=['admin'])
def delete_category(category_id):
    try:
        vo = CategoryVO()
        vo.category_id = category_id

        dao = CategoryDAO()

        try:
            dao.delete_category(vo)
        except Exception as db_error:
            print("Database Error in delete_category:", str(db_error))
            return jsonify({"error": "Database error"}), 500

        return jsonify({"message": "Category deleted successfully"}), 200

    except Exception as e:
        return handle_unexpected_error(e)
