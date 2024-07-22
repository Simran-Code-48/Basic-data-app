import streamlit as st
import pandas as pd
import time

# Read CSV data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load the data
csv_file_path = 'top_apps_IN_with_female_centric.csv'  # Update with the correct file path
data = load_data(csv_file_path)

apps = data.rename(columns={"appName": "title"}).to_dict(orient="records")

# Initialize session state for app index
if 'index' not in st.session_state:
    st.session_state.index = 0


# Function to save the updated data to the CSV file
def save_changes(index, female_centric):
    data.at[index, 'female_centric'] = female_centric
    data.to_csv(csv_file_path, index=False)
    
def show_app(index):
    app = apps[index]
    st.title(app["title"])
    st.write(f"**Category:** {app['category']}")
    st.write(f"**Description:** {app['description']}")
    st.write(f"**Female centric:** {app['female_centric']}")
    female_centric = st.radio(
        "Is this App Female centric?",
        [True, False],
        format_func=lambda x: "Yes" if x else "No",
        captions=["Female centric", "Non-female centric"],
        index=0 if app.get('female_centric', False) else 1
    )
    if st.button("Save"):
        save_changes(index, female_centric)
        st.success("Changes saved successfully!")
        time.sleep(2)  # Wait for 5 seconds
        st.experimental_rerun() 
        
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
