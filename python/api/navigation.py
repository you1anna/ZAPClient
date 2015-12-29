from pprint import pprint
from selenium import webdriver
import unittest
import navigation.webdriver.support.ui as ui
from config import Settings

class SeleniumTests():
	def __init__(self, driver):
		self.driver = driver
		self.userid = Settings['userid']

	def setup(self):
		pprint(self.domain)

	def setupprofile(self):
		driver = webdriver.FirefoxProfile()
		driver.set_preference("network.proxy.type", 1)
		driver.set_preference("network.proxy.http", Settings['ZAP_PROXY_HOST'])
		driver.set_preference('network.proxy.http_port', Settings['ZAP_PROXY_PORT'])
		driver.update_preferences()
		return driver

	def login(self, url, driver):
		driver = webdriver.Firefox(firefox_profile=driver)
		driver.get(url)
		driver.implicitly_wait(5)
		continueButton = driver.find_element_by_css_selector('[data-automation="continue-button"]')
		if continueButton.is_displayed():
			driver.find_element_by_css_selector('[data-automation="email-field"]').clear()
			driver.find_element_by_css_selector('[data-automation="email-field"]').send_keys("Robin.wmgr1")
			continueButton.click()
			driver.implicitly_wait(3)
			driver.find_element_by_id("passwordField").clear()
			driver.find_element_by_id("passwordField").send_keys("Steria12345$")
			driver.implicitly_wait(8)

			# def isVisible(self, locator, driver, timeout=2):
			# 	try:
			# 		ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
			# 		return True
			# 	except TimeoutException:
			# 		return False
