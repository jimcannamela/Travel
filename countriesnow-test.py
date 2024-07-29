# import requests

# url = "https://countriesnow.space/api/v0.1/countries/flag/images"

# payload = {
  
#    "iso2": "NG"

# }

# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

import requests

url = "https://countriesnow.space/api/v0.1/countries/cities"

payload = {
    
    "country": "nigeria"

    }
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)