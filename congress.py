import os
import json
import requests

congress_api_key = "4N7MNPWk48CkWhTV4oaL4fr5pyzl6ghVD5i6ljdZ"

url = f"https://api.congress.gov/v3/committee-report/119/hrpt?api_key={congress_api_key}&format=json"

r = requests.get(url)
results = r.json()

fr_url = results['reports'][0]['url']
fr = requests.get(fr_url + f"&api_key={congress_api_key}")

result = fr.json()
print(result)
