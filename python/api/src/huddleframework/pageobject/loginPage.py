
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage
from ..pageobject.dashboardPage import DashboardPage


class LoginPage(HuddleBasePage):
    relative_url = ""
    base_url = "http://login.huddle.{0}"
    USERNAME_FIELD = (By.CSS_SELECTOR, '[data-automation="email-field"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-automation="continue-button"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-automation="password-field"]')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, '[data-automation="continue-button"]')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver, self.relative_url, False)

    def _type_username(self, username):
        self.type(self.USERNAME_FIELD, username)

    def _click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def _type_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def _click_sign_in_button(self):
        self.click(self.SIGNIN_BUTTON)

    def login(self, username, password):
        self._type_username(username)
        self._click_continue_button()
        self._type_password(password)
        self._click_sign_in_button()
        return DashboardPage(self.driver)
