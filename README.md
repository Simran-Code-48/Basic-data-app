# Top Apps Dashboard

A Streamlit application to manage and display information about top apps, including their category, description, and whether they are female-centric. This app allows users to view app details, mark apps as female-centric or non-female-centric, and save these changes to a CSV file.

## Features

- **View App Details:** Display information about each app, including its title, category, and description.
- **Mark Female-Centric Status:** Use a radio button to specify if an app is female-centric or non-female-centric.
- **Save Changes:** Update the CSV file with the new female-centric status. A success message is shown for 2 seconds before the app refreshes.
- **Navigate Apps:** Move between apps using Previous and Next buttons.

## How to Run the App Locally

### 1. Install Python

Ensure Python is installed on your machine. Download it from the [official Python website](https://www.python.org/downloads/) if needed.

### 2. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/your-username/top-apps-dashboard.git 


### 3. Install the Required Packages

   Create a `requirements.txt` file with the following content:

   ```txt
   streamlit
   pandas
   
### 4. Run the app by running "python -m streamlit run streamlit_app.py"
