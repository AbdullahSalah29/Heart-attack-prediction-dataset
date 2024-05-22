
Big Data Project: Patient Health and Lifestyle Analysis API and WEB

Project Description

Overview
This project consists of a comprehensive backend API and a user-friendly frontend interface for managing and analyzing patient health and lifestyle data. The backend is built using Flask and MongoDB to handle large datasets efficiently, while the frontend is developed using Streamlit to provide an intuitive interface for data interaction and visualization.

Backend Description
Technology Stack:
Flask: A lightweight WSGI web application framework in Python for building the API.
MongoDB: A NoSQL database used for storing and managing patient health and lifestyle data.
PyMongo: A Python driver for MongoDB to interact with the database.
Features:

CRUD Operations:

Create, read, update, and delete patient data in various collections such as health, heart risk, patients, and lifestyle.
Aggregation and Counting:

Perform data aggregation to extract meaningful insights and statistics.
Count documents that meet specific criteria, like patients with diabetes or those with heart attack risk.
Index Management:

Create and drop indexes on specific fields to optimize query performance.
Check if a field exists in the collection before creating an index to avoid errors.
Query Hints:

Use hints to enforce the use of specific indexes during query execution to improve performance.
MapReduce:

Execute complex data processing tasks using MapReduce functions to compute statistics like average stress levels and count of high cholesterol patients.
Error Handling:

Robust error handling to manage invalid operations, missing data, and other potential issues.

Endpoints:
Health Collection: Endpoints to manage health-related data.
HeartRisk Collection: Endpoints to manage heart risk-related data.
Patients Collection: Endpoints to manage general patient data.
Lifestyle Collection: Endpoints to manage lifestyle-related data.
Setup Instructions:



Run the Application:
python app.py

Frontend Description
Technology Stack:

Streamlit: An open-source app framework in Python for creating beautiful, custom web apps for machine learning and data science.
Features:

User-Friendly Interface:

Intuitive interface to interact with the backend API.
Sidebar menus for easy navigation between different operations.
Data Input and Display:

Text areas for inputting JSON data.
Data tables and formatted text to display API responses and results.
Operation Management:

Perform CRUD operations directly from the interface.
Execute aggregation, counting, indexing, and MapReduce operations with ease.
Real-Time Interaction:

Submit data and view results in real-time without needing to refresh the page.
Handle and display errors effectively to guide users.

Usage Instructions:

Access the Streamlit Interface:
streamlit run Web.py

Perform Operations:
Select the desired collection and operation from the sidebar.
Input the required data in the provided text areas.
Click on the "Submit" button to perform the operation and view the results.
