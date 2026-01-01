# 🌦️ Weather App (Flask)

A simple and beginner-friendly **Weather Forecast Web Application** built using **Flask**.  
The app fetches real-time weather data from a weather API and displays current conditions like temperature, weather status, and description for any city.

---

## 📁 Project Structure
```
weather_app/
│
├── static/     # CSS files, images, and icons
├── templates/  # HTML templates (Jinja2)
│
├── .env        # Environment variables (API key)
├── .gitignore  # Files and folders ignored by Git
├── app.py      # Main Flask application file
├── requirements.txt   # Project dependencies
```

---

## 🚀 Features

- 🌍 Search weather by city name  
- 🌡️ Shows temperature and weather condition  
- ☀️ Weather icons based on condition (sun, cloud, rain, snow, thunder)  
- 🎨 Clean and simple user interface  
- 🔐 API key stored securely using `.env` file  

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**
- **Weather API**
- **python-dotenv**

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/codebyrks/Weather-App-flask.git
```

## 2️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```
## 3️⃣ Configure Environment Variables
  Create a .env file in the root directory and add:
  ```bash
  API_KEY=your_weather_api_key_here
  ```
## 4️⃣ Run the Flask App
```bash
python app.py
```
Your Weather App should run properly.
---
