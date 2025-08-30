import streamlit as st

def show_home():
    st.write("Curious about how your brain works when you're solving different problems?")
    st.write("Raven's Progressive Matrices are a great way to explore this!")
    st.write("With a BCI, you can even see how your brain activity changes!!!")
    st.write("Happy puzzling!")

def show_menu():
    return st.sidebar.radio("Menu", ["Home", "Numerical", "Traditional"], key="main_menu")