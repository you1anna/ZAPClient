from __future__ import absolute_import
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import AbstractPage


class Locators(object):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, u'[data-automation="sign-in-button"]')
    SIGN_OUT_SUCCESS_MSG = (By.CSS_SELECTOR, u'[data-automation="sign-out-success-msg"]')
    DEFAULT_LOGO = (By.CSS_SELECTOR, u'[data-automation="default-logo"]')

class SignOutPage(AbstractPage):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, u'[data-automation="sign-in-button"]')
    SIGN_OUT_SUCCESS_MSG = (By.CSS_SELECTOR, u'[data-automation="sign-out-success-msg"]')
    DEFAULT_LOGO = (By.CSS_SELECTOR, u'[data-automation="default-logo"]')
    relative_url = u"http://my.huddle.{0}/logout.aspx"

    def __init__(self, driver):
       super(SignOutPage, self).__init__(driver, self.relative_url)

    def login(self):
        self.click(Locators.SIGN_IN_BUTTON)

    def find_login_button(self):
        return self.find(Locators.SIGN_IN_BUTTON)

    def find_sign_out_success_msg(self):
        return self.find(Locators.SIGN_OUT_SUCCESS_MSG)

    def find_default_logo(self):
        return self.find(Locators.DEFAULT_LOGO)
