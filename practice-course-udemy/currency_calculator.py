import requests
import json

base_url = "https://api.exchangeratesapi.io/latest"

params_url = base_url + "?symbols=INR&base=USD&date=latest"
response = requests.get(params_url)
data = json.dumps(response.json(), indent=4)
print(data)
usd_to_inr_rates = json.dumps(response.json()['rates']['INR'], indent=4)
print(usd_to_inr_rates)