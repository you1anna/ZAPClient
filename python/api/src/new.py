#!/usr/bin/env python

import time
from pprint import pprint
from zapv2 import ZAPv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

target = 'https://connect.telenordigital.com/gui/mypage'
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})
# Use the line below if ZAP is not listening on 8090
# zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

# do stuff
print 'Accessing target %s' % target
# try have a unique enough session...
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)


# ConnectID.importContext
contextId = zap.context.new_context('ConnectID')
print "contextID = " + contextId

zap.context.include_in_context('ConnectID', "\\Q" + target + "\\E")
zap.context.include_in_context('ConnectID', "\\Qhttps://connect.telenordigital.com\\E.*")
zap.context.include_in_context('ConnectID', "\\Qhttps://connect.telenordigital.com/gui/msisdn/login\\E")
#zap.spider.exclude_from_scan("\\Qhttps://connect.telenordigital.com/gui/msisdn/login\\E")
zap.context.exclude_from_context('ConnectID', "\\Qhttps://connect.telenordigital.com/oauth/logout\\E")

zap.authentication.set_authentication_method(contextId, "formBasedAuthentication", "loginUrl=https%3A%2F%2Fconnect.telenordigital.com%2Fgui%2Fmsisdn%2Flogin%3FFlowState%3DcmVxdWVzdENvbnRleHQ9dXJuJTNBZmRjJTNBYXV0aC50ZWxlbm9yZGlnaXRhbC5jb20lM0EyMDEzMTAwMSUzQU1TSVNETldpdGhQYXNzd29yZCxyZXF1ZXN0SWQ9X2hVWVhOaDFjS3J6SmFuODJPVzZOQlRSQlhQaixyZXF1ZXN0SXNzdWVyPWh0dHBzJTNBJTJGJTJGY29ubmVjdC50ZWxlbm9yZGlnaXRhbC5jb20lMkZvYXV0aCUyRnNhbWwlMkZtZXRhZGF0YSx1c2luZ1NhbWxTZXNzaW9ucz1mYWxzZSxyZWxheVN0YXRlPUc2Y2ZDaDVpd2NQdmZsNWd6UHZxNXNDazNxQw%253D%253D%26flows%3Dlogin_msisdn_password%26flows%3Dlogin_email_password%26flows%3Dsignup_msisdn_email%26brand%3Dmypage%26locale%3Den%26gui_config%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJyZXMiOiJHNmNmQ2g1aXdjUHZmbDVnelB2cTVzQ2szcUMiLCJwdXQiOiJtc2lzZG4iLCJhcHQiOiJ3ZWIiLCJhdWMiOiJodHRwczpcL1wvY29ubmVjdC50ZWxlbm9yZGlnaXRhbC5jb21cL29hdXRoXC9hdXRoZW50aWNhdGlvbl9jYWxsYmFjayIsImxobCI6ZmFsc2UsImVzYyI6W10sImxvYyI6ImVuIiwic2xzIjp0cnVlLCJsb2giOltdLCJzc2kiOm51bGwsImFjciI6W10sImJyZCI6Im15cGFnZSJ9.jFuRBhhCsMhBPTCZ2kaYJq_gpJn7U3Uoa5zc4DHlybr5GjDLxqb2tX8Bd-p84yafey2b9XN2_tjr2RKBPa8PreXt2IyU9CWofJZYtyHFrsTwfx4MAs0G7a9pMw1PuWkJC8dgTUFBFDAiBI17FZ8j5p5fUKwZTnti1xMdyll-MwM&loginRequestData=FlowState%3DcmVxdWVzdENvbnRleHQ9dXJuJTNBZmRjJTNBYXV0aC50ZWxlbm9yZGlnaXRhbC5jb20lM0EyMDEzMTAwMSUzQU1TSVNETldpdGhQYXNzd29yZCxyZXF1ZXN0SWQ9X2hVWVhOaDFjS3J6SmFuODJPVzZOQlRSQlhQaixyZXF1ZXN0SXNzdWVyPWh0dHBzJTNBJTJGJTJGY29ubmVjdC50ZWxlbm9yZGlnaXRhbC5jb20lMkZvYXV0aCUyRnNhbWwlMkZtZXRhZGF0YSx1c2luZ1NhbWxTZXNzaW9ucz1mYWxzZSxyZWxheVN0YXRlPUc2Y2ZDaDVpd2NQdmZsNWd6UHZxNXNDazNxQw%253D%253D%26locale%3Den%26brand%3Dmypage%26flows%3Dlogin_msisdn_password%26flows%3Dlogin_email_password%26flows%3Dsignup_msisdn_email%26gui_config%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJyZXMiOiJHNmNmQ2g1aXdjUHZmbDVnelB2cTVzQ2szcUMiLCJwdXQiOiJtc2lzZG4iLCJhcHQiOiJ3ZWIiLCJhdWMiOiJodHRwczpcL1wvY29ubmVjdC50ZWxlbm9yZGlnaXRhbC5jb21cL29hdXRoXC9hdXRoZW50aWNhdGlvbl9jYWxsYmFjayIsImxobCI6ZmFsc2UsImVzYyI6W10sImxvYyI6ImVuIiwic2xzIjp0cnVlLCJsb2giOltdLCJzc2kiOm51bGwsImFjciI6W10sImJyZCI6Im15cGFnZSJ9.jFuRBhhCsMhBPTCZ2kaYJq_gpJn7U3Uoa5zc4DHlybr5GjDLxqb2tX8Bd-p84yafey2b9XN2_tjr2RKBPa8PreXt2IyU9CWofJZYtyHFrsTwfx4MAs0G7a9pMw1PuWkJC8dgTUFBFDAiBI17FZ8j5p5fUKwZTnti1xMdyll-MwM%26cc%3D%252B47%26number%3D%7B%25username%25%7D%26password%3D%7B%25password%25%7D%26stayLoggedIn%3Don%26cid%3D1209585439.1435232212%26tid%3DUA-54179841-4%26wsid%3D042IJDTRZUTA%26waid%3Dconnect.ui")
zap.authentication.set_logged_in_indicator(contextId, "\\Q<a id=\'inst_link_index_header_logout\' href=\'/gui/mypage/overview?action=logout\' class=\'logout\'>Log out<\/a>\\E")
zap.authentication.set_logged_out_indicator(contextId, "\\Q<form id=\'msisdnLoginForm\' method=\'POST\' autocomplete=\'off\'>\\E")


