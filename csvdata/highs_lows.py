# -- coding: utf-8 --

import csv

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)
    print(header_now)
