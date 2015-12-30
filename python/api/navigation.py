from pprint import pprint
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from config import Settings


class SeleniumTests:
	def __init__(self):
		self.userid = Settings['userid']

	def setupprofile(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.http", Settings['ZAP_PROXY_HOST'])
		profile.set_preference('network.proxy.http_port', Settings['ZAP_PROXY_PORT'])
		profile.set_preference("network.proxy.ssl", Settings['ZAP_PROXY_HOST'])
		profile.set_preference('network.proxy.ssl_port', Settings['ZAP_PROXY_PORT'])
		profile.update_preferences()
		return profile

	def login(self, url, profile):
		driver = webdriver.Firefox(firefox_profile=profile)
		driver.get(url)
		driver.implicitly_wait(5)
		continuebutton = driver.find_element_by_css_selector('[data-automation="continue-button"]')
		if continuebutton.is_displayed():
			driver.find_element_by_css_selector('[data-automation="email-field"]').clear()
			driver.find_element_by_css_selector('[data-automation="email-field"]').send_keys(Settings['userid'])
			continuebutton.click()
			driver.implicitly_wait(3)
			driver.find_element_by_id("passwordField").clear()
			driver.find_element_by_id("passwordField").send_keys("Steria12345$")
			driver.implicitly_wait(4)
			continuebutton2 = driver.find_element_by_css_selector('[data-automation="continue-button"]')
			continuebutton2.click()
			driver.implicitly_wait(8)
			# def isVisible(self, locator, driver, timeout=2):
			# 	try:
			# 		ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
			# 		return True
			# 	except TimeoutException:
			# 		return False