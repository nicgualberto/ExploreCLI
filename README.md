# 🌤️ ExploreCLI – Weather Forecast via Command Line

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/Weather_API-4FC3F7?style=for-the-badge)
![CLI](https://img.shields.io/badge/CLI-000000?style=for-the-badge&logo=gnubash&logoColor=white)

**ExploreCLI** is a simple and interactive command-line application that allows users to check the current temperature of any city using the **WeatherAPI**.

The project focuses on practicing API consumption, environment variables, and user interaction via terminal.

---

## ✨ Features

- 🌍 Get real-time temperature by city name
- 🔑 Secure API key management using `.env`
- 📡 API consumption with `requests`
- 🧠 Error handling for invalid cities or API issues
- 🔄 Continuous execution until user exits

---

## 🧠 How It Works

1. The user runs the application in the terminal
2. The program asks for a city name
3. A request is sent to WeatherAPI
4. The current temperature (°C) is displayed
5. The process repeats until the user types `exit`

---

## 🚀 Getting Started

### Requirements
- Python 3.8+
- WeatherAPI account (free tier works)

---

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/nicgualberto/ExploreCLI.git
    cd ExploreCLI
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
- Windows:
  ```bash
  venv\Scripts\activate
- Linux / macOS:
  ```bash
  source venv/bin/activate
- Install dependencies
  ```bash
  pip install -r requirements.txt

## Environment Configuration

- Create a `.env` file in the project root and add your API key:
- `WEATHER_API_KEY=your_api_key_here`
- ⚠️ Important:
Do not share your API key publicly. The `.env` file should be included in `.gitignore`.

## Running the Application
  `python main.py`
- Example interaction:
  `ExploreCLI
Enter the city name to check the temperature (type "exit" to quit): São Paulo
Current temperature in São Paulo: 24°C
`

## 🛠️ Technologies Used
- Python
- Requests
- WeatherAPI
- python-dotenv
- Command Line Interface (CLI)

## 📚 What I Learned

- Consuming external APIs with Python
- Managing environment variables securely
- Handling JSON responses and errors
- Designing interactive CLI applications
- Writing cleaner and more organized code

## 🎯 Project Purpose
- This project was developed for learning and portfolio purposes, focusing on backend fundamentals and API integration using Python.
