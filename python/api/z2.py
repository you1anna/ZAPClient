#!/usr/bin/env python

import time
import os
import subprocess
from zapv2 import ZAPv2

# Start ZAP
subprocess.Popen(['/path/to/zap.sh', '-daemon'], stdout=open(os.devnull, 'w'))
time.sleep(10)

zap = ZAPv2()

print 'Session will be saved to: %s' % zap.core.home_directory

zap.core.save_session('Session Name')

zap.core.save_session('/path/to/dir/HuddleSession')

zap.core.shutdown