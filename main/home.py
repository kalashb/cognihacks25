import streamlit as st

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
    st.header("Intense Study Mode")
    st.write("Maximize your focus. All distractions are minimized.")
elif mode == "Casual Study Mode":
    st.header("Casual Study Mode")
    st.write("Study at your own pace with light background music.")
elif mode == "Casual Browsing":
    st.header("Casual Browsing")
    st.write("Relax and browse content freely.")
elif mode == "Meditate":
    st.header("Meditate")
    st.write("Take a break and meditate. Breathe in, breathe out.")
elif mode == "Brain Puzzles":
    st.header("Brain Puzzles")
    st.write("Challenge yourself with fun brain puzzles!")