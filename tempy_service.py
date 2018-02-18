#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage:
    Takes data from:
        -- the internal temperature sensors,
        -- the OpenWeatherMap API.
    Passes the values of those two together with current time
    every 15 minutes to the data_write function in tempy_db script.
    
"""
from tempy_weather_data import weather_data
from tempy_sensor_data import read_sensor_data
import time
from tempy_db import data_write

# Retrieving current external temperature to pass as a parameter later on
weather_data = weather_data()
ext_temp = weather_data["temp"]

# Retriving current internal temperature to pass as a parameter later on
int_temp = read_sensor_data()

# Current time
current_time = time.time()

# Submitting data to database every 15 minutes
while True:
    data_write(current_time, int_temp, ext_temp)
    time.sleep(889)
    