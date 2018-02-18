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

while True:
    weather_data = weather_data()
    ext_temp = weather_data["temp"]
    int_temp = read_sensor_data()
    current_time = time.time()
    data_write(current_time, int_temp, ext_temp)
    time.sleep(15)
    