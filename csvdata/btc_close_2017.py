# -- coding: utf-8 --

import json
import pygal
import math

# 将数据存储到列表
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

for btc_dict in btc_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{} is month {} week {},{}, the close price is {}RMB".format(date, month, week, weekday, close))


# 收盘价折线图
dates = []
months = []
weeks = []
weekdays = []
close = []

for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价(￥)'
line_chart.x_labels = dates

N = 20  # x轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图(￥).svg')

# 收盘价对数变换折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价(￥)'
line_chart.x_labels = dates

N = 20  # x轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图(￥).svg')
