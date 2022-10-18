class BasePage：

    def __init__(self):
        global driver
        # 打开浏览器
        self.driver = webdriver.chrome()
        driver.implicitly_wait(10)
        driver = self.driver
        # 加载网页
        self.driver.get("https://https://www.uregina.ca/") 
    
    # 定位元素的关键字
    def locator_element(self, loc):
        return self.driver.find.element(*loc)

    # 设置值的关键字
    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)
        
    # 点击的关键字
    def click(self, loc):
        self.locator_element(loc).click()
    
    # 封装下拉框关键字
    def select(self, loc, value):
        sel = select(self.locator_element(loc))
        sel.select_by_value(value)
