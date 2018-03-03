import requests
import json

def get_weather():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    payload = {'city': '050010'}
    data = requests.get(url, params = payload).json()

    print(data['title'])
    for weather in data['forecasts']:
        print(weather['dateLabel'] + ':' + weather['telop'])
        # 天気ゲット
        temp = weather['temperature']
        # 最高気温 最低気温
        maxtemp = temp['max']
        mintemp = temp['min']
        if maxtemp is None and mintemp is None:
            print( '最低気温:' + '-' + ' ' + '最高気温:' + '-')
        elif  mintemp is None:
            print( '最低気温:' + '-' + ' ' + '最高気温:' + maxtemp['celsius'])
        else:
            print( '最低気温:' + mintemp['celsius'] + ' ' + '最高気温:' + maxtemp['celsius'])

if __name__ == '__main__':

	get_weather()
