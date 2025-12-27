import streamlit as st
import random

st.set_page_config(page_title="Memory Game", layout="centered")
st.title("🧠 Memory Game")

# Initialize session state
if "sequence" not in st.session_state:
    st.session_state.sequence = []

if "player_input" not in st.session_state:
    st.session_state.player_input = []

if "level" not in st.session_state:
    st.session_state.level = 0

if "message" not in st.session_state:
    st.session_state.message = "Click 'Start Game' to begin!"

# Function to start a new level
def start_level():
    st.session_state.level += 1
    st.session_state.sequence.append(random.choice(["Red", "Green", "Blue", "Yellow"]))
    st.session_state.player_input = []
    st.session_state.message = f"Level {st.session_state.level}: Watch the sequence!"

# Function to handle player click
def handle_click(color):
    st.session_state.player_input.append(color)

    # Check input correctness
    idx = len(st.session_state.player_input) - 1
    if st.session_state.player_input[idx] != st.session_state.sequence[idx]:
        st.session_state.message = f"Wrong! You reached level {st.session_state.level}. Click 'Start Game' to try again."
        st.session_state.level = 0
        st.session_state.sequence = []
        st.session_state.player_input = []
    elif len(st.session_state.player_input) == len(st.session_state.sequence):
        st.session_state.message = "Correct! Get ready for the next level."
        start_level()

# Start Game Button
if st.button("Start Game"):
    st.session_state.level = 0
    st.session_state.sequence = []
    start_level()

# Display message
st.write(st.session_state.message)

# Display colored buttons
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    if st.button("🔴 Red"):
        handle_click("Red")
with col2:
    if st.button("🟢 Green"):
        handle_click("Green")
with col3:
    if st.button("🔵 Blue"):
        handle_click("Blue")
with col4:
    if st.button("🟡 Yellow"):
        handle_click("Yellow")
