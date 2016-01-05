from __future__ import with_statement
from __future__ import absolute_import
import logging
import os.path
import time
import smtplib
import re
from email import message_from_file
from email.parser import HeaderParser

from .config import Config
from io import open
logger = logging.getLogger(u'tests_logger')

# not fully tested under load :)
class Smtpdropbox(object):
	def __init__(self):
		self.config = Config

	# todo
	def retrieve_activation_code(self, to_email):
		file, header = self._wait_for_email(to_email, u'Huddle Account Activation Code')
		if file is not None:
			with open(file) as email_file:
				body = self._extract_email(email_file)
				activation_code = re.search(u'Account Activation Code: (.+?)\\r\\n\\r\\n', body)
				if activation_code:
					return activation_code.group(1)  # return the first found
		else:
			return None

	# todo
	def retrieve_invitation(self, to_email):
		pass

	# todo
	def retrieve_approval(self, to_email):
		pass

	def _wait_for_email(self, to_email, subject):
		email_file = None
		email_header = None
		for i in xrange(self.config[u'read_tries']):
			if __debug__:
				logger.debug(u"waiting for email...")
			time.sleep(self.config[u'read_interval'])
			email_file, email_header = self._search_by_email_header(to_email, subject)
			if email_file is None:
				pass
			else:
				return email_file, email_header
		return email_file, email_header

	def _search_by_email_header(self, to_email, subject):
		for file in self._fetch_emails_in_last_x_minutes(self.config[u'read_period']):
			with open(file) as email:
				header = HeaderParser().parse(email)
				if ((header[u'to'] is not None) & (header[u'to'] == to_email)) & \
					((header[u'subject'] is not None) & (subject in header[u'subject'])):
					return file, header
		return None, None

	def _fetch_emails_in_last_x_minutes(self, period_in_minutes, start_time=time.time()):
		past = start_time - period_in_minutes * 60
		results = []
		for root, dirs, files in os.walk(self.config[u'smtp_file_path']):
			for name in files:
				file_path = os.path.join(root, name)
				# tips: os.path.getmtime = modification of file && os.path.getctime = creation of the file
				if os.path.getctime(file_path) >= past:
					results.append(file_path)
		return results

	# this hack might need some more work :)
	@staticmethod
	def _extract_email(email_file):
		msg_parts = message_from_file(email_file)
		for part in msg_parts.walk():
			# each part is a either non-multipart, or another multipart message
			# that contains further parts... Message is organized like a tree
			if part.get_content_type() == u'text/plain':
				return part.get_payload(None, True).decode(u'utf-8')


# not implemented yet - dummy code placed here
class Smtpsender(object):
	def __init__(self):
		self.config = Config

	@staticmethod
	def send_message(subject, from_address, to_address, msg):
		# me == the sender's email address
		# you == the recipient's email address
		msg[u'Subject'] = subject
		msg[u'From'] = from_address
		msg[u'To'] = to_address

		# Send the message via our own SMTP server.
		s = smtplib.SMTP(u'localhost')
		s.send_message(msg)
		s.quit()
