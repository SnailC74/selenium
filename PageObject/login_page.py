from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class LoginPage(BasePage):
   
    # 页面元素
    userId_loc = (By.NAME, "sid")
    password_loc = (By.NAME, "PIN")
    login_loc = (By.XPATH, "//input[@value='Login']")
    
    # 页面动作
    def login_service(self):
        self.locator_element(loginPage.userId_loc)
        self.locator_element(loginPage.password_loc)
        self.locator_element(loginPage.login_loc)
