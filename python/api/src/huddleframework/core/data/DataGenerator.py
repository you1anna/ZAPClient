# from amhed"s amazing project databuilder import AHDatabuilder

import logging
import uuid
import random
logger = logging.getLogger('tests_logger')

def user_info():
	user = dict(
		FirstName="PyFN" + random_string(),
		LastName="PyLN" + random_string(),
		Email="PyEmail" + random_string() + "@huddle.local",
		Telephone=random.randrange(10000000000, 99999999999, 7),
		Company="PyCom" + str(uuid.uuid4()),
		Username="UN" + str(uuid.uuid4()),
		Password="P@ssword1"
	)
	logger.debug(__name__ + "generating user info:" + str(user))
	return user


def random_string():
	return str(uuid.uuid4())


if __name__ == "__main__":
	# see what it does
	user_info()
