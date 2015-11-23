#!/usr/bin/env python

import time
import subprocess
from pprint import pprint
from zapv2 import ZAPv2, ZapError
from selenium import webdriver

loginUrl = 'https://login.huddle.dev/'
myHuddleUrl = 'https://my.huddle.dev/'
apiHuddleUrl = 'https://api.huddle.dev/'
userId = 'Robin.Wmgr1'
# workspaceUrl

ZAP_PROXY_HOST = '127.0.0.1'
ZAP_PROXY_PORT = 8080
MEDIUM = "MEDIUM"
HIGH = "HIGH"

zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

#subprocess.Popen(['/path/to/zap.sh', '-daemon'], stdout=open(os.devnull, 'w'))

contextId = zap.context.import_context('HuddleContext2.context')
zap.context.set_context_in_scope('HuddleContext2', True)
print "contextID: " + contextId

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", ZAP_PROXY_HOST)
profile.set_preference("network.proxy.http_port", ZAP_PROXY_PORT)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)

# you have to use remote, otherwise you'll have to code it yourself in python to
# driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX)

driver.get(loginUrl)
driver.implicitly_wait(5)
if driver.find_element_by_css_selector('[data-automation="continue-button"]').is_displayed():
    driver.find_element_by_css_selector('[data-automation="email-field"]').clear()
    driver.find_element_by_css_selector('[data-automation="email-field"]').send_keys("Robin.wmgr1")
    driver.find_element_by_css_selector('[data-automation="continue-button]').click()
driver.implicitly_wait(3)
driver.find_element_by_id("passwordField").clear()
driver.find_element_by_id("passwordField").send_keys("Steria12345$")

zap.urlopen(loginUrl)
print('Spidering target %s' % loginUrl)
zap.spider.scan(loginUrl)
time.sleep(2)

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




