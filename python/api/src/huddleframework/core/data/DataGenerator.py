# from amhed"s amazing project databuilder import AHDatabuilder
from __future__ import absolute_import
import logging
import uuid
import random
logger = logging.getLogger(u'tests_logger')

def user_info():
	user = dict(
		FirstName=u"PyFN" + random_string(),
		LastName=u"PyLN" + random_string(),
		Email=u"PyEmail" + random_string() + u"@huddle.local",
		Telephone=random.randrange(10000000000, 99999999999, 7),
		Company=u"PyCom" + unicode(uuid.uuid4()),
		Username=u"UN" + unicode(uuid.uuid4()),
		Password=u"P@ssword1"
	)
	logger.debug(__name__ + u"generating user info:" + unicode(user))
	return user


def random_string():
	return unicode(uuid.uuid4())


if __name__ == u"__main__":
	# see what it does
	user_info()
