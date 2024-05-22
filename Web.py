import streamlit as st
import requests
import pandas as pd
import json
import random
# Define base URL for API
base_url = "http://127.0.0.1:5000"

# Title of the web app
st.title("Big Data Project API")

# Subtitles for different collections
st.subheader("Health Collection")
st.write("Interact with endpoints related to the Health collection.")

# Function to perform CRUD operations and other functionalities for Health Collection
def perform_health_operation(operation, payload=None,Header=None):
    if operation == "Create One":
        response = requests.post(f"{base_url}/health", json=payload)
    elif operation == "Get All":
        response = requests.get(f"{base_url}/health/getall")
    elif operation == "Get by Patient ID":
        response = requests.get(f"{base_url}/health/{payload}")
    elif operation == "Add index":
        response = requests.get(f"{base_url}/health/index/{payload}/{Header}")
    elif operation == "Delete index":
        response = requests.delete(f"{base_url}/health/index/{payload}/{Header}")
    elif operation == "Get Hint":
        response = requests.get(f"{base_url}/health/hint/{payload}/{Header}")
    elif operation == "Update by Patient ID":
        response = requests.put(f"{base_url}/health/{Header}", json=payload)
    elif operation == "Delete by Patient ID":
        response = requests.delete(f"{base_url}/health/{payload}")
    elif operation == "Count Patients with Diabetes":
        response = requests.get(f"{base_url}/health/count")
    elif operation == "Aggregate Patients with Previous Heart Problems":
        response = requests.get(f"{base_url}/health/aggregate")
    elif operation == "MapReduce Stress level":
        response = requests.get(f"{base_url}/health/mapreduce/average_stress_level")
    elif operation == "MapReduce Cholesterol Count":
        response = requests.get(f"{base_url}/health/mapreduce/high_cholesterol_count")
    else:
        return

    if response.status_code ==200  :
        data = response.json()
        if operation in["Count Patients with Diabetes" , "Update by Patient ID" ,"Delete by Patient ID","Delete index"]:
           for key in response.json():
               return f"{key}:{response.json()[key]}"  
           
           return data
        elif data and operation!="Count Patients with Diabetes":
            df = pd.DataFrame(data)
            return df
    elif response.status_code==201 :return response.json()   
    else:
            return response.json()

# Sidebar menu to select operation for Health Collection
health_operation = st.sidebar.selectbox("Health Collection Operations", ["Create One", "Get All", "Get by Patient ID", 
                                                                        "Update by Patient ID", "Delete by Patient ID",
                                                                        "Count Patients with Diabetes", 
                                                                        "Aggregate Patients with Previous Heart Problems","MapReduce Stress level","MapReduce Cholesterol Count",
                                                                        "Add index","Delete index","Get Hint"])

# Perform selected operation for Health Collection
if health_operation in ["Create One"]:
    st.subheader(health_operation)
    payload = st.text_area("Enter JSON data:", key=f"health_{health_operation.lower().replace(' ', '_')}_payloadc")
    st.warning("must enter a Patient ID.")
    if st.button("Submit"):
        payload=json.loads(payload)
        result = perform_health_operation(health_operation, payload)
        st.write(result)
        
elif health_operation in["Update by Patient ID"]:
    st.subheader("Update by Patient ID")
    Header=st.text_input("Enter Patient ID",key=f"health_{health_operation.lower().replace(' ', '_')}_idhu")
    payload = st.text_area("Enter JSON data:",key=f"health_{health_operation.lower().replace(' ', '_')}_idpu")
    if not payload or not Header:
         st.warning("Please enter a Patient ID.")
         st.stop()
    if st.button("Submit   "):
        payload=json.loads(payload)
        result=perform_health_operation(health_operation,payload,Header)
        st.write(result)
