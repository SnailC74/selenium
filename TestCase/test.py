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
        
        # 查询课程
        scp = SearchClassPage()
        scp.search_class()
        
        # 注册/修改课程
        adcp = AddDeleteClassPage()
        sdcp.add_delete_class()
        
     def test_3_view_grade(self):
        """
        查看分数
        :return:
        """
        global driver
        # 打开浏览器
        driver = webdriver.chrome()
        driver.implicitly_wait(10)
        # 加载网页
        driver.get("https://https://www.uregina.ca/")
        # 进入当前学生界面
        driver.find.element(By.LINK_TEXT, "Current Students").click()
        # 进入自助服务界面
        driver.find.element(By.LINK_TEXT, "UR Self-Service").click()
        # 输入用户ID和密码
        driver.find.element(By.NAME, "sid").send_keys("*********")
        driver.find.element(By.NAME, "PIN").send_keys("********")
        # 点击登录
        driver.find.element(By.XPATH, "//input[@value='Login']").click()
        
        # 进入学生服务界面
        driver.find.element(By.LINK_TEXT, "Student").click()
        # 进入学生记录界面
        driver.find.element(By.LINK_TEXT, "Student Records").click()
        # 查看分数
        driver.find.element(By.LINK_TEXT, "Final Grades").click()
        # 选择查看的学期
        sel = select(driver.find.element(By.NAME, "term_in"))
        sel.select_by_value("202210")
        # 提交申请
        driver.find.element(By.XPATH, "//input[@value='Submit']").click()
        # 就可以查看到学期所有课程的分数
        
 if __name__ == '__main__':
     unittest.main()

