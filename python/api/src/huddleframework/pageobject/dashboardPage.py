
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage


class DashboardPage(HuddleBasePage):
	url = "http://login.huddle.{0}/myhuddle/"
	HOME_ICON = (By.CSS_SELECTOR, '[data-automation="huddle-header-home-button"]')

	def __init__(self, driver):
		self.relative_url = ""
		super(DashboardPage, self).__init__(driver, self)