elif health_operation in["Get Hint","Add index","Delete index"]:
    st.subheader(health_operation)
    Header=st.selectbox("Enter direction",key=f"health_{health_operation.lower().replace(' ', '_')}_idhi",options=["1","-1"])
    payload = st.text_input("Enter Field name data:",key=f"health_{health_operation.lower().replace(' ', '_')}_idpi")
    if not payload or not Header:
         st.warning("Please enter a Field Name.")
         st.stop()
    if st.button("Submit   "):
        
        result=perform_health_operation(health_operation,payload,Header)
        st.write(result)
else:
    result=""
    payload=""
    if health_operation == "Get by Patient ID" or health_operation == "Delete by Patient ID":
        payload = st.text_input("Enter Patient ID:", key=f"health_{health_operation.lower().replace(' ', '_')}_idpg")
        if not payload:
            st.warning("Please enter a Patient ID.")
            st.stop()
        if st.button("Submit"):
            result = perform_health_operation(health_operation, payload)
       
    result = perform_health_operation(health_operation, payload)
    st.write(result)


# Subtitles for HeartRisk Collection
st.subheader("HeartRisk Collection")
st.write("Interact with endpoints related to the HeartRisk collection.")

# Function to perform CRUD operations and other functionalities for HeartRisk Collection
def perform_heartrisk_operation(operation, payload=None,Header=5):
    if operation == "Create One":
        response = requests.post(f"{base_url}/heartrisk", json=payload)
    elif operation == "Get All":
        response = requests.get(f"{base_url}/heartrisk/getall")
    elif operation == "Get by Patient ID":
        response = requests.get(f"{base_url}/heartrisk/{payload}")
        
    elif operation == "Add index":
        response = requests.get(f"{base_url}/heartrisk/index/{payload}/{Header}")
    elif operation == "Delete index":
        response = requests.delete(f"{base_url}/heartrisk/index/{payload}/{Header}")
    elif operation == "Get Hint":
        response = requests.get(f"{base_url}/heartrisk/hint/{payload}/{Header}")
        
    elif operation == "Update by Patient ID":
        response = requests.put(f"{base_url}/heartrisk/{Header}", json=payload)
    elif operation == "Delete by Patient ID":
        response = requests.delete(f"{base_url}/heartrisk/{payload}")
    elif operation == "Count Patients with Heart Attack Risk":
        response = requests.get(f"{base_url}/heartrisk/count")
    elif operation == "Aggregate Patients with Heart Attack Risk":
        response = requests.get(f"{base_url}/heartrisk/aggregate")
    elif operation == "MapReduce High Risk Count":
        response = requests.get(f"{base_url}/heartrisk/mapreduce/high_risk_count")
    else:
        return

    if response.status_code ==200  :
        data = response.json()
        if operation in["Count Patients with Heart Attack Risk" , "Update by Patient ID" ,"Delete by Patient ID","Delete index"]:
           for key in response.json():
               return f"{key}:{response.json()[key]}"  
           
           return data
        elif data and operation!="Count Patients with Heart Attack Risk":
            df = pd.DataFrame(data)
            return df
    elif response.status_code==201 :return response.json()   
    else:
            return response.json()
# Sidebar menu to select operation for HeartRisk Collection
heartrisk_operation = st.sidebar.selectbox("HeartRisk Collection Operations", ["Create One", "Get All", "Get by Patient ID", 
                                                                              "Update by Patient ID", "Delete by Patient ID",
                                                                              "Count Patients with Heart Attack Risk", 
                                                                              "Aggregate Patients with Heart Attack Risk","MapReduce High Risk Count",
                                                                              "Add index","Delete index","Get Hint"])

# Perform selected operation for HeartRisk Collection
if heartrisk_operation in ["Create One"]:
    st.subheader(heartrisk_operation)
    payload = st.text_area("Enter JSON data: ", key=f"heartrisk_{heartrisk_operation.lower().replace(' ', '_')}_payloadc")
    st.warning("must enter a Patient ID.")

    if st.button("Submit "+health_operation):
        payload=json.loads(payload)
        result = perform_heartrisk_operation(heartrisk_operation, payload)
        st.write(result)
