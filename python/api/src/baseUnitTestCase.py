import logging
import logging.config
from config import Settings
from selenium import webdriver
import unittest
from loginPage import LoginPage

# logging.config.dictConfig(LoggingConfig)

class BaseUnitTestCase(unittest.TestCase):
	def __init__(self):
		super(BaseUnitTestCase, self).__init__()
		self.driver = None

	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		self.driver.close()

	def login_static_user(self, username=Settings['username'], password=Settings['password']):
		return LoginPage(self.driver).open().login(username, password)
