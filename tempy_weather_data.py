#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage:
    A simple request through the OpenWeatherMap API to call for current
    temperatue in a particular city.
    Returns the temperature.
"""

import requests
import sys

def weather_data():
    current = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "", # City and Country code go here
        "units": "metric",
        "lang": "", # Your language preferences
        "appid": "" #APIKEY goes here
        }

    try:
        data_current = requests.get(current, params=params).json()
        external_temp = data_current["main"]["temp"]
        return({"temp": external_temp})
    except:
        sys.exit(0)