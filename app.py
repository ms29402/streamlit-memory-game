import streamlit as st
import random
import time

st.title("🧠 Memory Game")

# Initialize game state
if "sequence" not in st.session_state:
    st.session_state.sequence = []

if "player_input" not in st.session_state:
    st.session_state.player_input = []

if "level" not in st.session_state:
    st.session_state.level = 0

if "message" not in st.session_state:
    st.session_state.message = "Click 'Start Game' to begin!"

if st.button("Start Game"):
    st.session_state.sequence = [random.choice(["Red","Green","Blue","Yellow"])]
    st.session_state.player_input = []
    st.session_state.level = 1
    st.session_state.message = f"Level {st.session_state.level}: Watch the sequence!"

st.write("Sequence:", st.session_state.sequence)
st.write(st.session_state.message)

import streamlit as st

st.set_page_config(page_title="Memory Game", layout="centered")

st.title("🧠 Memory Game")
st.write("Click the colored buttons")

# Initialize session state
if "message" not in st.session_state:
    st.session_state.message = "Waiting for input..."

# LED-style buttons
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    if st.button("🔴 RED"):
        st.session_state.message = "Red pressed"

with col2:
    if st.button("🟢 GREEN"):
        st.session_state.message = "Green pressed"

with col3:
    if st.button("🔵 BLUE"):
        st.session_state.message = "Blue pressed"

with col4:
    if st.button("🟡 YELLOW"):
        st.session_state.message = "Yellow pressed"

st.write(st.session_state.message)
