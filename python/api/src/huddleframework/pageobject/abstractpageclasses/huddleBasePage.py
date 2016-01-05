from __future__ import absolute_import
from ..abstractpageclasses.abstractPage import AbstractPage
from ...pageobject.globalHeader import GlobalHeader
from ...pageobject.abstractpageclasses.webComponent import WebComponent
from selenium.webdriver.common.by import By


class HuddleBasePage(AbstractPage):
	u"""
	This is the generic base huddle page of any page object - inherit WebElement which support shortcut to finding objects etc
	:param	driver: browser driver e.g. firefox, chrome etc
	:param	url: page url e.g. https://my.huddle.dev/createaccount.aspx
	:param	has_gloabl_header: default=True; with exception to public pages
	"""
	globalHeader = None
	WELCOME_DIALOG_DISMISS_BUTTON = (By.CSS_SELECTOR, u"[data-automation='slideshow-dismiss-button']")

	def __init__(self, driver, url, has_global_header=True):
		super(HuddleBasePage, self).__init__(driver, url)
		if has_global_header:
			self.globalHeader = GlobalHeader(driver)

		self.logger.debug(u"Initialised - " + self.__class__.__name__)

	def dismiss_welcome_dialog(self):
		self.click(locator=self.WELCOME_DIALOG_DISMISS_BUTTON)

	def sign_out(self):
		if self.globalHeader is None:
			raise Exception(u"global header is not registered on page:" + self.current_page())
		else:
			self.globalHeader.sign_out()

	# todo - determine if slideshow exists rather than get selenium to wait for it
	def close_the_slide_show_frame(self):
		try:
			SlideShowFrame(self.driver).close()
		except Exception:
			pass
		return self

	def slideshow_component(self):
		return SlideShowFrame.SLIDESHOW_COMPONENT

class SlideShowFrame(WebComponent):
	DISMISS_SLIDESHOW_BUTTON = (By.CSS_SELECTOR, u'[data-automation="slideshow-dismiss-button"]')
	SLIDESHOW_COMPONENT = (By.CSS_SELECTOR, u'[data-automation="component-slideshow"]')

	def __init__(self, driver):
		super(SlideShowFrame, self).__init__(driver, (By.CSS_SELECTOR, u'[data-automation="component-slideshow"]'))

	def close(self):
		self.click(self.DISMISS_SLIDESHOW_BUTTON)
