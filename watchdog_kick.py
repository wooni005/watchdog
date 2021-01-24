#!/usr/bin/python3

import time
import os
from watchdogdev import watchdog

exit = False

os.nice(20)
time.sleep(20)                  # Wait before starting
wd = watchdog('/dev/watchdog')

while not exit:
    wd.keep_alive()
    # print ("Kick")
    time.sleep(5)

# print "Magic Close"
wd.magic_close()
