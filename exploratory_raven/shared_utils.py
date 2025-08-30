import streamlit as st

def show_feedback_and_nav(was_correct, correct_letter, answered, on_submit, on_next):
    """
    Modular feedback and navigation logic for Raven's Matrices.
    - was_correct: bool or None
    - correct_letter: str
    - answered: bool
    - on_submit: function to call on submit
    - on_next: function to call on next
    """
    if not answered:
        st.button("Submit", on_click=on_submit)
    else:
        if was_correct:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Correct answer was {correct_letter}.")
        st.button("Next", on_click=on_next)

def run_puzzles_streamlit(puzzles, show_menu, show_home, display_matrix_streamlit, show_feedback_and_nav):
    st.title("Raven Matrisees")
    menu = show_menu()

    if menu == "Home":
        show_home()
        return
    elif menu == "Traditional":
        st.header("Traditional Raven's Matrices")
        st.write("Work in progress. Images coming soon!")
        return
    # Numerical mode below

    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'current' not in st.session_state:
        st.session_state.current = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = False
    if 'was_correct' not in st.session_state:
        st.session_state.was_correct = None

    p = puzzles[st.session_state.current] if st.session_state.current < len(puzzles) else None
    option_labels = []
    if p:
        options = p['options']
        option_labels = [f"{chr(65+i)}: {val}" for i, val in enumerate(options)]

    def submit_callback():
        choice = st.session_state.get(f"choice_{st.session_state.current}")
        if choice is not None and p:
            selected = option_labels.index(choice)
            if selected == p['answer']:
                st.session_state.score += 1
                st.session_state.was_correct = True
            else:
                st.session_state.was_correct = False
            st.session_state.answered = True

    def next_callback():
        st.session_state.current += 1
        st.session_state.answered = False
        st.session_state.was_correct = None
        st.session_state[f"choice_{st.session_state.current}"] = None

    if st.session_state.current >= len(puzzles):
        st.success(f"Game Over! Your final score: {st.session_state.score}/{len(puzzles)}")
        if st.button("Restart"):
            st.session_state.score = 0
            st.session_state.current = 0
            st.session_state.answered = False
            st.session_state.was_correct = None
        return

    st.subheader(f"Puzzle {st.session_state.current+1}")
    display_matrix_streamlit(p['grid'])
    st.radio("Choose your answer:", option_labels, index=None, key=f"choice_{st.session_state.current}", horizontal=True)

    correct_letter = chr(65 + p['answer'])
    show_feedback_and_nav(
        st.session_state.was_correct,
        correct_letter,
        st.session_state.answered,
        submit_callback,
        next_callback
    )
