from base import db
from base.com.vo.product_vo import ProductVO

class ProductDAO:

    def insert_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def view_product(self):
        return ProductVO.query.all()

    def view_product_by_id(self, product_id):
        return ProductVO.query.filter_by(product_id=product_id).first()

    def update_product(self, product_vo):
        db.session.merge(product_vo)
        db.session.commit()

    def delete_product(self, product_vo):
        prod = ProductVO.query.get(product_vo.product_id)
        db.session.delete(prod)
        db.session.commit()
