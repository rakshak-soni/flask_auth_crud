
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.vo.category_vo import CategoryVO
from base import db

class SubCategoryDAO():
    def select_category(self):
        category_vo = CategoryVO()
        category_list = category_vo.query.all()
        return category_list

    def insert_subcategory(self, subcategory_vo):
        db.session.add(subcategory_vo)
        db.session.commit()

    def view_subcategory(self):
        subcategory_list = db.session.query(SubCategoryVO).join(CategoryVO,
            SubCategoryVO.subcategory_category_id ==
            CategoryVO.category_id).all()
        return subcategory_list

    def delete_subcategory(self, subcategory_id):
        subcategory = SubCategoryVO.query.get(subcategory_id)
        if subcategory:
            db.session.delete(subcategory)
            db.session.commit()
            return True
        return False

    def update_subcategory(self, subcategory_id, data):
        subcategory = SubCategoryVO.query.get(subcategory_id)
        if subcategory:
            subcategory.subcategory_name = data.get('subcategory_name',
                                                    subcategory.subcategory_name)
            subcategory.subcategory_description = data.get(
                'subcategory_description', subcategory.subcategory_description)
            subcategory.subcategory_category_id = data.get(
                'subcategory_category_id', subcategory.subcategory_category_id)
            db.session.commit()
            return True
        return False

    def get_subcategory_by_category(self, category_id):
        return SubCategoryVO.query.filter_by(
            subcategory_category_id=category_id).all()