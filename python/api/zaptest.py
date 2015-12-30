#!/usr/bin/env python

import os
import time
import navigation
from config import Settings
from pprint import pprint
from zapv2 import ZAPv2, ZapError

ZAP_PROXY_HOST = '127.0.0.1'
ZAP_PROXY_PORT = 8080
MEDIUM = "MEDIUM"
HIGH = "HIGH"

disk = Settings['disk']
userId = Settings['userid']
loginUrl = Settings['loginUri']
myHuddleUri = Settings['myHuddleUri']

root = disk + ":\dev\Huddle-ZAPClient"
contextFile = "Contexts\\" + Settings['contextFileName']
contextFilePath = os.path.join(root, contextFile)

zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

contextId = zap.context.import_context(contextFilePath)
zap.context.set_context_in_scope(Settings['contextFileName'], True)
print "contextID: " + contextId


# NEXT >>>>>>>>>>>>>>>
zap.spider.exclude_from_scan(".*\/leave.*")
zap.spider.exclude_from_scan(".*logout.*")
zap.spider.exclude_from_scan(".*/leave.*")
#zap.httpsessions.active_session()
zap.spider.set_option_max_depth(5)

fftest = navigation.SeleniumTests()
profile = fftest.setupprofile()
fftest.login(loginUrl, profile)

zap.urlopen(myHuddleUri)
print('Spidering target %s' % myHuddleUri)
CID = int(contextId)
print(CID)
zap.spider.scan_as_user(loginUrl, userid=3, contextId=CID)
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




