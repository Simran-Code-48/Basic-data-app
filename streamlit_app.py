import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Sample data for apps
apps = [
    {"title": "App1", "category": "Category1", "description": "Description1"},
    {"title": "App2", "category": "Category2", "description": "Description2"},
    {"title": "App3", "category": "Category3", "description": "Description3"},
]

# Initialize session state for app index
if 'index' not in st.session_state:
    st.session_state.index = 0

def show_app(index):
    app = apps[index]
    st.title(app["title"])
    st.write(f"**Category:** {app['category']}")
    st.write(f"**Description:** {app['description']}")
    # female_centric = st.radio(
    #     "Is this App Female centric ? ",
    #     ["Yes", "No"],
    #     captions = ["Female Centric", "Not female centric"])
    # # Display current app
    female_centric1 = st.selectbox("Female Centric", ["Yes", "No"])
    return female_centric

def next_app():
    if st.session_state.index < len(apps) - 1:
        st.session_state.index += 1

def prev_app():
    if st.session_state.index > 0:
        st.session_state.index -= 1

female_centric = show_app(st.session_state.index)
# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous"):
        prev_app()
with col2:
    if st.button("Next"):
        next_app()
