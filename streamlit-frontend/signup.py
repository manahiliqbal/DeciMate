import streamlit as st
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import app  

# MongoDB connection
client = MongoClient("mongodb+srv://manahil0511:cHgNWcu0egmGNHAJ@cluster0.mh5yv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['myDatabase']  
users_collection = db['users']

# CSS for styling
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <style>
    .stApp {
        background: linear-gradient(135deg, #8A00D4, #D464FF, #38B6FF, #AC00D4);  
        background-size: 400% 400%;
        animation: gradientAnimation 20s ease infinite;
        font-family: 'Orbitron', sans-serif;
    }
    input[type="text"], input[type="password"] {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 2px solid #38B6FF !important;
        border-radius: 5px !important;
        padding: 10px !important;
        color: #AC00D4 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 14px !important;
        outline: none !important;
    }
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
    h1, h2, h3, p {
        font-family: 'Orbitron', sans-serif; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for login status
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Function to handle logout
def logout():
    st.session_state.authenticated = False
    # Simulate rerun by setting a query param to trigger a rerun
    st.experimental_set_query_params(logged_out="1")

# Function to refresh content based on login status
def reroute_content():
    if st.session_state.authenticated:
        app.show_main_app()  # This will display the content from app.py
        st.button("Logout", on_click=logout)
    else:
        # Show the signup/login page
        show_login_signup_page()

# Show content based on login status
def show_login_signup_page():
    # Tabs for Signup and Login
    tab1, tab2 = st.tabs(["Signup", "Login"])

    # Signup Form
    with tab1:
        st.subheader("Create a new account")
        signup_username = st.text_input("Username")
        signup_password = st.text_input("Password", type="password")
        signup_confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Signup"):
            if signup_password == signup_confirm_password:
                hashed_password = generate_password_hash(signup_password)

                if users_collection.find_one({"username": signup_username}):
                    st.error("Username already exists!")
                else:
                    users_collection.insert_one({
                        "username": signup_username,
                        "password": hashed_password
                    })
                    st.success("Account created successfully!")
            else:
                st.error("Passwords do not match!")

    # Login Form
    with tab2:
        st.subheader("Login to your account")
        login_username = st.text_input("Enter Username")
        login_password = st.text_input("Enter Password", type="password")

        if st.button("Login"):
            user = users_collection.find_one({"username": login_username})
            
            if user:
                if check_password_hash(user['password'], login_password):
                    st.success(f"Welcome, {login_username}!")
                    st.session_state.authenticated = True
                    # Simulate rerun by setting a query param to trigger a rerun
                    st.experimental_set_query_params(logged_in="1")
                else:
                    st.error("Invalid password.")
            else:
                st.error("Username does not exist.")

# Main content based on authentication
if st.session_state.authenticated:
    app.show_main_app()  
    st.button("Logout", on_click=logout)
else:
    reroute_content()
