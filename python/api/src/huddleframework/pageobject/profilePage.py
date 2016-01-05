from __future__ import absolute_import
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage


class ProfilePage(HuddleBasePage):

	EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, u'.edit-list')
	PROFILE_FIRST_AND_LAST_NAME = (By.CSS_SELECTOR, u'[data-automation="profile-display-name"]')

	def __init__(self, driver):
		self.relative_url = u""
		super(ProfilePage, self).__init__(driver, self.relative_url)


	def click_edit(self):
		self.click(self.EDIT_PROFILE_BUTTON)
		from .editProfilePage import EditProfilePage
		return EditProfilePage(self.driver)

	def get_profile_first_and_last_name(self):
		return self.find(self.PROFILE_FIRST_AND_LAST_NAME).text
