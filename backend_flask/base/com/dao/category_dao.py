
from base.com.vo.category_vo import CategoryVO, db

class CategoryDAO:
    def insert_category(self, vo):
        db.session.add(vo)
        db.session.commit()

    def view_category(self):
        category_vo_list = CategoryVO.query.all()
        return category_vo_list

    def edit_category(self, category_id):
        category_data = CategoryVO.query.filter_by(
            category_id=category_id).one()
        return category_data

    def update_category(self,category_vo):
        db.session.merge(category_vo)
        db.session.commit()

    def delete_category(self, category_vo):
        category_vo_list = CategoryVO.query.get(category_vo.category_id)
        db.session.delete(category_vo_list)
        db.session.commit()