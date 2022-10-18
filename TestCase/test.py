import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):
    def test_1_login(self):
        """
        登录
        :return:
        """
        # 进入当前学生界面
        up = UniversityPage()
        up.studentPage()
        # 进入自助服务界面
        sp = StudentPage()
        sp.servicePage()
        # 登录用户ID和密码
        lp = LoginPage()
        lp.login_service()
        
    def test_2_search_class(self):
        """
        查询课程
        :return
        """
        # 进入当前学生界面
        up = UniversityPage()
        up.studentPage()
        # 进入自助服务界面
        sp = StudentPage()
        sp.servicePage()
        # 登录用户ID和密码
        lp = LoginPage()
        lp.login_service()
        
        # 进入学生服务界面
        ssp = SelfServicePage()
        ssp.student_service()
        # 进入注册界面
        stsp = StudentServicePage()
        stsp.registration()
        # 查询课程
        scp = SearchClassPage()
        scp.search_class()
        
     def test_3_add_and_delete_class(self):
        """
        添加/删除课程
        :return:
        """
        # 进入当前学生界面
        up = UniversityPage()
        up.studentPage()
        # 进入自助服务界面
        sp = StudentPage()
        sp.servicePage()
        # 登录用户ID和密码
        lp = LoginPage()
        lp.login_service()
        
        # 进入学生服务界面
        ssp = SelfServicePage()
        ssp.student_service()
        # 进入注册界面
        stsp = StudentServicePage()
        stsp.registration()
        # 查询课程
        scp = SearchClassPage()
        scp.search_class()
        
        # 注册/修改课程
        adcp = AddDeleteClassPage()
        adcp.add_delete_class()
        
     def test_3_view_grade(self):
        """
        查看分数
        :return:
        """
        # 进入当前学生界面
        up = UniversityPage()
        up.studentPage()
        # 进入自助服务界面
        sp = StudentPage()
        sp.servicePage()
        # 登录用户ID和密码
        lp = LoginPage()
        lp.login_service()
        
        # 进入学生服务界面
        ssp = SelfServicePage()
        ssp.student_service()
        # 进入学生记录界面
        stsp = StudentServicePage()
        stsp.student_record()
        # 查看分数
        vgp = ViewGradePage()
        vgp.view_grade()
        
 if __name__ == '__main__':
     unittest.main()

