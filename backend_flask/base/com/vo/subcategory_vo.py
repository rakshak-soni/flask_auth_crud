from base import db

class SubCategoryVO(db.Model):
    __tablename__ = 'subcategory'
    subcategory_id = db.Column("subcategory_id",db.Integer,primary_key = True,
                            nullable = False,autoincrement = True)
    subcategory_name = db.Column("subcategory_name", db.String(255),
                                nullable=False)
    subcategory_description = db.Column("subcategory_description", db.Text,
                                     nullable=False)
    subcategory_category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

    category = db.relationship('CategoryVO', backref='subcategories')
    def as_dict(self):
        return {
            'subcategory_id' : self.subcategory_id,
            'subcategory_name' : self.subcategory_name,
            'subcategory_description' : self.subcategory_description,
            'subcategory_category_id': self.subcategory_category_id,
            "category_name": self.category.category_name if self.category else None
        }
