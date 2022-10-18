from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class StudentServicePage(BasePage):
    
    # 页面元素
    registration_loc = (By.LINK_TEXT, "Registration")
    
    # 页面动作
    def registrationPage(self):
        self.click(StudentServicePage.registration_loc)
