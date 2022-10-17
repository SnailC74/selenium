from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class UniversityPage(BasePage):
    
    # 页面元素
    currentStudent_loc = (By.LINK_TEXT, "Current Students")
    
    # 页面动作
    def studentPage(self):
        self.click(UniversityPage.currentStudent_loc)
