import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_customer_emails(self):
        customers_endpoint = "https://api.sheety.co/984b8d92a2e866f72d841ab32caf58d7/flightDeals/users"
        headers = {
            "Authorization": "Basic YXJhdmluZDI2MTA6QEFyYXZpbmQyNg=="
        }
        response = requests.get(customers_endpoint,headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data





