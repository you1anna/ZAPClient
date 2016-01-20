
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage
from ..pageobject.filesui.filesDetailsPage import FilesDetailsPage


class ActivationPage(HuddleBasePage):

	ACTIVATION_CODE_FIELD = (By.CSS_SELECTOR, '[data-automation="activationCode_field"]')
	ACTIVATION_BUTTON = (By.CSS_SELECTOR, '[data-automation="activate_button"]')

	def __init__(self, driver):
		self.relative_url = "/signup/activation.aspx"
		super(ActivationPage, self).__init__(driver, self.relative_url, False)

	def enter_and_submit_activation_code(self, activation_code):
		self.type(self.ACTIVATION_CODE_FIELD, activation_code)
		self.click(self.ACTIVATION_BUTTON)
		return FilesDetailsPage(self.driver)
