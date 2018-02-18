#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage:
    Reads data from the single temperature sensor attached to the RPi2.
    Returns Temperature in Celsius.
"""

import os
import glob
import time

os.system("modprobe w1-gpio")

base_dir = "/sys/bus/w1/devices/"
device_folder = glob.glob(base_dir + "28*")[0]
device_file = device_folder + "/w1_slave"

def get_sensor_data():
    f = open(device_file, "r")
    lines = f.readlines()
    f.close()
    return(lines)

def read_sensor_data():
    lines = get_sensor_data()
    while lines[0].strip()[-3:] != "YES":
        time.sleep(1)
        lines = get_sensor_data()

    equals_pos = lines[1].find("t=")

    if equals_pos != 1:
        temp_string = lines[1][equals_pos+2:]
        temp_celsius = float(temp_string) / 1000.0
        return(temp_celsius)