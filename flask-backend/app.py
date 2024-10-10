from flask import Flask, render_template, request
from openai import OpenAI
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  

# Load your API keys from config.py
app.config.from_pyfile('config.py')

# Initialize OpenAI with the API key
api_key = app.config['OPENAI_API_KEY']

# Route: Home (Health check)
@app.route('/')
def home():
    return {'message': 'Flask backend is running.'}, 200

# Route: Meal Planning
@app.route('/meal', methods=['GET', 'POST'])
def meal_planning():
    if request.method == 'POST':
        data = request.json  
        preferences = data.get('preferences', '')
        recent_meals = data.get('recent_meals', '')
        response = requests.post(
        "https://api.aimlapi.com/chat/completions",  
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "model": "gpt-4",  
            "messages": [
                {"role": "system", "content": "You are a helpful assistant for meal planning."},
                {"role": "user", "content": f"Suggest a dinner based on these preferences: {preferences}. The user has eaten {recent_meals} this week."}
            ]
        }
    )
        data = response.json()
        try:
            suggestion = data['choices'][0]['message']['content']
        except KeyError:
            suggestion = "Sorry, I couldn't generate a suggestion."

        return {'suggestion': suggestion}, 200



@app.route('/tasks', methods=['GET', 'POST'])
def task_prioritization():
    if request.method == 'POST':
        data = request.json 
        tasks = data.get('tasks', '')
        
        response = requests.post(
            "https://api.aimlapi.com/chat/completions", 
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"  
            },
            json={
                "model": "gpt-4",  
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant for task prioritization."},
                    {"role": "user", "content": f"Here is the list of tasks: {tasks}. Prioritize them based on urgency and importance."}
                ]
            }
        )
        
        data = response.json()
        try:
            prioritization = data['choices'][0]['message']['content']
        except KeyError:
            prioritization = "Sorry, I couldn't prioritize the tasks."

        return {'prioritization': prioritization}, 200


# Route: Outfit Suggestions
@app.route('/outfit', methods=['GET', 'POST'])
def outfit_planning():
    if request.method == 'POST':
        data = request.json 
        city = data.get('city', '')
        occasion = data.get('occasion', '')
        weather = get_weather(city)
        
        response = requests.post(
            "https://api.aimlapi.com/chat/completions",  
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"  
            },
            json={
                "model": "gpt-4",  
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant for outfit planning."},
                    {"role": "user", "content": f"Suggest an outfit for {occasion} based on the weather of {weather}°C in {city}."}
                ]
            }
        )
        data = response.json()

        try:
            outfit = data['choices'][0]['message']['content']
        except KeyError:
            outfit = "Sorry, I couldn't suggest an outfit."

        return {'outfit': outfit}, 200


# Helper Function: Get Weather Data
def get_weather(city):
    api_key = app.config['OPENWEATHER_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return response['main']['temp']

if __name__ == '__main__':
    app.run(debug=True)
