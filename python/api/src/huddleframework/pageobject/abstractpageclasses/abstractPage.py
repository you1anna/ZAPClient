from __future__ import absolute_import
__author__ = u'Huddle'
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from ..abstractpageclasses.webComponent import WebComponent


class AbstractPage(WebComponent):
	base_url = None

	def __init__(self, driver, url):
		u"""
		Use HuddleBasePage instead
		This is the generic base page of any page object - inherit WebElement which support shortcut to finding objects etc
		:param	driver: browser driver e.g. firefox, chrome etc; expects a string variable driver.domain
		:param	url: page url e.g. https://my.huddle.dev/createaccount.aspx
		"""
		super(AbstractPage, self).__init__(driver, None)
		self.base_url = u'http://my.huddle.{0}'
		self.relative_url = url
		self.wait_for_page_load()

	def current_page(self):
		return self.driver.current_url

	def open(self, param=None):
		self.driver.get(unicode(self.get_page_url()).format(param))
		self.driver.maximize_window()
		return self

	def get_page_url(self):
		return unicode.format(self.base_url, self.driver._domain) + self.relative_url

	def wait_for_page_load(self, timeout=30):
		self.logger.debug(u"Waiting for page to load at {}.".format(self.driver.current_url))
		old_page = self.driver.find_element_by_tag_name(u'html')
		yield
		WebDriverWait(self, timeout).until(staleness_of(old_page))
