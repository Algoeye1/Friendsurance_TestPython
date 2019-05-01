# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Story001EXPTKR001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://thawing-shelf-73260.herokuapp.com/index.jsp""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story001_e_x_p_t_k_r001(self):
        driver = self.driver
        driver.get("http://thawing-shelf-73260.herokuapp.com/index.jsp")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("TestUID_1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("qwerty")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("go_list_expenses").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='List Expenses:'])[1]/following::font[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='List Expenses:'])[1]/following::font[2] | ]]
        self.assertEqual("Date", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='List Expenses:'])[1]/following::font[2]").text)
        self.assertEqual("Category", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Date'])[1]/following::font[2]").text)
        self.assertEqual("amount", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::font[2]").text)
        self.assertEqual("Reason", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='amount'])[1]/following::font[2]").text)
        self.assertEqual("Modify", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Reason'])[1]/following::font[2]").text)
    
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
