from flask import Flask, request, jsonify
import jwt  
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

# Load MongoDB URI from config.py
app.config.from_pyfile('config.py')

# Use MongoClient directly
client = MongoClient(app.config['MONGO_URI'])

# Get the database (explicitly specify the database name)
db = client['myDatabase']  # Replace <dbname> with your actual database name
print("Database object:", db)

# Collection for users
users_collection = db['users']

# Check if connection is successful
try:
    client.server_info()  # Will throw an exception if the connection fails
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if users_collection.find_one({"username": username}):
        return jsonify({"message": "User already exists!"}), 400
    
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"username": username, "password": hashed_password})
    
    return jsonify({"message": "User created successfully!"}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    user = users_collection.find_one({"username": username})
    
    if user and check_password_hash(user["password"], password):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401


# Initialize OpenAI with the API key
api_key = app.config['OPENAI_API_KEY']

# Middleware: JWT Verification for Clerk.js
@app.before_request
def verify_token():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split()[1]  # Bearer <token>
        try:
            # Decode the token (optional: use Clerk's public keys for signature verification)
            decoded_token = jwt.decode(token, options={"verify_signature": False})
            request.user = decoded_token
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token.'}), 401
    else:
        return jsonify({'message': 'Authorization header missing.'}), 401

# Route: Home 
@app.route('/')
def home():
    return {'message': 'Flask backend is running.'}, 200

# Example of a protected route
@app.route('/protected', methods=['GET'])
def protected_route():
    user = request.user  # Access the authenticated user
    return {'message': f'Hello {user["email"]}, you have access to this route.'}, 200

# Route: Meal Planning (AI-based suggestions)
@app.route('/meal', methods=['POST'])
def meal_planning():
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

# Route: Task Prioritization (AI-based suggestions)
@app.route('/tasks', methods=['POST'])
def task_prioritization():
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

# Helper Function: Get Weather Data
def get_weather(city):
    api_key = app.config['OPENWEATHER_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return response['main']['temp']

# Route: Outfit Suggestions (AI-based suggestions based on weather and occasion)
@app.route('/outfit', methods=['POST'])
def outfit_planning():
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

if __name__ == '__main__':
    app.run(debug=True)
