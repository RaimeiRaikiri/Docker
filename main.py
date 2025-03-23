import requests

payload = {
"appid": API_KEY,
"q": "Rainham",
"units": "metric"}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", payload)

print(response.text)


