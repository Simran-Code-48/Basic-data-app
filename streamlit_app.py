import streamlit as st
import pandas as pd

# Read CSV data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Load the data
csv_file_path = 'top_apps_IN.csv'  # Update with the correct file path
data = load_data(csv_file_path)

apps = data.rename(columns={"appName": "title"}).to_dict(orient="records")

# Initialize session state for app index
if 'index' not in st.session_state:
    st.session_state.index = 0

def show_app(index):
    app = apps[index]
    st.title(app["title"])
    st.write(f"**Category:** {app['category']}")
    st.write(f"**Description:** {app['description']}")
    
   female_centric = st.radio(
        "Is this App Female centric?",
        ["Yes", "No"],
        captions=["Female centric", "Non-female centric"]
   )
    return female_centric

def next_app():
    if st.session_state.index < len(apps) - 1:
        st.session_state.index += 1

def prev_app():
    if st.session_state.index > 0:
        st.session_state.index -= 1


# Display current app
female_centric = show_app(st.session_state.index)

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous"):
        prev_app()
        st.experimental_rerun()
with col2:
    if st.button("Next"):
        next_app()
        st.experimental_rerun()
