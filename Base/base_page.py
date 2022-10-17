class BasePage：

    def __init__(self):
        global driver
        # 打开浏览器
        self.driver = webdriver.chrome()
        driver = self.driver
        # 加载网页
        self.driver.get("https://https://www.uregina.ca/") 
        
    def locator_element(self, loc):
        return self.driver.find.element(*loc)
