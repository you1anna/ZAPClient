from __future__ import absolute_import
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage
from ..pageobject.activationPage import ActivationPage


class CreateAccountPage(HuddleBasePage):

	FIRSTNAME_FIELD = (By.CSS_SELECTOR, u'[data-automation="firstName_field"]')
	LASTNAME_FIELD = (By.CSS_SELECTOR, u'[data-automation="lastName_field"]')
	EMAIL_FIELD = (By.CSS_SELECTOR, u'[data-automation="email_field"]')
	CONFIRMEMAIL_FIELD = (By.CSS_SELECTOR, u'[data-automation="confirmEmail_field"]')
	TELEPHONE_FIELD = (By.CSS_SELECTOR, u'[data-automation="telephone_field"]')
	COMPANY_FIELD = (By.CSS_SELECTOR, u'[data-automation="company_field"]')
	PASSWORD_FIELD = (By.CSS_SELECTOR, u'[data-automation="password_field"]')
	CONFIRMPASSWORD_FIELD = (By.CSS_SELECTOR, u'[data-automation="confirmPassword_field"]')
	USERNAME_FIELD = (By.CSS_SELECTOR, u'[data-automation="username_field"]')
	TERMSOFSERVICE_CHECKBOX = (By.CSS_SELECTOR, u'[data-automation="termsOfService_checkbox"]')
	CREATE_BUTTON = (By.CSS_SELECTOR, u'[data-automation="create_button"]')

	def __init__(self, driver):
		self.relative_url = u"/signup/createaccount.aspx?package=package_freetrial"
		super(CreateAccountPage, self).__init__(driver, self.relative_url, False)

	def register_new_user(self, user):
		u"""
		:param user: dictionary of user attributes e.g. data.datagenerator.userprofile
		:return: PageObject.ActivationPage
		"""
		self._type_first_and_last_name(user[u'FirstName'], user[u'LastName'])
		self._type_email(user[u'Email'])
		self._type_telephone_and_company(user[u'Telephone'], user[u'Company'])
		self._type_username_and_password(user[u'Username'], user[u'Password'])
		self._click_agreement()
		return self._click_create()

	def _type_first_and_last_name(self, first_name, last_name):
		self.type(self.FIRSTNAME_FIELD, first_name)
		self.type(self.LASTNAME_FIELD, last_name)

	def _type_email(self, email):
		self.type(self.EMAIL_FIELD, email)
		self.type(self.CONFIRMEMAIL_FIELD, email)

	def _type_telephone_and_company(self, telephone, company):
		self.type(self.TELEPHONE_FIELD, telephone)
		self.type(self.COMPANY_FIELD, company)

	def _type_username_and_password(self, username, password):
		self.type(self.USERNAME_FIELD, username)
		self.type(self.PASSWORD_FIELD, password)
		self.type(self.CONFIRMPASSWORD_FIELD, password)

	def _click_agreement(self):
		self.click(self.TERMSOFSERVICE_CHECKBOX)

	def _click_create(self):
		self.click(self.CREATE_BUTTON)
		return ActivationPage(self.driver)
