#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:48:26 2018

@author: ralchev
"""

import requests
import sys
import logging

def weather_data():
    logging.basicConfig(filename="error.log", level=logging.INFO)
    current = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Sofia,bg",
        "units": "metric",
        "lang": "bg",
        "appid": ""
        }

    try:
        data_current = requests.get(current, params=params).json()
        external_temp = data_current["main"]["temp"]
        return({"temp": external_temp})
    except Exception as e:
        logging.exception("ERROR")
        weather_data()