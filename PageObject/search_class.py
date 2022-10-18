from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class SearchClassPage(BasePage):
      
    # 页面元素
    studentService_loc = (By.LINK_TEXT, "Student")
    registration_loc = (By.LINK_TEXT, "Registration")
    searchClass_loc = (By.LINK_TEXT, "Search for Classes")
    p_term_loc = (By.NAME, "p_term")
    submit_loc = (By.XPATH, "//input[@value='Submit']")
    sel_subj_loc = (By.NAME, "sel_subj")
    course_search_loc = (By.XPATH, "//input[@value='Course Search']")
    sub_btn_loc (By.NAME, "SUB_BTN")
    
    # 页面动作
    def search_class(self):
        self.click(SearchClassPage.studentService_loc)
        self.click(SearchClassPage.registration_loc)
        self.click(SearchClassPage.searchClass_loc)
        self.select(SearchClassPage.p_term_loc, "202310")
        self.click(SearchClassPage.submit_loc)
        self.select(SearchClassPage.sel_subj_loc, "CS")
        self.click(SearchClassPage.course_search_loc)
        self.click(SearchClassPage.sub_btn_loc)
