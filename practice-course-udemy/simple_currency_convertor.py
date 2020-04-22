"""
1. Gather the parameters of interest
2. Construct the URL and send a GET request to it
3. For unsuccessful requests: print the error message
4. For successful requests: extract the relevant data and calculate the result
5. Display the results to the user
"""
import json
import requests

base_url = "https://api.exchangeratesapi.io"
date = input("Please enter the date (in the format 'yyyy-mm-dd' or 'latest'):")
base = input("convert from (currency):")
curr = input("Convert to (currency):")
quan = float(input("How much {} do you wan to convert: ".format(base)))

url = base_url + "/" + date + "?base=" + base + "&symbols=" + curr
response = requests.get(url)

if(response.ok is False):
    print("\nError {}:".format(response.status_code))
    print(response.json()['error'])
else:
    data = response.json()
    rate = data['rates'][curr]

    result = quan*rate
    print(json.dumps(data, indent=4))
    print(result)
    print("\n{0} {1} is equal to {2} {3}, based upon exchange rates on {4}".format(quan,base,result,curr,data['date']))