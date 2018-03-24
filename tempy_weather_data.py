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
        "appid": "33528e2b76c5e8219b4aa0f64194cb0f"
        }

    try:
        data_current = requests.get(current, params=params).json()
        external_temp = data_current["main"]["temp"]
        logging.info("SUCCESS")
        return({"temp": external_temp})
    except Exception as e:
        logging.exception("EROOR, MATE!")
        weather_data()