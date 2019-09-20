#module
import requests
#Call the Chicago Food Inspection API
response = requests.get("https://data.cityofchicago.org/resource/4ijn-s7e5.json")
# Decode the raw JSON data.
response_data = response.json()

print(response_data)


#or in 1 line
#import requests
#response_data = requests.get("https://data.cityofchicago.org/resource/4ijn-s7e5.json").json()
#print(response_data)