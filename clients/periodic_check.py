# Check which service calls failed and try to rerun them again.

# This script is running every hours/minutes according to our preference  cron.hourly / cron.minutes

########################################### RUN cron.hourly / cron.minutes #####################################

# Script is doing the following:
### read the service calls table
### check for services calls with status zero
### for every call do the following
###### call the send revenue service
######### if it works
############# set the status of this service call to 1 / True
######### else:
############# do nothing
from datetime import date
import requests, json
# get services calls from table
url = "http://127.0.0.1:8000/api/list/servicescalls/"
request  = requests.get(url)
services_calls = json.loads(request.text)
#print(services_calls)
for call in services_calls:
    if call['status'] == 0:
        ## call the service
        data = {
            'Branch': 1,
            'date':call['expected_date'],
            'revenu' : call['revenue'],
            'loses': call['loss'],
        }

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

            # update this calls and set it = 1
            SERVICECALLAPI = "http://127.0.0.1:8000/api/servicecall-update/" + str(call['id']) +  str("/")
            data =     {
                "id": call['id'],
                "status": True,
                "expected_date": call['expected_date'],
                "actual_date": str(date.today()),
                "comments": "Run successuflly",
                "revenue": call['revenue'],
                "loss": call['loss']
            }
            
            request = requests.post(url = SERVICECALLAPI, data = data)
            print(json.dumps(data))
            print(json.loads(request.text))
            #print(request.text)
        except Exception as e:
            print(e)
            # do nothing as there will be another try later from the same service
            print('server is down')
            pass