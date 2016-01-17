from selenium import webdriver
from config import Settings
from src.huddleframework.pageobject.dashboardPage import DashboardPage
from baseUnitTestCase import BaseUnitTestCase


class SeleniumTests(BaseUnitTestCase):
	def __init__(self, *args, **kwargs):
		super(BaseUnitTestCase, self).__init__(*args, **kwargs)
		self.userid = Settings['userid']
		self.username = Settings['username']
		self.loginUri = Settings['loginUri']
		self.myHuddleUri = Settings['myHuddleUri']

	def setupprofile(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.http", Settings['ZAP_PROXY_HOST'])
		profile.set_preference('network.proxy.http_port', Settings['ZAP_PROXY_PORT'])
		profile.set_preference("network.proxy.ssl", Settings['ZAP_PROXY_HOST'])
		profile.set_preference('network.proxy.ssl_port', Settings['ZAP_PROXY_PORT'])
		profile.set_preference("webdriver_assume_untrusted_issuer", False)
		profile.set_preference("accept_untrusted_certs", True)
		profile.update_preferences()
		return profile

	def test_loginHuddle(self):
		self.profile = self.setupprofile()
		self.dashboardpage = self.login(self.loginUri, self.profile)
		self.dashboardpage.globalHeader.click_profile_dropdown()
		self.dashboardpage.globalHeader.click_on_workspace_picker()
		self.driver.implicitly_wait(5)
		pass

	def login(self, url, profile):
		self.driver = webdriver.Firefox(firefox_profile=profile)
		self.driver.get(url)
		self.driver.implicitly_wait(5)
		self.continuebutton = self.driver.find_element_by_css_selector('[data-automation="continue-button"]')
		try:
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
		except Exception:
			print(Exception.message)
		return DashboardPage(self.driver)

	# next
	# dashboardpage = driver.get(self.myHuddleUri)

	# def isVisible(self, locator, driver, timeout=2):
	# 	try:
	# 		ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
	# 		return True
	# 	except TimeoutException:
	# 		return False
