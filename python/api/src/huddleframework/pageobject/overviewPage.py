
__author__ = 'robin.miklinski'
from selenium.webdriver.common.by import By
from ..pageobject.abstractpageclasses.webComponent import WebComponent
from ..pageobject.workspacePage import WorkspacePage
from ..pageobject.workspacePage import WorkspaceTabContent

class OverviewPage(WorkspacePage):

    #TODO Construct this later
    INVITE_MODAL = (By.CSS_SELECTOR,'[data-automation="invitation-modal-btn"]')

    def __init__(self, driver):
        self.relative_url = "/workspace/{1}"
        super(OverviewPage, self).__init__(driver, self.relative_url)
        self.WorkspaceTabContent = _OverviewTab(driver)

    def invite_user(self, invitee):
        self.click(self.INVITE_MODAL)
        return InviteModal(self.driver)


class _OverviewTab(WorkspaceTabContent):

    def __init__(self, driver):
        super(_OverviewTab, self).__init__(driver, (By.ID, "workspace-overview"))


class InviteModal(OverviewPage):

    EMAIL_ADDRESS_INPUT = (By.CSS_SELECTOR, '[data-automation="component-pills"] input')

    def __init__(self, driver, invitee):
        super(InviteModal, self).__init__(driver)
        self.invitee = invitee

    def __type_invitee(self, invitee):
        self.type(self.EMAIL_ADDRESS_INPUT, invitee)
        #TODO: need to hit enter so that pill is generated

        self.type(self.EMAIL_ADDRESS_INPUT, invitee)

    def send_invites(self):
        self.click( (By.CSS_SELECTOR,'[data-automation="submitButton"]'))
