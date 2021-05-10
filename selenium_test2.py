#coding = utf-8
from selenium import webdriver
from time import sleep,ctime
import os
import pytest
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        
        options = webdriver.ChromeOptions()
        #chrome浏览器可执行文件的地址
        options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        #浏览器驱动：chromedriver的下载地址
        chrome_driver_binary = "C:/Program Files/Google/Chrome/Application/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_binary,chrome_options=options)
        
        #要测试的网页，打开网页
        self.driver.get("http://www.baidu.com")
    
    def test(self):
        sleep(3)
        #此处id为"kw"的控件，输入测试文本：Test search
        self.driver.find_element_by_id("kw").send_keys("Test search")
        #此处找到的id为"su"的控件，模拟鼠标执行点击
        self.driver.find_element_by_id("su").click()
    def tearDown(self):
        sleep(3)
        #退出浏览器
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()

