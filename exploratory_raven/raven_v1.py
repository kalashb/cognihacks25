import streamlit as st
from shared_utils import run_puzzles_streamlit, show_feedback_and_nav
from home import show_home, show_menu

###############################################
### Numerical puzzles
# We should def change these
###############################################
puzzles = [
    # 2x2 puzzles (1-10)
    {'grid': [[2, 4], [3, None]], 'options': [5, 6, 1, 7], 'answer': 0},
    {'grid': [[5, 7], [None, 11]], 'options': [8, 12, 9, 13], 'answer': 2},
    {'grid': [[1, 3], [None, 7]], 'options': [4, 5, 6, 8], 'answer': 1},
    {'grid': [[6, None], [9, 12]], 'options': [7, 8, 10, 11], 'answer': 1},
    {'grid': [[4, 8], [None, 16]], 'options': [6, 10, 12, 14], 'answer': 2},
    {'grid': [[3, None], [7, 11]], 'options': [5, 6, 8, 9], 'answer': 3},
    {'grid': [[7, 14], [None, 28]], 'options': [10, 12, 14, 16], 'answer': 1},
    {'grid': [[2, None], [6, 8]], 'options': [3, 4, 5, 7], 'answer': 1},
    {'grid': [[9, 6], [None, 3]], 'options': [0, 3, 6, 9], 'answer': 2},
    {'grid': [[8, None], [4, 2]], 'options': [1, 2, 3, 6], 'answer': 3},

    # 3x3 puzzles (11-20) — increased difficulty
    {'grid': [[1, 2, 6], [2, 6, 18], [6, 18, None]], 'options': [54, 36, 72, 48], 'answer': 0},
    {'grid': [[8, 1, 6], [3, 5, 7], [4, 9, None]], 'options': [2, 1, 3, 4], 'answer': 0},
    {'grid': [[1, 1, 2], [3, 5, 8], [13, 21, None]], 'options': [34, 33, 35, 31], 'answer': 0},
    {'grid': [[2, 3, 5], [7, 11, 13], [17, 19, None]], 'options': [21, 23, 25, 27], 'answer': 1},
    {'grid': [[1, 4, 9], [16, 25, 36], [49, 64, None]], 'options': [72, 81, 90, 100], 'answer': 1},
    {'grid': [[1, 3, 3], [1, 4, 6], [1, 5, None]], 'options': [9, 10, 11, 12], 'answer': 1},
    {'grid': [[2, 4, 8], [3, 9, 27], [5, 25, None]], 'options': [75, 100, 125, 150], 'answer': 2},
    {'grid': [[2, 6, 12], [4, 12, 24], [6, 18, None]], 'options': [30, 36, 42, 48], 'answer': 1},
    {'grid': [[1, 2, 3], [2, 4, 6], [3, 6, None]], 'options': [7, 8, 9, 10], 'answer': 2},
    {'grid': [[2, 4, 6], [8, 10, 12], [14, 16, None]], 'options': [16, 18, 20, 22], 'answer': 1},
]

def display_matrix(grid):
    """Prints a matrix with None as '?'."""
    for row in grid:
        print("\t".join(str(x) if x is not None else "?" for x in row))
    print()

def display_matrix_cli(grid):
    """Prints a matrix with None as '?' for CLI."""
    for row in grid:
        print("\t".join(str(x) if x is not None else "?" for x in row))
    print()

###############################################
### Matrix for numerical (allows 2x2 and 3x3)
###############################################
def display_matrix_streamlit(grid):
    """Displays a matrix in Streamlit as a styled HTML table."""
    table_html = "<style>\n.raven-matrix-table {\n  border-collapse: collapse;\n  margin: 10px 0;\n}\n.raven-matrix-table td {\n  width: 150px;\n  height: 150px;\n  text-align: center;\n  vertical-align: middle;\n  font-size: 1.6em;\n  font-family: 'Segoe UI', Arial, sans-serif;\n  color: #2563eb; /* neutral blue */\n  border: 1px solid #d1d5db;\n  background: #f8fafc;\n}\n.raven-matrix-table td.missing {\n  color: #64748b;\n  background: #e0e7ef;\n  font-style: italic;\n}\n</style>\n"
    table_html += "<table class='raven-matrix-table'>"
    for row in grid:
        table_html += "<tr>"
        for x in row:
            if x is None:
                table_html += "<td class='missing'>?</td>"
            else:
                table_html += f"<td>{x}</td>"
        table_html += "</tr>"
    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)


def run_puzzles_cli(puzzles):
    score = 0
    print("\nWelcome to the Raven-like Matrix Puzzles!\n")
    for idx, p in enumerate(puzzles, start=1):
        print(f"Puzzle {idx}:")
        display_matrix_cli(p['grid'])

        # Display options
        for opt_idx, val in enumerate(p['options'], start=1):
            print(f"  {chr(64+opt_idx)}: {val}")
        choice = input("Your answer (A-D): ").strip().upper()

        # Check the answer
        if ord(choice) - 65 == p['answer']:
            print("Correct!\n")
            score += 1
        else:
            correct_letter = chr(65 + p['answer'])
            print(f"Incorrect. Correct answer was {correct_letter}.\n")

    print(f"Your final score: {score}/{len(puzzles)}")


def run_puzzles_streamlit(puzzles,
            show_menu,
            show_home,
            display_matrix_streamlit,
            show_feedback_and_nav):
    
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

    def submit_callback():
        choice = st.session_state.get(f"choice_{st.session_state.current}")
        if choice is not None:
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

    p = puzzles[st.session_state.current]
    st.subheader(f"Puzzle {st.session_state.current+1}")
    display_matrix_streamlit(p['grid'])
    options = p['options']
    option_labels = [f"{chr(65+i)}: {val}" for i, val in enumerate(options)]
    # Horizontal radio buttons for answer options
    st.radio("Choose your answer:", option_labels, index=None, key=f"choice_{st.session_state.current}", horizontal=True)

    correct_letter = chr(65 + p['answer'])
    show_feedback_and_nav(
        st.session_state.was_correct,
        correct_letter,
        st.session_state.answered,
        submit_callback,
        next_callback
    )

# Run the puzzle session
if __name__ == "__main__":
    import sys
    if 'streamlit' in sys.argv:
        run_puzzles_streamlit(
            puzzles,
            show_menu,
            show_home,
            display_matrix_streamlit,
            show_feedback_and_nav
        )
    else:
        run_puzzles_cli(puzzles)
