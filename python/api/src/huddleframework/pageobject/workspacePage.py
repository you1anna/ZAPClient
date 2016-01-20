
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage
from ..pageobject.abstractpageclasses.webComponent import WebComponent


class WorkspacePage(HuddleBasePage):

	#TODO Construct this later
	WorkspaceHeader = None
	WorkspaceTabContent = None

	def __init__(self, driver, url="https://my.huddle.{0}/workspace/{1}"):
		super(WorkspacePage, self).__init__(driver, url)
		self.WorkspaceHeader = WorkspaceHeader(driver)
		self.WorkspaceTabContent = WorkspaceTabContent(driver, None)


class WorkspaceHeader(WebComponent):

	FILES_TAB_LINK = (By.CSS_SELECTOR, '[data-text="Files"]')

	def __init__(self, driver):
		super(WorkspaceHeader, self).__init__(driver, (By.CSS_SELECTOR, '.torque-ws-header'))


class WorkspaceTabContent(WebComponent):

	def __init__(self, driver, locator):
		super(WorkspaceTabContent, self).__init__(driver, (By.ID, 'dashboard-main'))
		if locator is None:
			self.object = driver
		else:
			self.object = self.find(locator)
