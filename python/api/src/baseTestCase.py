# import logging
# import logging.config
# from .config import Settings
# from contexts import setup, teardown
# from selenium import webdriver
#
#
# # logging.config.dictConfig(LoggingConfig)
#
# class BaseTestCase:
# 	def __init__(self):
# 		self.driver = None
#
# 	@setup
# 	def setUp(self):
# 		self.driver = webdriver.Firefox()
#
# 	@teardown
# 	def tearDown(self):
# 		self.driver.close()
#
# 	def login_static_user(self, username=Settings['username'], password=Settings['password']):
# 		return LoginPage(self.driver).open().login(username, password)
