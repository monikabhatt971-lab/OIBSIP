# Oasis Infobyte Internship - Task 4:Basic Weather App
# created by: Monika Bhatt

import requests

def get_weather():
    print("--- Basic Weather App ---")

    API_KEY = "4518dcc18d89776f5302ac7d7f031001"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    city = input("Enter City Name:")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            print("\nWeather Details")
            print("city:",data["name"])
            print("Temperature:",data["main"]["temp"],"°C")
            print("Humidity:",data["main"]["humidity"],"%")
            print("Condition:",data["weather"][0]["description"])

        elif response.status_code == 404:
            print("City not found!")

        else:
            print("Status Code:", response.status_code)
            print(response.text)

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")

if __name__== "__main__":
    get_weather()