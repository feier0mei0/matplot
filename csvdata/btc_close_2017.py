# -- coding: utf-8 --

import requests

# 无法访问该url
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)

with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
file_requests = req.json(req)
print(file_requests)