userId = zap.users.new_user(contextId, "Bisera")
print "userID = " + userId
zap.users.set_authentication_credentials(contextId, userId, "username=********&password=********")
zap.users.set_user_enabled(contextId, userId, True)


zap.forcedUser.set_forced_user(contextId, userId)
zap.forcedUser.set_forced_user_mode_enabled(True)
zap.spider.set_option_max_depth(5)

zap.context.set_context_in_scope('ConnectID', True)


print 'Spidering target %s' % target
zap.spider.scan(target)
# Give the Spider a chance to start
time.sleep(5)
while (int(zap.spider.status()) < 100):
    print 'Spider progress %: ' + zap.spider.status()
    time.sleep(2)

print 'Spider completed'
# Give the passive scanner a chance to finish
time.sleep(5)


print 'Spidering target %s' % target
zap.spider.scan(target)
# Give the Spider a chance to start
time.sleep(5)
while (int(zap.spider.status()) < 100):
    print 'Spider progress %: ' + zap.spider.status()
    time.sleep(2)

print 'Spider completed'
# Give the passive scanner a chance to finish
time.sleep(5)


# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# base_url = "https://connect.telenordigital.com/gui/"
# verificationErrors = []
# accept_next_alert = True


# driver.get(target)
# driver.find_element_by_id("countryPrefix").clear()
# driver.find_element_by_id("countryPrefix").send_keys("+47")
# driver.find_element_by_id("phoneNumber").clear()
# driver.find_element_by_id("phoneNumber").send_keys("********")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("********")
# driver.find_element_by_id("inst_button_msisdn-login_form_login").click()

# driver.find_element_by_id("inst_link_index_nav_changepassword").click()
# driver.find_element_by_id("inst_link_index_tab_subscriptions").click()
# driver.find_element_by_id("inst_link_index_tab_purchasehistory").click()
# driver.find_element_by_id("inst_link_index_tab_manageclientauthorizations").click()
# driver.find_element_by_id("inst_link_index_tab_about").click()
# driver.find_element_by_css_selector("img.logo.visibleDesktop").click()
# driver.find_element_by_id("inst_link_index_changeprofile_edit").click()
# driver.find_element_by_xpath("//a[@id='inst_link_index_nav_overview']/span[2]").click()
# driver.find_element_by_id("inst_link_index_managephone_edit").click()
# driver.find_element_by_xpath("//a[@id='inst_link_index_nav_overview']/span[2]").click()
# driver.find_element_by_id("inst_link_index_manageemail_edit").click()
# driver.find_element_by_css_selector("img.logo.visibleDesktop").click()


# target = 'https://connect.telenordigital.com/'
# print 'And again %s' % target
# zap.spider.scan(target)
# # Give the Spider a chance to start
# time.sleep(2)
# while (int(zap.spider.status()) < 100):
#     print 'Spider progress %: ' + zap.spider.status()
#     time.sleep(2)

# print 'Spider completed'
# # Give the passive scanner a chance to finish
# time.sleep(5)


print 'Scanning target %s' % target
#zap.ascan.scan_as_user(target, 2, 2, recurse=True)
#zap.ascan.scan(target, recurse=True, inscopeonly=True)
zap.ascan.scan(target, recurse=True)

while (int(zap.ascan.status()) < 100):
    print 'Scan progress %: ' + zap.ascan.status()
    time.sleep(5)

print 'Scan completed'

# Report the results

print 'Hosts: ' + ', '.join(zap.core.hosts)
print 'Alerts: '
pprint (zap.core.alerts())