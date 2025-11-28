from base import db
from base.com.vo.category_vo import CategoryVO
from base.com.vo.subcategory_vo import SubCategoryVO
class ProductVO(db.Model):
    __tablename__ = 'product'
    product_id = db.Column("product_id", db.Integer, primary_key=True,
                           nullable=False, autoincrement=True)
    product_name = db.Column("product_name", db.String(255), nullable=
    False)
    product_description = db.Column("product_description", db.Text,
                                    nullable=False)
    product_price = db.Column("product_price", db.Integer, nullable=False)
    product_quantity = db.Column("product_quantity", db.Integer,nullable = False)
    product_image_name = db.Column("product_image_name", db.String(255),nullable = False)
    product_image_path = db.Column("product_image_path", db.String(255),
                                   nullable = False)
    product_category_id = db.Column("product_category_id", db.Integer
                                    , db.ForeignKey(
            'category.category_id', ondelete="CASCADE",
            onupdate="CASCADE"), nullable=False)
    product_subcategory_id = db.Column("product_subcategory_id", db.Integer
                                       , db.ForeignKey(
            'subcategory.subcategory_id', ondelete="CASCADE",
            onupdate="CASCADE"), nullable=False)

    category = db.relationship("CategoryVO", backref="products")
    subcategory = db.relationship("SubCategoryVO", backref="products")

    def as_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_price': self.product_price,
            'product_quantity': self.product_quantity,
            'product_image_name': self.product_image_name,
            'product_image_path': self.product_image_path,
            'product_category_id': self.product_category_id,
            'product_subcategory_id': self.product_subcategory_id,
            "category_name": self.category.category_name
            if self.category else None,

            "subcategory_name": self.subcategory.subcategory_name
            if self.subcategory else None,
        }

