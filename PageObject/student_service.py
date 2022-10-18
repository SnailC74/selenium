from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class StudentServicePage(BasePage):
      
    # 页面元素
    registration_loc = (By.LINK_TEXT, "Registration")
    studentRecord_loc = (By.LINK_TEXT, "Student Records")
    
    # 页面动作
    def registration(self):
        self.click(StudentServicePage.registration_loc)
            
    def student_record(self):
        self.click(StudentServicePage.studentRecord_loc)
