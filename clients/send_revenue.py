# importing the requests library
import requests, json

# First authenticate in order to use the required APIs, then call the targeted service api

# API Endpoint
API_ENDPOINT = "http://127.0.0.1:8000/api/"

# Credentials of api user
credentials = { 'username' : 'amro', 'password' : 'amr12amr' }

# service path
api_url = "token/"

# authenticate and get the crt Token to be used later
request = requests.post(API_ENDPOINT + api_url, data=credentials, verify=False)


# store Token
token = json.loads(request.text)['token']

# display success message
print("Authenticated with Token, ", token)

# build the header dict to be passed with any request that requires authentication
headers = { 'Authorization' : 'Token ' + token }

# send revenue report
# revenue report data  # alternative way to get the data is to access the database through another api call in the branch office
data ={
        "date": 1616242925,
        "revenu": 3000,
        "loses": 3000,
        "Branch": 1
      }

# revenue url
api_url = 'send-revenue/'

# send the report using POST
request = requests.post(url = API_ENDPOINT + api_url, headers=headers, data = data)

# print response
print(json.loads(request.text))