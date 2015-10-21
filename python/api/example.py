#!/usr/bin/env python

import time
from pprint import pprint
from zapv2 import ZAPv2, ZapError

target = 'https://login.huddle.dev/'
# zap = ZAPv2()
# if ZAP is not listening on 8090
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

print('Accessing target %s' % target)

zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)

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

# Report the results

print("Hosts: " + ", ".join(zap.core.hosts))
print ('Alerts: ')
pprint(zap.core.alerts())