elif heartrisk_operation in["Get Hint","Add index","Delete index"]:
    st.subheader(heartrisk_operation)
    Header=st.selectbox("Enter direction",key=f"heartrisk_{heartrisk_operation.lower().replace(' ', '_')}_idhi",options=["1","-1"])
    payload = st.text_input("Enter Field name data:",key=f"heartrisk_{heartrisk_operation.lower().replace(' ', '_')}_idpi")
    if not payload or not Header:
         st.warning("Please enter a Field Name.")
         st.stop()
    if st.button("Submit          "):
        
        result=perform_heartrisk_operation(heartrisk_operation,payload,Header)
        st.write(result)
        
elif heartrisk_operation in["Update by Patient ID"]:
    st.subheader("Update by Patient ID")
    Header=st.text_input("Enter Patient ID",key=f"heartrisk_{heartrisk_operation.lower().replace(' ', '_')}_idhu")
    payload = st.text_area("Enter JSON data:",key=f"heartrisk_{heartrisk_operation.lower().replace(' ', '_')}_idpu")
    if not payload or not Header:
         st.warning("Please enter a Patient ID.")
         st.stop()
    if st.button("Submit   "):
        payload=json.loads(payload)
        result=perform_heartrisk_operation(heartrisk_operation,payload,Header)
        st.write(result)

else:
    payload=""
    if heartrisk_operation == "Get by Patient ID" or heartrisk_operation == "Delete by Patient ID":
        payload = st.text_input("Enter Patient ID:", key=f"heartrisk_{heartrisk_operation.lower().replace(' ', '_')}_idpg")
        if not payload:
            st.warning("Please enter a Patient ID.")
            st.stop()

    result = perform_heartrisk_operation(heartrisk_operation, payload)
    if isinstance(result, pd.DataFrame):
        st.write(result)
    else:
        st.write(result)
# Subtitles for Patients Collection
st.subheader("Patients Collection")
st.write("Interact with endpoints related to the Patients collection.")

# Function to perform CRUD operations and other functionalities for Patients Collection
def perform_patients_operation(operation, payload=None,Header=5):
    if operation == "Create One":
        response = requests.post(f"{base_url}/patients", json=payload)
    elif operation == "Get All":
        response = requests.get(f"{base_url}/patients/getall")
    elif operation == "Get by Patient ID":
        response = requests.get(f"{base_url}/patients/{payload}")
        
    elif operation == "Add index":
        response = requests.get(f"{base_url}/patients/index/{payload}/{Header}")
    elif operation == "Delete index":
        response = requests.delete(f"{base_url}/patients/index/{payload}/{Header}")
    elif operation == "Get Hint":
        response = requests.get(f"{base_url}/patients/hint/{payload}/{Header}") 
           
    elif operation == "Update by Patient ID":
        response = requests.put(f"{base_url}/patients/{Header}", json=payload)
    elif operation == "Delete by Patient ID":
        response = requests.delete(f"{base_url}/patients/{payload}")
    elif operation == "Count Patients Age Over 60":
        response = requests.get(f"{base_url}/patients/count")
    elif operation == "Aggregate Africa Male Patients":
        response = requests.get(f"{base_url}/patients/aggregate")
    elif operation == "MapReduce Age per Continent":
        response = requests.get(f"{base_url}/patients/mapreduce/average_age_per_continent")
    elif operation == "MapReduce Big Country Big Avg Income":
        response = requests.get(f"{base_url}/patients/mapreduce/big_country_big_avg_income")
    else:
        return

    if response.status_code ==200  :
        data = response.json()
        if operation in["Count Patients Age Over 60" , "Update by Patient ID" ,"Delete by Patient ID","Delete index"]:
           for key in response.json():
               return f"{key}:{response.json()[key]}"  
           
           return data
        elif data and operation!="Count Patients Age Over 60":
            df = pd.DataFrame(data)
            return df
    elif response.status_code==201 :return response.json()   
    else:
            return response.json()

