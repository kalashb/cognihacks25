import streamlit as st
from intense_study import intense_study_mode
from casual_study import casual_study_mode
from casual_browsing import casual_browsing_mode
from meditation import meditation_mode
from puzzles import puzzles_mode

st.title("Focus Mode Selector")

mode = st.sidebar.radio(
    "Choose your mode:",
    [
        "Intense Study Mode",
        "Casual Study Mode",
        "Casual Browsing",
        "Meditate",
        "Brain Puzzles"
    ]
)

if mode == "Intense Study Mode":
    intense_study_mode()
elif mode == "Casual Study Mode":
    casual_study_mode()
elif mode == "Casual Browsing":
    casual_browsing_mode()
elif mode == "Meditate":
    meditation_mode()
elif mode == "Brain Puzzles":
    puzzles_mode()