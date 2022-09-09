import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN" : TOKEN
}

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "walking graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today_date = datetime.now().strftime('%Y%m%d')


pixel_data = {
    "date": f"{today_date}",
    "quantity": input("how many Kms have you walked today? ")
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20220318"

update_data = {
    "quantity": "5.23"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=update_data, headers=headers)
# print(response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20220317"

# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)