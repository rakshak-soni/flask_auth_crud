import os
from flask import request, jsonify, send_from_directory
from base import app
from base.com.dao.product_dao import ProductDAO
from base.com.middleware.auth_middleware import token_required
from base.com.vo.product_vo import ProductVO
import traceback

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'product_images')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def internal_error(e):
    print("UNEXPECTED ERROR:", str(e))
    print(traceback.format_exc())
    return jsonify({"error": "Internal server error"}), 500


@app.route('/product', methods=['POST'])
@token_required(required_roles=['admin'])
def add_product():
    try:
        data = request.form
        if not data:
            return jsonify({"error": "Invalid or empty form data"}), 400

        product_image = request.files.get('product_image')

        image_name = None
        image_path = None

        # handle image upload
        if product_image:
            try:
                image_name = product_image.filename
                image_path = os.path.join('product_images', image_name)
                product_image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
            except Exception as img_err:
                print("IMAGE SAVE ERROR:", str(img_err))
                return jsonify({"error": "Failed to save image"}), 500

        vo = ProductVO()
        vo.product_name = data.get('product_name')
        vo.product_description = data.get('product_description')
        vo.product_price = data.get('product_price')
        vo.product_quantity = data.get('product_quantity')
        vo.product_category_id = data.get('product_category_id')
        vo.product_subcategory_id = data.get('product_subcategory_id')
        vo.product_image_name = image_name
        vo.product_image_path = image_path

        try:
            dao = ProductDAO()
            dao.insert_product(vo)
        except Exception as db_err:
            print("DATABASE ERROR insert_product:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        return jsonify({"message": "Product inserted successfully"}), 201

    except Exception as e:
        return internal_error(e)



@app.route('/product', methods=['GET'])
@token_required(required_roles=['admin'])
def view_products():
    try:
        dao = ProductDAO()

        try:
            data = dao.view_product()
        except Exception as db_err:
            print("DATABASE ERROR view_product:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        return jsonify([row.as_dict() for row in data]), 200

    except Exception as e:
        return internal_error(e)



@app.route('/product/<int:product_id>', methods=['GET'])
@token_required(required_roles=['admin'])
def view_product_by_id(product_id):
    try:
        dao = ProductDAO()

        try:
            row = dao.view_product_by_id(product_id)
        except Exception as db_err:
            print("DATABASE ERROR view_product_by_id:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        if not row:
            return jsonify({"error": "Product not found"}), 404

        return jsonify(row.as_dict()), 200

    except Exception as e:
        return internal_error(e)



@app.route('/product/<int:product_id>', methods=['PUT'])
@token_required(required_roles=['admin'])
def update_product(product_id):
    try:
        data = request.form
        if not data:
            return jsonify({"error": "Invalid or empty form data"}), 400

        dao = ProductDAO()

        try:
            existing = dao.view_product_by_id(product_id)
        except Exception as db_err:
            print("DATABASE ERROR view_product_by_id:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        if not existing:
            return jsonify({"error": "Product not found"}), 404

        product_image = request.files.get('product_image')

        image_name = existing.product_image_name
        image_path = existing.product_image_path

        # new image upload handling
        if product_image:
            try:
                image_name = product_image.filename
                image_path = os.path.join('product_images', image_name)
                product_image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
            except Exception as img_err:
                print("IMAGE SAVE ERROR:", str(img_err))
                return jsonify({"error": "Failed to save image"}), 500

        vo = ProductVO()
        vo.product_id = product_id
        vo.product_name = data.get("product_name")
        vo.product_description = data.get("product_description")
        vo.product_price = data.get("product_price")
        vo.product_quantity = data.get("product_quantity")
        vo.product_category_id = data.get("product_category_id")
        vo.product_subcategory_id = data.get("product_subcategory_id")
        vo.product_image_name = image_name
        vo.product_image_path = image_path

        try:
            dao.update_product(vo)
        except Exception as db_err:
            print("DATABASE ERROR update_product:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        return jsonify({"message": "Product updated successfully"}), 200

    except Exception as e:
        return internal_error(e)



@app.route('/product/<int:product_id>', methods=['DELETE'])
@token_required(required_roles=['admin'])
def delete_product(product_id):
    try:
        dao = ProductDAO()

        try:
            product = dao.view_product_by_id(product_id)
        except Exception as db_err:
            print("DATABASE ERROR view_product_by_id:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        if not product:
            return jsonify({"error": "Product not found"}), 404

        try:
            dao.delete_product(product)
        except Exception as db_err:
            print("DATABASE ERROR delete_product:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        return jsonify({"message": "Product deleted successfully"}), 200

    except Exception as e:
        return internal_error(e)



@app.route('/product_image/<filename>')
def product_image(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        print("IMAGE FETCH ERROR:", str(e))
        return jsonify({"error": "Unable to load image"}), 500



@app.route("/view_subcategory_by_category/<int:category_id>", methods=["GET"])
@token_required(required_roles=['admin'])
def view_subcategory_by_category(category_id):
    try:
        from base.com.dao.subcategory_dao import SubCategoryDAO
        subcategory_dao = SubCategoryDAO()

        try:
            data = subcategory_dao.get_subcategory_by_category(category_id)
        except Exception as db_err:
            print("DATABASE ERROR get_subcategory_by_category:", str(db_err))
            return jsonify({"error": "Database error"}), 500

        return jsonify([sub.as_dict() for sub in data]), 200

    except Exception as e:
        return internal_error(e)
