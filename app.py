from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API KEY NOT FOUND. Check your .env file")

# ---------------- WEATHER TYPE (FOR CSS ANIMATION) ----------------
def get_weather_type(condition):
    condition = condition.lower()
    
    if "clear" in condition:
        return "sunny"
    elif "rain" in condition or "drizzle" in condition:
        return "rainy"
    elif "snow" in condition or "cold" in condition or "sleet" in condition:
        return "cold"
    elif "thunder" in condition or "storm" in condition:
        return "thunder"
    elif "cloud" in condition or "overcast" in condition or "mist" in condition or "haze" in condition or "fog" in condition:
        return "cloudy"
    else:
        return "cloudy"

# ---------------- MAIN ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    forecast = []
    weather_type = None
    error = None

    if request.method == "POST":
        city = request.form["city"]

        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        forecast_url = (
            f"https://api.openweathermap.org/data/2.5/forecast"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        weather_res = requests.get(weather_url)
        forecast_res = requests.get(forecast_url)

        # ---------- CURRENT WEATHER ----------
        if weather_res.status_code == 200:
            data = weather_res.json()

            weather = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temp": round(data["main"]["temp"], 1),
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "condition": data["weather"][0]["description"].capitalize()
            }

            weather_type = get_weather_type(weather["condition"])

            # ---------- 5-DAY FORECAST (12:00 PM DATA) ----------
            if forecast_res.status_code == 200:
                forecast_data = forecast_res.json()["list"]

                for item in forecast_data:
                    # Pick mid-day temperature (more accurate)
                    if "12:00:00" in item["dt_txt"]:
                        date = item["dt_txt"].split(" ")[0]

                        forecast.append({
                            "day": datetime.strptime(date, "%Y-%m-%d").strftime("%A"),
                            "temp": round(item["main"]["temp"], 1),
                            "condition": item["weather"][0]["description"].capitalize()
                        })

                        if len(forecast) == 5:
                            break
        else:
            error = "City not found or API error"

    return render_template(
        "index.html",
        weather=weather,
        forecast=forecast,
        weather_type=weather_type,
        error=error
    )

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)