#!/usr/bin/env python

import time
import subprocess
from selenium import webdriver
from pprint import pprint
from zapv2 import ZAPv2, ZapError


target = 'https://login.huddle.dev/'
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

subprocess.Popen(['/path/to/zap.sh', '-daemon'], stdout=open(os.devnull, 'w'))
time.sleep(10)

print('Accessing target %s' % target)


HuddleContext = zap.context.import_context('D:\dev\ZAPClient\Contexts\HuddleContext2.context')
zap.context.set_context_in_scope(HuddleContext, True)
pprint(zap.context.context_list)
pprint(zap.context.context('HuddleContext'))
zap.context.set_context_in_scope('HuddleContext', 'TRUE')


zap.context.include_in_context('HuddleContext', "\\Qhttps://login.huddle.dev\\E.*")
print('stop')

zap.authentication.set_login_url(1, 'https://login.huddle.dev/', postdata='username=Robin.Wmgr1&password=Steria12345$')
zap.authentication.set_login_indicator(1, 'you are logged in')
zap.authentication.login(1)

userId = zap.users.new_user(contextId, "Wmgr1")
print "userID = " + userId

zap.urlopen(target)
print('Spidering target %s' % target)
zap.spider.scan(target)
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
print('Scanning target %s' % target)
zap.ascan.scan(target)
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


