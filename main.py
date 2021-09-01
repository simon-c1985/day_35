import requests

API_KEY = '5a0c3693602ca6757d080b2017f1164c'
latitude = 59.9072
longitude = 30.5058
exclude = 'minutely,current,daily'
parameters = {
    'lat': latitude,
    'lon': longitude,
    'exclude': exclude,
    'appid': API_KEY,
    'units': 'metric',
}
will_rain = False
response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
json_data = response.json()
for index in range(0, 12):
    if int(json_data['hourly'][index]['weather'][0]['id']) < 700:
        print(json_data['hourly'][index]['weather'][0]['id'])
        will_rain = True
        print(f'{index} hours later will be rain')
if will_rain:
    print('Bring an umbrella')
