from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.webComponent import WebComponent
from ..pageobject.signOutPage import SignOutPage


class GlobalHeader(WebComponent):

	# locator
	GLOBAL_HEADER = (By.CSS_SELECTOR, "#header-content")
	PROFILE_DROPDOWN_LINK = (By.CSS_SELECTOR, "[data-automation='huddle-header-avatar-menu-link']")
	DASHBOARD_LINK = (By.ID, "dashboard-link")
	HELP_LINK = (By.CSS_SELECTOR, "[data-automation='help-link']")
	WORKSPACE_PICKER = (By.CSS_SELECTOR, "[data-automation='huddle-header-workspace-select']")

	def __init__(self, driver):
		super(GlobalHeader, self).__init__(driver, self.GLOBAL_HEADER)

	def click_profile_dropdown(self):
		self.click(self.PROFILE_DROPDOWN_LINK)
		return ProfileDropdownMenu(self.driver)

	def click_on_dashboard_link(self):
		self.click(self.DASHBOARD_LINK)

	def click_on_help_link(self):
		self.click(self.HELP_LINK)

	# TODO not finished
	def sign_out(self):
		self.click_profile_dropdown() \
			.click_on_sign_out_link()
		return SignOutPage(self.driver)

	def click_on_workspace_picker(self):
		self.click(self.WORKSPACE_PICKER)
		return WorkspaceDowndropMenu(self.driver)


class ProfileDropdownMenu(WebComponent):

	MY_PROFILE_LINK = (By.CSS_SELECTOR, "#header-profile-link")
	ACCOUNT_SETTINGS_LINK = (By.CSS_SELECTOR, "a:contains('Account settings')")
	COMPANY_LINK = (By.CSS_SELECTOR, "li.company-link a")
	SIGNOUT_LINK = (By.CSS_SELECTOR, "#logout-link")
	REQUEST_NEW_ACCOUNT_LINK = (By.CSS_SELECTOR, "a:contains('Request new account'')")

	def __init__(self, driver):
		super(ProfileDropdownMenu, self).__init__(driver, (By.CSS_SELECTOR, ".huddle-header__bar__profile-menu__dropdown"))

	def click_on_company_link(self):
		from .companyPage import CompanyPage
		self.click(self.COMPANY_LINK)
		return CompanyPage(self.driver)

	def click_on_my_profile_link(self):
		from .profilePage import ProfilePage
		self.click(self.MY_PROFILE_LINK)
		return ProfilePage(self.driver)

	# Todo
	def click_on_account_settings_link(self):
		self.click(self.ACCOUNT_SETTINGS_LINK)

	# Todo
	def click_on_request_new_account_link(self):
		self.click(self.REQUEST_NEW_ACCOUNT_LINK)

	def click_on_sign_out_link(self):
		self.click(self.SIGNOUT_LINK)
		return SignOutPage(self.driver)


class WorkspaceDowndropMenu(WebComponent):

	# locator
	CREATE_WORKSPACE_LINK = (By.CSS_SELECTOR, '[data-automation="workspace-select-create-workspace-link"]')

	def __init__(self, driver):
		super(WorkspaceDowndropMenu, self).__init__(driver, (By.CSS_SELECTOR, '[data-automation="huddle-header-workspace-select"]'))

	#@staticmethod
	def _get_workspace_link_locator(self, workspace_title):
		workspace_list = self.driver.find_element_by_css_selector('[data-automation="workspace-filter-list"]').find_elements_by_tag_name("li")

		for workspace in workspace_list:
			if workspace.text == workspace_title:
				print(workspace.text)
				return (By.CSS_SELECTOR, '[data-automation="workspace-select-workspace-link"]')

	def click_create_workspace_link(self):
		self.click(self.CREATE_WORKSPACE_LINK)
		from .createWorkspaceFrame import CreateWorkspaceFrame
		try:
			create_workspace_frame = CreateWorkspaceFrame(self.driver)
		except Exception:
			self.click(self.CREATE_WORKSPACE_LINK)
			create_workspace_frame = CreateWorkspaceFrame(self.driver)
		return create_workspace_frame

	def click_option_by_title(self, workspace_title):
		self.click(self._get_workspace_link_locator(workspace_title))
		from .overviewPage import OverviewPage
		return OverviewPage(self.driver)
