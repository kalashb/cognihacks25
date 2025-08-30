import streamlit as st

def show_main_menu():
    return st.sidebar.radio(
        "Choose your experience:",
        [
            "Intense Study Mode",
            "Casual Study Mode",
            "Casual Browsing",
            "Meditate",
            "Brain Puzzles"
        ],
        key="main_experience_menu"
    )

def show_home():
    st.title("Welcome to the Cognitive Experience App")
    st.write("Curious about how your brain works when you're solving different problems?")
    st.write("Choose a mode from the menu to get started!")