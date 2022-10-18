# selenium
#用电脑模拟人操作浏览器，实现自动化测试

from selenium import webdriver

#打开浏览器

driver = webdriver.chrome()

#加载网页

driver.get("https://www.baidu.com")


#元素定位

find_element_by_id()

find_element_by_name()

find_element_by_class_name()

find_element_by_tag_name()

find_element_by_link_text()

find_element_by_partial_link_text()

find_element_by_xpath()

find_element_by_css_selector()


# Unittest

# 1. 设计模式（封装）

PO模式 Page Object Model

1. 基础层：selenium原生的方法

2. 页面对象层：页面的元素和动作

3. 测试用例层：测试用例和测试数据

页面对象层调用基础层，测试用例层调用页面对象层


# 2. 断言

判断预期结果与实际结果是否相符

self.assertEqual() 判断两个值是否相等

self.assertTrue() 判断一个值是否为true

self.assertIn() 判断一个值是否在另一个值里面
