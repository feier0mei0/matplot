# -- coding: utf-8 --

import json

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
