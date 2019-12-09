#!/opt/argonone/bin/python3
# -*- coding: utf-8 -*-
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# PEP 8, PEP 263.
"""
Argon Systemd Shutdown script
"""

import sys
import smbus
import RPi.GPIO as GPIO

rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

if len(sys.argv) > 1:
    bus.write_byte(0x1a, 0)
    if sys.argv[1] == "poweroff" or sys.argv[1] == "halt":
        try:
            bus.write_byte_data(0x1a,0,0xFF)
        except:
            rev = 0
