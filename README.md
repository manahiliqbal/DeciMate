# DeciMate: an AI Assistant for Reducing Decision Fatigue
App is live at: https://decimate.streamlit.app/

This project was made as a part of the **Reasoning with o1 Hackathon** by *lablab.ai*

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
- **MongoDB**: User data, pis stored and managed using MongoDB. The database stores login and signup information.
  
4. *Machine Learning*:
- The AI leverages *simple recommendation algorithms* based on user feedback and past behaviors, improving over time through usage.
  
5. *APIs*:
- **Weather API**: To provide context-based outfit recommendations depending on the daily weather.


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
