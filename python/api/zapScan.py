#!/usr/bin/env python

import os
import time
import platform
import subprocess
import zapSelenium
from config import Settings
from pprint import pprint
from zapv2 import ZAPv2, ZapError

MEDIUM = "MEDIUM"
HIGH = "HIGH"

disk = Settings['disk']
username = Settings['username']
userid = Settings['userid']
loginUrl = Settings['loginUri']
myHuddleUri = Settings['myHuddleUri']
proxyUrl = Settings['proxyUrl']
contextFile = Settings['contextFileName']
zapPath = Settings['zapPath']

root = disk + ":\dev\Huddle-ZAPClient"
contextFilePath = os.path.join(root, 'Contexts', contextFile)

zap = ZAPv2(proxies={'http': proxyUrl, 'https': proxyUrl})

if not os.path.exists(zapPath):
	zapPath = 'C:\Program Files\OWASP\Zed Attack Proxy'
zapBat = os.path.join(zapPath, 'zap.bat')

print subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT), '\n'
print 'Zap path = ' + zapBat
print 'Starting ZAP...'

subprocess.Popen(zapBat, stdout=open(os.devnull, 'w'), cwd=Settings['zapPath'])
version = ''
while version == '':
	try:
		version = zap.core.version
	except:
		print 'ZAP not running yet, waiting.'
		time.sleep(1)
	else:
		time.sleep(1)
print 'ZAP v' + version + ' launched successfully.\n'


contextId = zap.context.import_context(contextFilePath)
zap.context.set_context_in_scope(Settings['contextFileName'], True)
print "contextID: " + contextId

# Client config
zap.spider.exclude_from_scan(".*\/leave.*")
zap.spider.exclude_from_scan(".*logout.*")
zap.spider.exclude_from_scan(".*/leave.*")
zap.authentication.set_logged_in_indicator(contextId, '\\Qlogout.aspx\E')
# zap.httpsessions.active_session()
# zap.spider.set_option_max_depth(5)

# Map Huddle in Zap
mapDashboardPage = zapSelenium.SeleniumTests()
mapDashboardPage.test_loginHuddle()

zap.urlopen(myHuddleUri)
print('Spidering target %s' % myHuddleUri)
zap.spider.scan_as_user(loginUrl, userid=userid, contextId=contextId)
time.sleep(2)

zap.httpsessions.active_session()

try:
	while int(zap.spider.status()) < 100:
		print('Spider progress: ' + zap.spider.status() + '%')
		time.sleep(2)
except ZapError, e:
	print(e.message)

print('Spider completed')
time.sleep(5)

# wait
print('Scanning target %s' % loginUrl)
zap.ascan.scan(loginUrl)
try:
	while int(zap.ascan.status()) < 100:
		print('Scan progress: ' + zap.ascan.status() + '%')
		time.sleep(2)
except ZapError, e:
	print(e.message)

print('Scan completed')

print("Hosts: " + ", ".join(zap.core.hosts))
print ('Alerts: ')
pprint(zap.core.alerts())

# def scanBeforeLogin():
#     huddleWebApp.goToLoginPage()
#     spiderWithZap()
#     setAttackStrength()
#     zapScanner.setEnablePassiveScan(true)
#     scanWithZap()
#     List<Alert> alerts = filterAlerts(zapScanner.getAlerts())
#     logAlerts(alerts)
#     assertThat(alerts.size(), equalTo(0))
#
#
# def createContext():
#     zap.context.include_in_context(huddleContext, "\\Q" + loginUrl + "\\E.*")
#     zap.context.include_in_context(huddleContext, "\\Q" + myHuddleUrl + "\\E.*")
#     zap.context.include_in_context(huddleContext, "\\Q" + apiHuddleUrl + "\\E.*")
#
#     zap.authentication.set_logged_in_indicator(contextId, '\\Q\/logout.aspx\E')
#     zap.authentication.set_authentication_method(contextId, "formBasedAuthentication")
#
#     zap.context.exclude_from_context('HuddleContext', "\\Qhttps://push.huddle.dev\\E")
