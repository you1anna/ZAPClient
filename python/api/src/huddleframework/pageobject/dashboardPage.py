from __future__ import absolute_import
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.huddleBasePage import HuddleBasePage

class DashboardPage(HuddleBasePage):
    url = u"http://login.huddle.{0}/myhuddle/"
    HOME_ICON = (By.CSS_SELECTOR, u'[data-automation="huddle-header-home-button"]')

    def __init__(self, driver):
        self.relative_url = u""
        super(DashboardPage, self).__init__(driver, self)