# Sidebar menu to select operation for Patients Collection
patients_operation = st.sidebar.selectbox("Patients Collection Operations", ["Create One", "Get All", "Get by Patient ID", 
                                                                            "Update by Patient ID", "Delete by Patient ID",
                                                                            "Count Patients Age Over 60", 
                                                                            "Aggregate Africa Male Patients","MapReduce Age per Continent","MapReduce Big Country Big Avg Income",
                                                                            "Add index","Delete index","Get Hint"])

# Perform selected operation for Patients Collection
if patients_operation in ["Create One"]:
    st.subheader(patients_operation)
    payload = st.text_area("Enter JSON data:", key=f"patients_{patients_operation.lower().replace(' ', '_')}_payloadc")
    st.warning("must enter a Patient ID.")

    if st.button("Submit "):
        payload=json.loads(payload)
        result = perform_patients_operation(patients_operation, payload)
        st.write(result)
        
elif patients_operation in["Get Hint","Add index","Delete index"]:
    st.subheader(patients_operation)
    Header=st.selectbox("Enter direction",key=f"patients_{patients_operation.lower().replace(' ', '_')}_idhi",options=["1","-1"])
    payload = st.text_input("Enter Field name data:",key=f"patients_{patients_operation.lower().replace(' ', '_')}_idpi")
    if not payload or not Header:
         st.warning("Please enter a Field Name.")
         st.stop()
    if st.button("Submit      "):
        
        result=perform_patients_operation(patients_operation,payload,Header)
        st.write(result)
        
elif patients_operation in["Update by Patient ID"]:
    st.subheader("Update by Patient ID")
    Header=st.text_input("Enter Patient ID",key=f"patient{patients_operation.lower().replace(' ', '_')}_idhu")
    payload = st.text_area("Enter JSON data:",key=f"patient{patients_operation.lower().replace(' ', '_')}_idpu")
    if not payload or not Header:
         st.warning("Please enter a Patient ID.")
         st.stop()
    if st.button("Submit   "):
        payload=json.loads(payload)
        result=perform_patients_operation(patients_operation,payload,Header)
        st.write(result)

else:
    payload=""
    if patients_operation == "Get by Patient ID" or patients_operation == "Delete by Patient ID":
        payload = st.text_input("Enter Patient ID:", key=f"patients_{patients_operation.lower().replace(' ', '_')}_idpg")
        if not payload:
            st.warning("Please enter a Patient ID.")
            st.stop()

    result = perform_patients_operation(patients_operation, payload)
    if isinstance(result, pd.DataFrame):
        st.write(result)
    else:
        st.write(result)

# Subtitles for Lifestyle Collection
st.subheader("Lifestyle Collection")
st.write("Interact with endpoints related to the Lifestyle collection.")

# Function to perform CRUD operations and other functionalities for Lifestyle Collection
def perform_lifestyle_operation(operation, payload=None,Header=5):
    if operation == "Create One":
        response = requests.post(f"{base_url}/lifestyle", json=payload)
    elif operation == "Get All":
        response = requests.get(f"{base_url}/lifestyle/getall")
    elif operation == "Get by Patient ID":
        response = requests.get(f"{base_url}/lifestyle/{payload}")
        
    elif operation == "Add index":
        response = requests.get(f"{base_url}/lifestyle/index/{payload}/{Header}")
    elif operation == "Delete index":
        response = requests.delete(f"{base_url}/lifestyle/index/{payload}/{Header}")
    elif operation == "Get Hint":
        response = requests.get(f"{base_url}/lifestyle/hint/{payload}/{Header}")
        
    elif operation == "Update by Patient ID":
        response = requests.put(f"{base_url}/lifestyle/{Header}", json=payload)
    elif operation == "Delete by Patient ID":
        response = requests.delete(f"{base_url}/lifestyle/{payload}")
    elif operation == "Count Smoking and Alcohol":
        response = requests.get(f"{base_url}/lifestyle/count")
    elif operation == "Aggregate Unhealthy Diet":
        response = requests.get(f"{base_url}/lifestyle/aggregate")
    elif operation=="MapReduce Count Alcohol Non Smokers":
        response=requests.get(f"{base_url}/lifestyle/mapreduce/count_alcohol_non_smokers")
    elif operation=="MapReduce Average Sleep Smokers":
        response=requests.get(f"{base_url}/lifestyle/mapreduce/average_sleep_smokers")
    elif operation=="MapReduce Low Exercise Count":
        response=requests.get(f"{base_url}/lifestyle/mapreduce/low_exercise_count")
    else:
        return

    if response.status_code ==200  :
        data = response.json()
        if operation in["Count Smoking and Alcohol" , "Update by Patient ID" ,"Delete by Patient ID","Delete index"]:
           for key in response.json():
               return f"{key}:{response.json()[key]}"  
           
           return data
        elif data and operation!="Count Smoking and Alcohol":
            df = pd.DataFrame(data)
            return df
        
    elif response.status_code==201 :return response.json()   
    else:
            return response.json()

