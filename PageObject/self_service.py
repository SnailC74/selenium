from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class SelfServicePage(BasePage):
    
    # 页面元素
    student_service_loc = (By.LINK_TEXT, "Student")
    
    # 页面动作
    def student_servicePage(self):
        self.click(SelfServicePage.student_service_loc)
