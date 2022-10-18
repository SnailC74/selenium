from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class LoginPage(BasePage):
   
    # 页面元素
    userId_loc = (By.NAME, "sid")
    password_loc = (By.NAME, "PIN")
    login_loc = (By.XPATH, "//input[@value='Login']")
    exit_loc = (By.LINK_TEXT, "EXIT")
    
    # 页面动作
    def login_service(self, userId = "*********", password = "********"):
        self.send_keys(LoginPage.userId_loc, userId)
        self.send_keys(LoginPage.password_loc, password)
        self.click(loginPage.login_loc)
    
    # 断言
    def get_except_result(self):
        return self.get_value(LoginPage.exit_loc)
