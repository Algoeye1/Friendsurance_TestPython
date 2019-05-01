# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Story002EXPCRT001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://thawing-shelf-73260.herokuapp.com/index.jsp""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story002_e_x_p_c_r_t001(self):
        driver = self.driver
        driver.get("http://thawing-shelf-73260.herokuapp.com/index.jsp")
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::div[1]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Expense tracker'])[2]/following::font[2]").click()
        driver.find_element_by_id("day").click()
        driver.find_element_by_id("day").clear()
        driver.find_element_by_id("day").send_keys("15")
        driver.find_element_by_id("month").click()
        driver.find_element_by_id("month").clear()
        driver.find_element_by_id("month").send_keys("01")
        driver.find_element_by_id("year").click()
        driver.find_element_by_id("year").clear()
        driver.find_element_by_id("year").send_keys("2019")
        driver.find_element_by_id("category").click()
        driver.find_element_by_id("category").click()
        driver.find_element_by_id("amount").click()
        driver.find_element_by_id("amount").clear()
        driver.find_element_by_id("amount").send_keys("12")
        driver.find_element_by_id("reason").click()
        driver.find_element_by_id("reason").clear()
        driver.find_element_by_id("reason").send_keys("shop")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='List Expenses:'])[1]/following::img[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Modify'])[1]/following::tr[1]").click()
        try: self.assertEqual(u"12,00 €", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Modify'])[1]/following::font[2]").click()
        try: self.assertEqual("14/1/19", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Modify'])[1]/following::font[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Modify'])[1]/following::font[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Modify'])[1]/following::font[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Modify'])[1]/following::font[4] | ]]
        try: self.assertEqual("shoppings1", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Modify'])[1]/following::font[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[4] | ]]
        try: self.assertEqual("sha", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[4]").text)
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
