from __future__ import absolute_import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging


class WebComponent(object):

	logger = logging.getLogger(u'tests_logger')
	locator = None

	def __init__(self, driver, locator, wait_time=30):
		self.locator = locator
		self.driver = driver
		if locator is None:
			self.object = driver
		else:
			self.object = self.find(locator=locator, wait_time=wait_time)

	def find(self, locator, condition=None, wait_time=15):
		condition = expected_conditions.visibility_of_element_located(locator) if condition is None else condition
		d = self.driver
		WebDriverWait(d, wait_time).until(condition)
		return d.find_element(*locator)

	def clear(self, locator):
		if __debug__:
			self.logger.debug(u"Cleared - " + locator[1])
		self.find(locator=locator, condition=expected_conditions.visibility_of_element_located(locator)).clear()
		return self

	def type(self, locator, msg):
		if __debug__:
			self.logger.debug(u"Typed - " + locator[1])
		self.find(locator=locator, condition=expected_conditions.visibility_of_element_located(locator)).send_keys(msg)
		return self

	def click(self, locator):
		if __debug__:
			self.logger.debug(u"Clicked - " + locator[1])
		self.find(locator=locator, condition=expected_conditions.visibility_of_element_located(locator)).click()
		return self

	def wait(self, timeout):
		self.driver.implicitly_wait(timeout)
