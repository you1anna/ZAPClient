
__author__ = 'robin.miklinski'
from selenium.webdriver.common.by import By
from ...pageobject.abstractpageclasses.webComponent import WebComponent
from ...pageobject.workspacePage import WorkspacePage
from ...pageobject.workspacePage import WorkspaceTabContent


class FilesDetailsPage(WorkspacePage):

	#TODO Construct this later
	relative_url = "https://my.huddle.dev/workspace/{1}/files/#/{2}"

	def __init__(self, driver):
		super(FilesDetailsPage, self).__init__(driver, self.relative_url)
		self.WorkspaceTabContent = _FilesDetailsTab(driver)


class _FilesDetailsTab(WorkspaceTabContent):

	FILE_TITLE = (By.CSS_SELECTOR, '[data-automation="file-header-title"]')
	LOCK_BUTTON = (By.CSS_SELECTOR, '[data-automation="lock"]')
	UNLOCK_BUTTON = (By.CSS_SELECTOR, '[data-automation="unlock"]')
	ActionButtons = None

	def __init__(self, driver):
		super(_FilesDetailsTab, self).__init__(driver, (By.CSS_SELECTOR, '[data-automation="file-details-page"]'))
		self.ActionButtons = _FilesDetailsActionButtons(self.driver)

	def find_document_title(self):
		return self.find(self.FILE_TITLE)

	def find_lock_button(self):
		return self.find(self.LOCK_BUTTON)

	def find_unlock_button(self):
		return self.find(self.UNLOCK_BUTTON)


class _FilesDetailsActionButtons(WebComponent):

	ADD_REVIEWERS_BUTTON = (By.CSS_SELECTOR, '[data-automation="actions-add-reviewers-button"]')

	def __init__(self, driver):
		super(_FilesDetailsActionButtons, self).__init__(driver, (By.CSS_SELECTOR, '[data-automation="file-details-action-buttons"]'))
		pass

	def find_add_reviewers_button(self):
		return self.find(self.ADD_REVIEWERS_BUTTON)
