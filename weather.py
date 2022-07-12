import requests,json, datetime, pandas as pd

cities = ['Cologne', 'Munich', 'Berlin']
apilink = 'http://api.weatherapi.com/v1/forecast.json?key=bea853d469e0444dbe7152331220507&days=3&q='
finalRes = []

for i in cities:
	res = json.loads(requests.get(apilink + i).text)
	try:
		for j in res['forecast']['forecastday']:
			for k in j['hour']:
				individual = {}
				individual['city']   = i
				individual['hour']   = k['time']
				individual['temp_c'] = k['temp_c']
				individual['wind_kph'] = k['wind_kph']
				individual['cloud'] = k['cloud']
				finalRes.append(individual)	
	except Exception as e:
		print(e)
pd.DataFrame(finalRes).to_csv('weatherapi.csv')
