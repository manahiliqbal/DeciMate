# Decimate: an AI Assistant for Reducing Decision Fatigue

Project Overview

This project is an AI-powered assistant designed to reduce *decision fatigue* by automating and streamlining repetitive daily decisions. For the purpose of this hackathon, the assistant focuses on three core areas:
- *Outfit Planning*
- *Meal Planning*
- *Task Prioritization*

The assistant analyzes user preferences, behaviors, and context (e.g., weather, calendar, available ingredients) to offer personalized suggestions, helping users avoid the mental load of small daily decisions. By integrating these modules into one cohesive system, the AI aims to improve the user's productivity and reduce stress.

Key Features

1. *Outfit Planning*: The AI suggests daily outfit combinations based on the user's preferences, weather conditions, and calendar events (e.g., professional or casual attire depending on meetings).
   
2. *Meal Planning*: The assistant offers meal suggestions based on dietary preferences, available ingredients, and past choices. It can generate a grocery list if needed.
   
3. *Task Prioritization*: The AI helps users organize and prioritize their daily tasks by analyzing deadlines, importance, and time available. It suggests which tasks to focus on and when to take breaks.

### Use Case

The AI assistant is designed for busy individuals who experience decision fatigue due to daily repetitive choices, such as:
- *Professionals* balancing work tasks and personal life.
- *Parents* juggling family responsibilities and self-care.
- *Students* needing help with task management, especially when schedules are packed with assignments.

By automating small decisions, users can free up mental space for more important tasks, stay organized, and make healthier, more efficient choices.


Tech Stack

1. *Backend*: 
- **Flask**: We use Flask to create a lightweight, flexible backend that serves the AI recommendations and manages user interactions.

2. *Frontend*: 
- **Streamlit**: We use Streamlit to create a bright playful frontend that displays the AI recommendations and manages user experience.
  
3. *Database*:
- **PostgreSQL**: User data, preferences, and patterns are stored and managed using PostgreSQL. The database stores information about past decisions, outfits, meals, and tasks for personalized recommendations.
  
4. *Machine Learning*:
- The AI leverages *simple recommendation algorithms* based on user feedback and past behaviors, improving over time through usage.
  
5. *APIs*:
- **Weather API**: To provide context-based outfit recommendations depending on the daily weather.
- **Calendar API**: To help the AI analyze the user's schedule and provide task prioritization and outfit suggestions based on upcoming events.



Installation and Setup

1. Clone the repository
```bash
git clone https://github.com/your-repo/ai-decision-assistant.git
cd ai-decision-assistant
```

2. Set up virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database
- Install PostgreSQL if not already installed.
- Create a new PostgreSQL database and user.
- Update the `config.py` file with your PostgreSQL database credentials.
  
```bash
# config.py
SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost/<database>'
```

5. Set up environment variables (optional)
Create a `.env` file to store sensitive environment variables like API keys for weather integration.

```bash
WEATHER_API_KEY=your-weather-api-key
CALENDAR_API_KEY=your-calendar-api-key
```

#### 6. Initialize the database
```bash
flask db init
flask db migrate
flask db upgrade
```

7. Run the Flask app
```bash
flask run
```

---

Usage Instructions

1. *Initial Setup*: 
   - When the user first interacts with the assistant, they'll be asked to input their preferences for meals (dietary restrictions, favorite meals), outfit styles, and task management priorities (e.g., deadlines, project importance).
   
2. *Daily Interaction*: 
   - The user can ask the assistant for a meal suggestion, outfit recommendation, or task prioritization. The assistant will offer suggestions based on context and past behaviors.

3. *Personalization and Feedback*: 
   - The AI learns over time by tracking user responses and preferences, allowing for more refined and accurate suggestions as the user continues to interact.



API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/outfit`    | Get daily outfit recommendation based on user preferences and weather. |
| `GET`  | `/meal`      | Get a meal suggestion based on preferences and available ingredients. |
| `GET`  | `/tasks`     | Get a prioritized task list based on deadlines and importance. |
| `POST` | `/feedback`  | Submit feedback on suggestions to improve future recommendations. |


Future Improvements

This project is designed as a proof of concept for the hackathon. In the future, we plan to:
- Implement *more advanced recommendation algorithms* using machine learning to improve decision accuracy over time.
- Expand the assistant to handle more decision areas like *fitness routines* or *social event planning*.

Conclusion

This AI assistant helps users reduce cognitive load by automating repetitive decisions in their daily lives. Through machine learning, personalized recommendations, and feedback loops, it continuously learns from user behaviors to optimize its suggestions. With the current focus on *outfit planning*, *meal planning*, and *task prioritization*, this project is a strong starting point for building a comprehensive tool that reduces decision fatigue and improves productivity.


Contributors

- **Manahil Iqbal**
- **Hareem Fatima**

Feel free to reach out with any questions or feedback!
