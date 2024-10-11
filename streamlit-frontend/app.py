import streamlit as st
import requests

# Define the Flask backend URL
FLASK_BACKEND_URL = "http://127.0.0.1:5000"  # Adjust this if the Flask backend is running elsewhere

def show_main_app():
    # Gradient background and styling
    st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">

    <style>
    /* Gradient background and font styling */
    .stApp{
        background: linear-gradient(135deg, #8A00D4, #D464FF, #38B6FF, #AC00D4);  
        background-size: 400% 400%;
        animation: gradientAnimation 20s ease infinite;
        font-family: 'Orbitron', sans-serif; 
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Styling input fields */
    input[type="text"], textarea {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 2px solid #38B6FF !important;
        border-radius: 5px !important;
        padding: 10px !important;
        color: #AC00D4 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 14px !important;
        outline: none !important;
    }
    
    input[type="text"]::placeholder, textarea::placeholder {
        color: rgba(255, 255, 255, 0.7);
    }

    input[type="text"]:focus, textarea:focus {
        border-color: #D464FF;
        box-shadow: 0 0 10px #D464FF;
    }

    /* Styling buttons */
    div.stButton > button {
        background-color: #D464FF;
        color: white;
        border: 2px solid #38B6FF;
        padding: 10px 20px;
        font-family: 'Orbitron', sans-serif;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #D464FF;
        box-shadow: 0 0 20px #38B6FF;
    }

    div.stButton > button:active {
        background-color: #38B6FF;
        box-shadow: 0 0 10px #D464FF inset;
    }

    .main .block-container {
        background: transparent !important;
        padding: 20px;
    }

    h1, h2, h3, p, li {
        font-family: 'Orbitron', sans-serif; 
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Main app title
    st.title("DeciMate: AI Assistant for Reducing Decision Fatigue")

    # Meal Planning Section
    st.subheader("Meal Planning")

    preferences = st.text_input("Enter your meal preferences (e.g., vegetarian, spicy, etc.):")
    recent_meals = st.text_input("Enter recent meals you had this week:")

    if st.button("Get Meal Suggestion", key="meal_suggestion_button"):
        if preferences and recent_meals:
            response = requests.post(
                f"{FLASK_BACKEND_URL}/meal",
                json={'preferences': preferences, 'recent_meals': recent_meals}  
            )
            if response.status_code == 200:
                suggestion = response.json().get('suggestion', 'No suggestion found.')
                st.write(f"Suggested meal: {suggestion}")
            else:
                st.error("Error fetching meal suggestion. Please try again.")
        else:
            st.error("Please fill in both fields.")

    # Outfit Planning Section
    st.subheader("Outfit Planning")

    city = st.text_input("Enter your city:")
    occasion = st.text_input("Enter the occasion (e.g., casual, formal):")

    if st.button("Get Outfit Suggestion", key="outfit_suggestion_button"):
        if city and occasion:
            response = requests.post(
                f"{FLASK_BACKEND_URL}/outfit",
                json={'city': city, 'occasion': occasion}  
            )
            if response.status_code == 200:
                outfit = response.json().get('outfit', 'No outfit suggestion found.')
                st.write(f"Suggested outfit: {outfit}")
            else:
                st.error("Error fetching outfit suggestion. Please try again.")
        else:
            st.error("Please fill in both fields.")

    # Task Prioritization Section
    st.subheader("Task Prioritization")

    tasks = st.text_area("Enter your tasks (one per line):")

    if st.button("Prioritize Tasks", key="task_prioritization_button"):
        if tasks:
            response = requests.post(
                f"{FLASK_BACKEND_URL}/tasks",
                json={'tasks': tasks}  
            )
            if response.status_code == 200:
                prioritization = response.json().get('prioritization', 'No prioritization found.')
                st.write(f"Task prioritization: {prioritization}")
            else:
                st.error("Error prioritizing tasks. Please try again.")
        else:
            st.error("Please enter the tasks.")

        