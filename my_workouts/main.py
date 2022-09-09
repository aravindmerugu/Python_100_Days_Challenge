from datetime import datetime
import requests
import os

APP_ID = os.environ["APP_ID"]
API_KEY="YOUR_API_KEY"

GENDER = "male"
WEIGHT_KG = "55"
HEIGHT_CM = "165"
AGE = "23"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
# print(result["exercises"][0]["user_input"])
# print(result["exercises"][1]["user_input"])
# print(result["exercises"][1]["duration_min"])
# print(result["exercises"][1]["nf_calories"])

SHEETY_ENDPOINT = "https://api.sheety.co/984b8d92a2e866f72d841ab32caf58d7/myWorkout/workouts"
sheet_header = {
    "Authorization": "Basic YXJhdmluZDpAQXJhdmluZDI2"
}

datetime = datetime.now()
date = datetime.strftime("%d/%m/%Y")
time = datetime.strftime("%H:%M:%S")

for workout in result["exercises"]:
    WORKOOUT_DATA = {
        "workout": {
            "date": date,
            "time": time,
            "exercise":workout["user_input"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=WORKOOUT_DATA, headers=sheet_header)
    print(response.text)
    response.raise_for_status()