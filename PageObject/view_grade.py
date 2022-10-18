from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class ViewGradePage(BasePage):
      
    # 页面元素
    finalGrade_loc = (By.LINK_TEXT, "Final Grades")
    select_term_loc = (By.NAME, "term_in")
    submit_loc = (By.XPATH, "//input[@value='Submit']")
    
    # 页面动作
    def view_grade(self):
        self.click(ViewGradePage.finalGrade_loc)
        self.select(ViewGradePage.select_term_loc, "202210")
        self.click(ViewGradePage.submit_loc)
        
