from base.com.vo.role_vo import RoleVO

class RoleDAO:

    @staticmethod
    def get_role_by_name(role_name):
        return RoleVO.query.filter_by(role_name=role_name).first()