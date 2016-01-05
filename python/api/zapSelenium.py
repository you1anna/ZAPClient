from pprint import pprint
from selenium import webdriver
from baseTestCase import BaseTestCase
from huddleBasePage import HuddleBasePage
from dashboardPage import DashboardPage
import selenium.webdriver.support.ui as ui
from config import Settings


class SeleniumTests(BaseTestCase):
	def __init__(self):
		BaseTestCase.__init__(self)
		self.userid = Settings['userid']
		self.username = Settings['username']
		self.myHuddleUri = Settings['myHuddleUri']

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
		self.driver = webdriver.Firefox(firefox_profile=profile)
		self.driver.get(url)
		self.driver.implicitly_wait(5)
		self.continuebutton = self.driver.find_element_by_css_selector('[data-automation="continue-button"]')
		if self.continuebutton.is_displayed():
			self.driver.find_element_by_css_selector('[data-automation="email-field"]').clear()
			self.driver.find_element_by_css_selector('[data-automation="email-field"]').send_keys(Settings['username'])
			self.continuebutton.click()
			self.driver.implicitly_wait(3)
			self.driver.find_element_by_id("passwordField").clear()
			self.driver.find_element_by_id("passwordField").send_keys(Settings['password'])
			self.driver.implicitly_wait(4)
			self.continuebutton.click()
			self.driver.implicitly_wait(8)
		return DashboardPage(self.driver)


	# next
	# dashboardpage = driver.get(self.myHuddleUri)

	# def isVisible(self, locator, driver, timeout=2):
	# 	try:
	# 		ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
	# 		return True
	# 	except TimeoutException:
	# 		return False
