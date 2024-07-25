import pandas as pd
import psycopg2 

# Read CSV data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load the data
csv_file_path = 'top_apps_IN_with_female_centric.csv'
data = load_data(csv_file_path)

# Convert data types as required for the database schema
data['female_centric'] = data['female_centric'].astype(bool)  # Ensure boolean type

# Select the first five rows for testing
test_data = data.head(5)

conn_string = "postgresql://postgres:oismejK8yqzMD15z@resoundingly-victorious-rodent.data-1.use1.tembo.io:5432/postgres"

# Connect to the existing database
db_connection = psycopg2.connect(conn_string) # Replace with your database connection details

# Define a function to insert data into the existing table
def insert_data(df, db_connection):
    with db_connection.cursor() as cursor:
        for index, row in df.iterrows():
            cursor.execute('''
                INSERT INTO apps (
                    id,package, appName, description, category, packageId, userCount, female_centric
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                index,
                row['package'],
                row['appName'],
                row['description'],
                row['category'],
                row['packageId'],
                row['userCount'],
                row['female_centric']
            ))
        db_connection.commit()

# Insert only the first five rows into the existing table
insert_data(test_data, db_connection)

# Close the database connection
db_connection.close()


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
