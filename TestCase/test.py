import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# ID定位
//driver.find.element(By.ID, "kw").send_keys("University of Regina")
# Name定位
//driver.find.element(By.NAME, "wd").send_keys("University of Regina")
# Link_text定位
//driver.find.element(By.LINK_TEXT, "地图").click()
# Partial_link定位
//driver.find.element(By.PARTIAL_LINK, "图").click()

class TestCase(unittest.TestCase):
    def test_1_login(self):
        """
        登录
        :return:
        """
        global driver
        # 打开浏览器
        driver = webdriver.chrome()
        # 加载网页
        driver.get("https://https://www.uregina.ca/")
        # 选择当前学生界面
        driver.find.element(By.LINK_TEXT, "Current Students").click()
        # 选择自助服务界面
        driver.find.element(By.LINK_TEXT, "UR Self-Service").click()
        # 输入用户ID和密码
        driver.find.element(By.NAME, "sid").send_keys("*********")
        driver.find.element(By.NAME, "PIN").send_keys("********")
        # 点击登录
        driver.find.element(By.XPATH, "//input[@value='Login']").click()
        
    def test_2_search_class(self):
        """
        查询课程
        :return
        """
        global driver
        # 打开浏览器
        driver = webdriver.chrome()
        driver.implicitly_wait(10)
        # 加载网页
        driver.get("https://https://www.uregina.ca/")
        # 选择当前学生界面
        driver.find.element(By.LINK_TEXT, "Current Students").click()
        # 选择自助服务界面
        driver.find.element(By.LINK_TEXT, "UR Self-Service").click()
        # 输入用户ID和密码
        driver.find.element(By.NAME, "sid").send_keys("*********")
        driver.find.element(By.NAME, "PIN").send_keys("********")
        # 点击登录
        driver.find.element(By.XPATH, "//input[@value='Login']").click()
        
        # 进入学生界面
        driver.find.element(By.LINK_TEXT, "Student").click()
        # 进入注册界面
        driver.find.element(By.LINK_TEXT, "Registration").click()
        # 查询课程
        driver.find.element(By.LINK_TEXT, "Search for Classes").click()
        # 选择查看的学期
        sel = select(driver.find.element(By.NAME, "p_term"))
        sel.select_by_value("202310")
        # sel.select_by_visible_text("2023 Winter")
        # sel.select_by_index("1")
        # 搜索
        driver.find.element(By.XPATH, "//input[@value='Submit']").click()
        # 选择查看的课程分类
        sel = select(driver.find.element(By.NAME, "sel_subj"))
        sel.select_by_value("CS")
        # sel.select_by_visible_text("Computer Science")
        # sel.select_by_index("17")
        # 搜索
        driver.find.element(By.XPATH, "//input[@value='Course Search']").click()
        # 选择查看的课程
        driver.find.element(By.NAME, "SUB_BTN").click()
        
     def test_3_add_and_delete_class(self):
        """
        添加/删除课程
        :return:
        """
        global driver
        # 打开浏览器
        driver = webdriver.chrome()
        driver.implicitly_wait(10)
        # 加载网页
        driver.get("https://https://www.uregina.ca/")
        # 选择当前学生界面
        driver.find.element(By.LINK_TEXT, "Current Students").click()
        # 选择自助服务界面
        driver.find.element(By.LINK_TEXT, "UR Self-Service").click()
        # 输入用户ID和密码
        driver.find.element(By.NAME, "sid").send_keys("*********")
        driver.find.element(By.NAME, "PIN").send_keys("********")
        # 点击登录
        driver.find.element(By.XPATH, "//input[@value='Login']").click()
        
        # 进入学生界面
        driver.find.element(By.LINK_TEXT, "Student").click()
        # 进入注册界面
        driver.find.element(By.LINK_TEXT, "Registration").click()
        # 查询课程
        driver.find.element(By.LINK_TEXT, "Search for Classes").click()
        # 选择查看的学期
        sel = select(driver.find.element(By.NAME, "p_term"))
        sel.select_by_value("202310")
        # sel.select_by_visible_text("2023 Winter")
        # sel.select_by_index("1")
        # 搜索
        driver.find.element(By.XPATH, "//input[@value='Submit']").click()
        # 选择查看的课程分类
        sel = select(driver.find.element(By.NAME, "sel_subj"))
        sel.select_by_value("CS")
        # sel.select_by_visible_text("Computer Science")
        # sel.select_by_index("17")
        # 搜索
        driver.find.element(By.XPATH, "//input[@value='Course Search']").click()
        # 选择查看的课程
        driver.find.element(By.NAME, "SUB_BTN").click()
        
        # 注册课程
        driver.find.element(By.XPATH, "//input[@value='10762 202310']").click()
        driver.find.element(By.XPATH, "//input[@value='Register']").click()
        # 课程就成功注册，显示在课程列表中
        # 删除课程
        # 在课程列表中的action修改属性为drop
        sel = select(driver.find.element(By.NAME, "RSTS_IN"))
        sel.select_by_value("Drop Self-Serv 100% Ref No Grd")
        # 提交修改
        driver.find.element(By.XPATH, "//input[@value='Submit Changes']").click()
        
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
        # Link_text定位
        driver.find.element(By.LINK_TEXT, "Current Students").click()
        # Link_text定位
        driver.find.element(By.LINK_TEXT, "UR Self-Service").click()
        # 输入用户ID和密码
        driver.find.element(By.NAME, "sid").send_keys("*********")
        driver.find.element(By.NAME, "PIN").send_keys("********")
        # 点击登录
        driver.find.element(By.XPATH, "//input[@value='Login']").click()
        
        # 进入学生界面
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

