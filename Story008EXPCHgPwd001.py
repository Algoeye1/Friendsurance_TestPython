# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Story008EXPCHgPwd001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://thawing-shelf-73260.herokuapp.com/index.jsp""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story008_e_x_p_c_hg_pwd001(self):
        driver = self.driver
        driver.get("http://thawing-shelf-73260.herokuapp.com/index.jsp")
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::font[2]").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("qwerty")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("newpassword1").click()
        driver.find_element_by_id("newpassword1").clear()
        driver.find_element_by_id("newpassword1").send_keys("df12@434c")
        driver.find_element_by_id("newpassword2").click()
        driver.find_element_by_id("newpassword2").clear()
        driver.find_element_by_id("newpassword2").send_keys("df12@434c")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::font[2]").click()
        try: self.assertEqual("List Expenses:", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::font[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual("Expense tracker", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Toggle navigation'])[1]/following::font[2]").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
