from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class SelfServicePage(BasePage):
    
    # 页面元素
    studentService_loc = (By.LINK_TEXT, "Student")
    
    # 页面动作
    def student_service(self):
        self.click(SelfServicePage.studentService_loc)
