import requests

# api_key = '61b974d1d037ecdb33098330f1df9003'

city = input('Enter a city to see the weather: ')
api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=61b974d1d037ecdb33098330f1df9003&units=metric'.format(city)

print('Made by SxxVe ')

res = requests.get(api_url)
data = res.json()

wind = data['main']['pressure']
des = data['weather'][0]['description']
temp = data['main']['temp']

print('The temperature is:',temp,'C')
print('Wind:',wind)
print('Description: ',des)
