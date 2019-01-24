import time
import unittest
import HtmlTestRunner
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\theda\\PycharmProjects\\TestProject1\\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_LoginFunctionalityTest_1(self):
        #Negative Testing
        self.driver.get("https://utest.com/")
        #Find Element->1) Find & Locate 2) Determine action
        # 3) Pass parameter
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(10)
        self.driver.find_element_by_id("username").send_keys("abcd@gmail.com")
        self.driver.find_element_by_name("password").send_keys("abcd1234")
        time.sleep(5)
        self.driver.find_element_by_id("kc-login").click()

        x = self.driver.title
        # x is here a variable -> Variable is a container that stores data
        print(x)
        self.assertEqual(x, "Log in to uTest")


    def test_LoginFunctionalityTest_2(self):
        #Negative Testing
        self.driver.get("https://utest.com/")
        #Find Element->1) Find & Locate 2) Determine action
        # 3) Pass parameter
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(10)
        self.driver.find_element_by_id("username").send_keys("abcd@gmail.com")
        time.sleep(5)
        self.driver.find_element_by_name("password").send_keys("abcd1234")
        time.sleep(5)
        self.driver.find_element_by_id("kc-login").click()

        x = self.driver.title
        # x is here a variable -> Variable is a container that stores data
        print(x)
        self.assertEqual(x, "Log to uTest")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\theda\\PycharmProjects\\TestProject1\\report"))
