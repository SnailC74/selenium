from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class StudentPage(BasePage):
    
    # 页面元素
    self_service_loc = (By.LINK_TEXT, "UR Self-Service")
    
    # 页面动作
    def servicePage(self):
        self.click(StudentPage.self_service_loc)
