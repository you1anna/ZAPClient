from __future__ import absolute_import
import logging
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage
from ..pageobject.abstractpageclasses.webComponent import WebComponent


class CompanyPage(HuddleBasePage):

	NAVIGATION_AREA = (By.CSS_SELECTOR, u'[data-automation="Navigation"]')
	COMPANY_NAME_TITLE = (By.CSS_SELECTOR, u'[data-automation="companyName"]')
	PEOPLE_TAB_LINK = (By.CSS_SELECTOR, u'a:contains("people")')
	WORKSPACE_TAB_LINK = (By.CSS_SELECTOR, u'#applicationHost > div > div > div > div.resource-list-header > tabs > ul > li:nth-child(2) > a')
	PUBLIC_FILES_TAB_LINK = (By.CSS_SELECTOR, u'a:contains("Public files")')
	SETTINGS_LINK = (By.CSS_SELECTOR, u'[data-automation="settingsLink"]')

	def __init__(self, driver):
		self.relative_url = u""
		super(CompanyPage, self).__init__(driver, self.relative_url)
		self.peopleList = PeopleList(self.driver)

	def get_company_name(self):
		companyname = self.find(self.COMPANY_NAME_TITLE)
		return companyname.text()

	def go_to_people_list(self):
		self.click(self.PEOPLE_TAB_LINK)
		return PeopleList(self.driver)

	def go_to_workspaces_list(self):
		self.click(self.WORKSPACE_TAB_LINK)
		return WorkspacesList(self.driver)

	def go_to_public_files_list(self):
		self.click(self.PUBLIC_FILES_TAB_LINK)
		return PublicFilesList(self.driver)

	def open_settings_menu(self):
		self.click(self.SETTINGS_LINK)


class PeopleList(WebComponent):

	FILTER_BOX = (By.CSS_SELECTOR, u'[data-automation="resourceListFilter"]')
	SORT_DROPDOWN_BUTTON = (By.CSS_SELECTOR, u'[data-automation="sortMenu"]')
	SHOW_SELECTED_LINK = (By.CSS_SELECTOR, u'[data-automation="showSelectedButton"]')
	CLEAR_SELECTION_BUTTON = (By.CSS_SELECTOR, u'[data-automation="clearSelectionButton"]')
	REMOVE_FROM_COMPANY_BUTTON = (By.CSS_SELECTOR, u'[data-automation="removeFromCompanyButton"]')

	def __init__(self, driver):
		super(PeopleList, self).__init__(driver, (By.CSS_SELECTOR, u'[data-automation="MemberListPage"]'))

	def go_to_show_selected_list(self):
		self.click(self.SHOW_SELECTED_LINK)

	def clear_selection(self):
		self.click(self.CLEAR_SELECTION_BUTTON)


class WorkspacesList(WebComponent):
	def __init__(self, driver):
		super(WorkspacesList, self).__init__(driver, (By.CSS_SELECTOR, u'[data-automation="WorkspaceListPage"]'))
		pass


class PublicFilesList(WebComponent):
	def __init__(self, driver):
		super(PublicFilesList, self).__init__(driver, (By.CSS_SELECTOR, u'[data-automation="PublicFileList"]'))
		pass

