from flask import Flask, render_template

app = Flask(__name__)
import requests

# def get_weather(city_name, api_key):
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city_name,
#         "appid": api_key,
#         "units": "metric"  # Use "imperial" for Fahrenheit
#     }

#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()  # Raise an HTTPError for bad responses
#         data = response.json()

#         # Extract weather details
#         weather = {
#             "city": data["name"],
#             "temperature": data["main"]["temp"],
#             "description": data["weather"][0]["description"],
#             "humidity": data["main"]["humidity"],
#             "wind_speed": data["wind"]["speed"]
#         }
#         return weather

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching weather data: {e}")
#         return None

# if __name__ == "__main__":
#     API_KEY = "1132c42b947133a83aeb7b5c2d94c376"
#     city = input("Enter city name: ")
#     weather = get_weather(city, API_KEY)

#     if weather:
#         print(f"City: {weather['city']}")
#         print(f"Temperature: {weather['temperature']}°C")
#         print(f"Description: {weather['description']}")
#         print(f"Humidity: {weather['humidity']}%")
#         print(f"Wind Speed: {weather['wind_speed']} km/h")


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
