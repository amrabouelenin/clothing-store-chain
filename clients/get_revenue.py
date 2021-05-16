# importing the requests library
import requests, json

## Read the day of today amount

### to read the data, an api service needs to be exist
### make the api service do all the required operation before transfering to headquarter


# ### to read the data, an api service needs to be exist
# ### make the api service do all the required operation before transfering to headquarter

# request  = requests.get(BranchENDPOINT)

# data = json.loads(request.text)

## wrap it in json data
## send it to the headquarter
## if it succeeded add record in the database of branch that it works

class GetRevenue():

    def __init__(self):
        self.ENDPOINT = "http://127.0.0.1:8000/api/transactions_today"
        self.SERVICECALLAPI = "http://127.0.0.1:8000/api/add/servicecall"
        self.data = {}
    
    def get_reveneu(self):
        # request the transcation today service
        request  = requests.get(self.ENDPOINT)
        self.data = json.loads(request.text)
    
    def set_request_status(self, data):
        request = requests.post(url = self.SERVICECALLAPI, data = data)
        return json.loads(request.text)

    
