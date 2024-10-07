from flask import Flask, render_template, request
from openai import OpenAI
import requests

app = Flask(__name__)

# Load your API keys from config.py
app.config.from_pyfile('config.py')

# Initialize OpenAI with the API key
api_key = app.config['OPENAI_API_KEY']

# Route: Home
@app.route('/')
def home():
    return render_template('index.html')

# Route: Meal Planning
@app.route('/meal', methods=['GET', 'POST'])
def meal_planning():
    if request.method == 'POST':
        preferences = request.form['preferences']
        recent_meals = request.form['recent_meals']
        response = requests.post(
        "https://api.aimlapi.com/chat/completions",  # Replace with the correct endpoint
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "model": "gpt-4",  # Make sure the model is correct
            "messages": [
                {"role": "system", "content": "You are a helpful assistant for meal planning."},
                {"role": "user", "content": f"Suggest a dinner based on these preferences: {preferences}. The user has eaten {recent_meals} this week."}
            ]
        }
    )
        data = response.json()
        
        # Extracting suggestion from API response
        try:
            suggestion = data['choices'][0]['message']['content']
        except KeyError:
            suggestion = "Sorry, I couldn't generate a suggestion."

        return render_template('meal.html', suggestion=suggestion)

    return render_template('meal.html')


@app.route('/tasks', methods=['GET', 'POST'])
def task_prioritization():
    if request.method == 'POST':
        tasks = request.form['tasks']  
        
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

        return render_template('tasks.html', prioritization=prioritization)

    return render_template('tasks.html')


# Route: Outfit Suggestions
@app.route('/outfit', methods=['GET', 'POST'])
def outfit_planning():
    if request.method == 'POST':
        city = request.form['city']
        occasion = request.form['occasion']
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

        return render_template('outfit.html', outfit=outfit)

    return render_template('outfit.html')


# Helper Function: Get Weather Data
def get_weather(city):
    api_key = app.config['OPENWEATHER_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return response['main']['temp']

if __name__ == '__main__':
    app.run(debug=True)
