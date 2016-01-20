#
# from sqlalchemy import Table, MetaData, Column, Integer
# import SQLAlchemy
# import pyodbc
# import urllib
# params = urllib.quote_plus("DRIVER={SQL Server Native Client 10.0};SERVER=dagger;DATABASE=test;UID=user;PWD=password")
#
# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
# # todo
# # we would avoid this where possible
# # but things like making a user an admin, enable publishing, adding account could ONLY be done via SQL
#
# class huddledb(object):
#
# 	engine = create_engine("DRIVER={SQL Server};SERVER=cloak;DATABASE=test;UID=user;PWD=password")
# 	def __init__(self):
# 		super().__init__()
