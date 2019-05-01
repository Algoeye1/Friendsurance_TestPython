# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Story006EXPCRTdata001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://thawing-shelf-73260.herokuapp.com/index.jsp""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story006_e_x_p_c_r_tdata001(self):
        driver = self.driver
        driver.get("http://thawing-shelf-73260.herokuapp.com/index.jsp")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::div[5]").click()
        try: self.assertEqual("Register new user", driver.find_element_by_link_text("Register new user").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual("Register new user", driver.find_element_by_link_text("Register new user").text)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[1]/following::div[2]").click()
        self.assertEqual("Username", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[1]/following::label[1]").text)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username'])[1]/following::div[3]").click()
        self.assertEqual("Password", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username'])[1]/following::label[1]").text)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").click()
        self.assertEqual("Login", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").text)
        driver.find_element_by_id("go_add_expense").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::div[1]").click()
        try: self.assertEqual("Login", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("go_list_expenses").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").click()
        self.assertEqual("Login", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").text)
        driver.find_element_by_id("go_list_categories").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::div[1]").click()
        self.assertEqual("Login", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").text)
        driver.find_element_by_id("go_show_statistics").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").click()
        self.assertEqual("Login", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Show Statistics'])[1]/following::h3[1]").text)
    
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
