from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class AddDeleteClassPage(BasePage):
      
    # 页面元素
    choice_loc = (By.XPATH, "//input[@value='10762 202310']")
    register_loc = (By.XPATH, "//input[@value='Register']")
    rsts_in_loc = (By.NAME, "RSTS_IN")
    submit_change_loc = (By.XPATH, "//input[@value='Submit Changes']")
    
    # 页面动作
    def add_delete_class(self):
        self.click(AddDeleteClassPage.choice_loc)
        self.click(AddDeleteClassPage.register_loc)
        self.select(AddDeleteClassPage.rsts_in_loc, "Drop Self-Serv 100% Ref No Grd")
        self.click(AddDeleteClassPage.submit_change_loc)
        
