import streamlit as st
import pandas as pd

# Read CSV data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load the data
csv_file_path = 'top_apps_IN_with_female_centric.csv'
data = load_data(csv_file_path)

# Initialize session state if not already set
if 'row_index' not in st.session_state:
    st.session_state.row_index = 0

# Display the current row's data
current_row = data.iloc[st.session_state.row_index]
st.write("Current row data:")
st.write(current_row)

# Display the value of the female_centric column
female_centric_value = current_row['female_centric']
st.write("Value of female_centric for the current row:")
st.write(female_centric_value)

# Check and display the data type of female_centric
female_centric_dtype = data['female_centric'].dtype
st.write("Data type of female_centric column:")
st.write(female_centric_dtype)

# Navigation buttons
col1, col2 = st.columns([1, 3])

with col1:
    if st.button('Previous'):
        if st.session_state.row_index > 0:
            st.session_state.row_index -= 1

with col2:
    if st.button('Next'):
        if st.session_state.row_index < len(data) - 1:
            st.session_state.row_index += 1

# apps = data.rename(columns={"appName": "title"}).to_dict(orient="records")

# # Initialize session state for app index
# if 'index' not in st.session_state:
#     st.session_state.index = 0

# # Function to save the updated data to the CSV file
# def save_changes(index, female_centric):
#     st.write(f"Saving changes at index {index} with female_centric={female_centric}")
#     app_name = apps[index]['title']
#     data_index = data[data['appName'] == app_name].index[0]
#     data.at[data_index, 'female_centric'] = female_centric
#     st.write(f"Updated DataFrame row:\n{data.loc[data_index]}")
#     # Save to CSV
#     data.to_csv(csv_file_path, index=False)
#     # Reload the data to check if changes were saved
#     updated_data = load_data(csv_file_path)
#     # Debug statement to confirm changes
#     st.write(f"Reloaded DataFrame row:\n{updated_data.loc[data_index]}")
    
# def show_app(index):
#     app = apps[index]
#     st.title(app["title"])
#     st.write(f"**Category:** {app['category']}")
#     st.write(f"**Description:** {app['description']}")
#     st.write(f"**Female centric:** {app['female_centric']}")
#     female_centric = st.radio(
#         "Is this App Female centric?",
#         [True, False],
#         format_func=lambda x: "Yes" if x else "No",
#         captions=["Female centric", "Non-female centric"],
#         index=0 if app.get('female_centric', False) else 1
#     )
#     if st.button("Save"):
#         save_changes(index, female_centric)
#         st.success("Changes saved successfully!")
#         time.sleep(2)  # Wait for 5 seconds
#         st.rerun() 
        
#     return female_centric

# def next_app():
#     if st.session_state.index < len(apps) - 1:
#         st.session_state.index += 1

# def prev_app():
#     if st.session_state.index > 0:
#         st.session_state.index -= 1


# # Display current app
# female_centric = show_app(st.session_state.index)

# Navigation buttons
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("Previous"):
#         prev_app()
#         st.rerun()
# with col2:
#     if st.button("Next"):
#         next_app()
#         st.rerun()
