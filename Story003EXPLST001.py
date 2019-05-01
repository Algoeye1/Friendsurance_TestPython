# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Story003EXPLST001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://thawing-shelf-73260.herokuapp.com/index.jsp""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story003_e_x_p_l_s_t001(self):
        driver = self.driver
        driver.get("http://thawing-shelf-73260.herokuapp.com/index.jsp")
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='sha77'])[1]/following::img[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), "^Attention: Unrecoverable Delete Action\n\nDo you really want to delete:\nsha77 [\\s\\S]$")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='sha'])[1]/following::img[1]").click()
        driver.find_element_by_id("reason").click()
        driver.find_element_by_id("reason").clear()
        driver.find_element_by_id("reason").send_keys("sha1")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::td[2]").click()
        try: self.assertEqual("sha1", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='sha1'])[1]/following::img[2]").click()
        driver.find_element_by_id("amount").click()
        driver.find_element_by_id("amount").clear()
        driver.find_element_by_id("amount").send_keys("120.0")
        driver.find_element_by_id("reason").click()
        driver.find_element_by_id("reason").clear()
        driver.find_element_by_id("reason").send_keys("sha12")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::td[1]").click()
        try: self.assertEqual(u"120,00 €", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::td[2]").click()
        try: self.assertEqual("sha12", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='shoppings1'])[1]/following::font[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add Expense'])[1]/following::font[2]").click()
        self.accept_next_alert = True
    
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
