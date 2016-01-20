
from selenium.webdriver.common.by import By
from .abstractpageclasses.webComponent import WebComponent


class CreateWorkspaceFrame(WebComponent):

	SHADOWBOX_CONTENT = (By.ID, "shadowbox_content")
	TEMPLATE_SELECTOR = (By.CSS_SELECTOR, "[ID$='templateSelect']")
	TITLE_FIELD = (By.CSS_SELECTOR, "input[ID$='title']")
	DESCRIPTION_FIELD = (By.ID, "textarea[ID$='m_description']")
	CREATE_WORKSPACE_BUTTON = (By.ID, "create-workspace-button")
	CLOSE_SHADOW_BOX_BUTTON = (By.ID, "shadowbox_nav_close")

	def __init__(self, driver):
		super(CreateWorkspaceFrame, self).__init__(driver, (By.CSS_SELECTOR, "#shadowbox"))

	def click_next(self):
		self.driver.switch_to.frame(self.find(self.SHADOWBOX_CONTENT))
		self.click(self.CREATE_WORKSPACE_BUTTON)
		self.driver.switch_to_default_content()

	def click_close(self):
		self.click(self.CLOSE_SHADOW_BOX_BUTTON)
		self.driver.switch_to_default_content()

	def type_title(self, title):
		self.driver.switch_to.frame(self.find(self.SHADOWBOX_CONTENT))
		self.type(self.TITLE_FIELD, title)
		self.driver.switch_to_default_content()
		return self


