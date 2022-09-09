from pprint import pprint
import requests
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

SHEETY_ENDPOINT = "https://api.sheety.co/984b8d92a2e866f72d841ab32caf58d7/flightDeals/prices"

headers = {
    "Authorization" : "Basic YXJhdmluZDI2MTA6QEFyYXZpbmQyNg=="
}

response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
data = response.json()["prices"]

pprint(data)

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
teqila_api = "YOUR_TEQUILLA_API_KEY"

for row in data:
    if row['iataCode'] =="":
        tequila_headers = {
            "apikey": teqila_api,
        }
        params = {
            "term": row['city']
        }
        flight_response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=tequila_headers)
        print(flight_response)
        city_code = flight_response.json()["locations"][0]["code"]

        SHEETY_PUT_ENDPOINT = f"https://api.sheety.co/984b8d92a2e866f72d841ab32caf58d7/flightDeals/prices/{row['id']}"
        body = {
            "price" : {
                'iataCode': city_code,
            }
        }
        put_response = requests.put(url=SHEETY_PUT_ENDPOINT, json=body, headers=headers)
        print(put_response.text)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)


