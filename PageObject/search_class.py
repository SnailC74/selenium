from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class SearchClassPage(BasePage):
      
    # 页面元素
    studentService_loc = (By.LINK_TEXT, "Student")
    registration_loc = (By.LINK_TEXT, "Registration")
    searchClass_loc = (By.LINK_TEXT, "Search for Classes")
    
    # 页面动作
    def search_class(self):
        self.click(SearchClassPage.studentService_loc)
        self.click(SearchClassPage.registration_loc)
        self.click(SearchClassPage.searchClass_loc)
