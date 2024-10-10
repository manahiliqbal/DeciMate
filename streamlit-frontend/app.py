import streamlit as st
import requests

# Set Flask backend URL
FLASK_BACKEND_URL = "http://127.0.0.1:5000"

st.title("DeciMate: AI Assistant for Reducing Decision Fatigue")
st.subheader("Meal Planning")


preferences = st.text_input("Enter your meal preferences (e.g., vegetarian, spicy, etc.):")
recent_meals = st.text_input("Enter recent meals you had this week:")

# Button to trigger API request
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
        
st.subheader("Outfit Planning")


city = st.text_input("Enter your city:")
occasion = st.text_input("Enter the occasion (e.g., casual, formal):")

# Outfit Suggestion
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


st.subheader("Task Prioritization")


tasks = st.text_area("Enter your tasks (one per line):")
# Task Prioritization
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

        
