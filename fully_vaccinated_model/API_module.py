import requests
import json
API = "https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=us:*&key=f7038b3e8176fc9358413aad840b9ffbc972a142"
 
response = requests.get(API)                        # call the API/collect response
formattedResponse = json.loads(response.text)[1:]   # create JSON with data (don't need column one)
population = int(formattedResponse[0][1])           # temporary population