import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# ID定位
driver.find.element(By.ID, "kw").send_keys("University of Regina")
# Name定位
driver.find.element(By.NAME, "wd").send_keys("University of Regina")
# Link_text定位
driver.find.element(By.LINK_TEXT, "地图").click()
# Partial_link定位
driver.find.element(By.PARTIAL_LINK, "图").click()

class TestCase(unittest.TestCase):
  
    def test_1_login(self):
        global driver
        # 打开浏览器
        driver = webdriver.chrome()
        # 加载网页
        driver.get("https://https://www.uregina.ca/")
        # Link_text定位
        driver.find.element(By.LINK_TEXT, "Current Students").click()
        # Link_text定位
        driver.find.element(By.LINK_TEXT, "UR Courses").click()
        
        
