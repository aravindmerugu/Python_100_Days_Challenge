import requests
from twilio.rest import Client

api_key = "YOUR_API_KEY"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

parameters = {
    "lat":79.5833,
    "lon":18,
    "exclude":("current","minutely","daily"),
    "appid":api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_data=response.json()["hourly"][0:12]

for hour_data in weather_data:
    if hour_data["weather"][0]["id"]>800:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Awesome weather today, Have a nice day🤩",
            from_='+12185177821',
            to='+919182669603'
        )
        print(message.status)
        break