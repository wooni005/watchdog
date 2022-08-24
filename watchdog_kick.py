#!/usr/bin/python3

import time
import os
from watchdogdev import watchdog

exitThread = False

os.nice(20)
time.sleep(20)                  # Wait before starting
wd = watchdog('/dev/watchdog')

while not exitThread:
    wd.keep_alive()
    # print ("Kick")
    time.sleep(5)

# print "Magic Close"
wd.magic_close()
