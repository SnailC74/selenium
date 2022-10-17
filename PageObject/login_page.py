from base.base import BasePage

class LoginPage(BasePage):
   
    # 页面元素
    userId_loc = (By.NAME, "sid")
    password_loc = (By.NAME, "PIN")
    login_loc = (By.XPATH, "//input[@value='Login']")
    
    # 页面动作
    def login_ecshop(self):
        self.locator_element(loginPage.userId_loc)
        self.locator_element(loginPage.password_loc)
        self.locator_element(loginPage.login_loc)
