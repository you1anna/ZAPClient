
from selenium.webdriver.common.by import By
from huddleframeworksrc.framework.huddleframework.pageobject.activationPage import ActivationPage
from huddleframeworksrc.framework.huddleframework.pageobject.dashboardPage import DashboardPage

class InvitePage(DashboardPage):
    INVITE_MODAL_BUTTON = (By.CSS_SELECTOR,'[data-automation="invitation-modal-btn"]')
    COMPONENT_PILL_INPUT = (By.CSS_SELECTOR,'[data-automation="component-pills"]')

    def __init__(self, driver):
        self.relative_url = "CompanyDialog.aspx"
        super(InvitePage, self).__init__(driver)

    def __type_invitee(self, invitee):
        self.type(self.COMPONENT_PILL_INPUT, invitee)

    def invite(self, invitee):
        self.__type_invitee(invitee)