from __future__ import absolute_import
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage
from ..pageobject.abstractpageclasses.webComponent import WebComponent


class EditProfilePage(HuddleBasePage):

	EDIT_PROFILE_TAB_BUTTON = (By.CSS_SELECTOR, u'[data-automation="tab-editmyprofile"]')
	MY_SETTING_TAB_BUTTON = (By.CSS_SELECTOR, u'[data-automation="tab-mysettings"]')
	CHANGE_MY_PASSWORD_TAB_BUTTON = (By.CSS_SELECTOR, u'[data-automation="tab-changepassword"]')
	PROFILE_SETTINGS_TAB = None

	def __init__(self, driver):
		self.relative_url = u"/myhuddle/profile.aspx"
		super(EditProfilePage, self).__init__(driver, self.relative_url)
		self.PROFILE_SETTINGS_TAB = EditMyProfileTab(driver)


	def click_edit_my_profile(self):
		self.click(self.EDIT_PROFILE_TAB_BUTTON)

	# todo
	def click_my_settings(self):
		pass

	# todo
	def click_change_password(self):
		pass

	def get_profile_name(self):
		self.click(self.MY_SETTING_TAB_BUTTON)


class EditMyProfileTab(WebComponent):
	PROFILE_PICTURE_BROWSER = (By.ID, u'ctl00_ctl00_ctl00_pageBody_BodyColumn_WorkFrameContent_fuUploadPicture')
	DISPLAY_NAME_TEXTBOX = (By.ID, u'ctl00_ctl00_ctl00_pageBody_BodyColumn_WorkFrameContent_tbDisplayName')
	FIRST_NAME_TEXTBOX = (By.ID, u'ctl00_ctl00_ctl00_pageBody_BodyColumn_WorkFrameContent_tbFirstname')
	LAST_NAME_TEXTBOX = (By.ID, u'ctl00_ctl00_ctl00_pageBody_BodyColumn_WorkFrameContent_tbLastname')
	COMPANY_NAME_TEXTBOX = (By.ID, u'ctl00_ctl00_ctl00_pageBody_BodyColumn_WorkFrameContent_tbCompany')
	UPDATE_BUTTON = (By.ID, u'ctl00_ctl00_ctl00_pageBody_BodyColumn_WorkFrameContent_btnSaveProfile')

	def __init__(self, driver):
		super(EditMyProfileTab, self).__init__(driver, (By.ID, u'profile-settings'))

	def type_display_name(self, display_name):
		self.clear(self.DISPLAY_NAME_TEXTBOX)
		self.type(self.DISPLAY_NAME_TEXTBOX, display_name)
		return self

	def type_first_name(self, first_name):
		self.clear(self.FIRST_NAME_TEXTBOX)
		self.type(self.FIRST_NAME_TEXTBOX, first_name)
		return self

	def type_last_name(self, last_name):
		self.clear(self.LAST_NAME_TEXTBOX)
		self.type(self.LAST_NAME_TEXTBOX, last_name)
		return self

	def click_update(self):
		self.click(self.UPDATE_BUTTON)
		return self
