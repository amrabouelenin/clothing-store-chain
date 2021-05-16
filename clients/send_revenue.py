# importing the requests library
import requests, json
from get_revenue import GetRevenue
from datetime import date
## Read the day of today amount
########################################### RUN DAILY cron.daily #####################################
# inistanitiate service
G = GetRevenue()

# call service
G.get_reveneu()

# store data to be sent
data = G.data

## handle Fault Tolerence
try:

    # First authenticate in order to use the required APIs, then call the targeted service api

    # API Endpoint
    API_ENDPOINT = "http://127.0.0.1:8001/api/"

    # Credentials of api user
    credentials = { 'username' : 'testapi', 'password' : 'testapi' }

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

    # revenue url
    api_url = 'send-revenue/'

    # send the report using POST
    request = requests.post(url = API_ENDPOINT + api_url, headers=headers, data = data)

    # print response
    print(json.loads(request.text))

    calls_data =   {
        "status": True,
        "expected_date": date.today(),
        "actual_date": date.today(),
        "comments": "ran succesfully",
        "revenue": G.data['revenu'],
        "loss": G.data['loses']
    }

    message = G.set_request_status(calls_data)

    # message = G.set_request_status(calls_data)
    print("Headquarter is up",message)
except:
    ## add status record equal zero

    calls_data =   {
        "status": False,
        "expected_date": date.today(),
        "actual_date": None,
        "comments": "didn't run",
        "revenue": G.data['revenu'],
        "loss": G.data['loses']
    }

    message = G.set_request_status(calls_data)
    print("Headquarter is down",message)
    pass