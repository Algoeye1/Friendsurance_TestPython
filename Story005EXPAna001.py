# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Story005EXPAna001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://thawing-shelf-73260.herokuapp.com/index.jsp""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story005_e_x_p_ana001(self):
        driver = self.driver
        driver.get("http://thawing-shelf-73260.herokuapp.com/index.jsp")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("TestUID_1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("df12@434c")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::div[5]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='List Categories'])[1]/following::font[2]").click()
        driver.find_element_by_name("month").click()
        Select(driver.find_element_by_name("month")).select_by_visible_text("2019.01")
        driver.find_element_by_name("month").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::div[1]").click()
        try: self.assertEqual("Category", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings12'])[1]/following::font[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Expense tracker", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Value'])[1]/following::tr[1]").click()
        try: self.assertEqual("shoppings12", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Value'])[1]/following::font[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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
