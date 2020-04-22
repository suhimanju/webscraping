import json
import requests

base_url = "https://api.exchangeratesapi.io"
historical_url = base_url + "/2020-04-18"
time_period = base_url + "/history?start_at=2017-04-20&end_at=2018-04-3&symbols=INR"
response = requests.get(time_period)
data = json.dumps(response.json(), indent=4)
print(data)