# Sidebar menu to select operation for Lifestyle Collection
lifestyle_operation = st.sidebar.selectbox("Lifestyle Collection Operations", ["Create One", "Get All", "Get by Patient ID", 
                                                                                "Update by Patient ID", "Delete by Patient ID",
                                                                                "Count Smoking and Alcohol", 
                                                                                "Aggregate Unhealthy Diet","MapReduce Count Alcohol Non Smokers",
                                                                                "MapReduce Average Sleep Smokers",
                                                                                "MapReduce Low Exercise Count",
                                                                                "Add index","Delete index","Get Hint"])

# Perform selected operation for Lifestyle Collection
if lifestyle_operation in ["Create One"]:
    st.subheader(lifestyle_operation)
    payload = st.text_area("Enter JSON data:", key=f"lifestyle_{lifestyle_operation.lower().replace(' ', '_')}_payloadc")
    st.warning("must enter a Patient ID.")

    if st.button("Submit  "):
        payload=json.loads(payload)     
        result = perform_lifestyle_operation(lifestyle_operation, payload)
        st.write(result)
        
elif lifestyle_operation in["Get Hint","Add index","Delete index"]:
    st.subheader(lifestyle_operation)
    Header=st.selectbox("Enter direction",key=f"lifestyle_{lifestyle_operation.lower().replace(' ', '_')}_idhi",options=["1","-1"])
    payload = st.text_input("Enter Field name data:",key=f"lifestyle_{lifestyle_operation.lower().replace(' ', '_')}_idpi")
    if not payload or not Header:
         st.warning("Please enter a Field Name.")
         st.stop()
    if st.button("Submit       "):
        
        result=perform_lifestyle_operation(lifestyle_operation,payload,Header)
        st.write(result)
        
elif lifestyle_operation in["Update by Patient ID"]:
    st.subheader("Update by Patient ID")
    Header=st.text_input("Enter Patient ID",key=f"lifestyle_{lifestyle_operation.lower().replace(' ', '_')}_idhu")
    payload = st.text_area("Enter JSON data:",key=f"lifestyle_{lifestyle_operation.lower().replace(' ', '_')}_idpu")
    if not payload or not Header:
         st.warning("Please enter a Patient ID.")
         st.stop()
    if st.button("Submit      "):
        payload=json.loads(payload)
        result=perform_lifestyle_operation(lifestyle_operation,payload,Header)
        st.write(result)

else:
    payload=""
    if lifestyle_operation == "Get by Patient ID" or lifestyle_operation == "Delete by Patient ID":
        payload = st.text_input("Enter Patient ID:", key=f"lifestyle_{lifestyle_operation.lower().replace(' ', '_')}_idpg")
        if not payload:
            st.warning("Please enter a Patient ID.")
            st.stop()

    result = perform_lifestyle_operation(lifestyle_operation, payload)
    if isinstance(result, pd.DataFrame):
        st.write(result)
    else:
        st.write(result)
