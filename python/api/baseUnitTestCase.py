import unittest
from selenium import webdriver
from .config import Settings
from .src.huddleframework.pageobject.loginPage import LoginPage


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

	def runTest(self):
		pass
