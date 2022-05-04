# -- coding: utf-8 --

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温、最低气温
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据日期和天气绘图
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, 'red', alpha=0.5)
plt.plot(dates, lows, 'blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图线的格式
title = "Daily high and low temperatures - 2014\nDeath Valley,CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()
