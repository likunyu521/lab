import requests
import json


class Weather:

    def __init__(self):
        self.data = []

    def city_weather(city):
        url = "http://notify.mse.sogou.com/weather?city=" + city

        payload = {}
        headers = {
            'Cookie': 'IPLOC=CN1100'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        json_response = json.loads(response.text)

        print(city + ':' + json_response['statuscode'])


citys = ["北京", "上海", "天津", "重庆", "广州", "成都", "杭州", "南京", "深圳"]

for city in citys:
    Weather.city_weather(city)

print('thanks')