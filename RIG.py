import time
import pandas as pd
import streamlit as st
from datetime import datetime

data_collection = []

st.title("Hello! Welcome to RIG.")
st.header("Registration Form")

name = st.text_input("Enter Your Name")
gender = st.radio("Choose Your Gender", ["Male", "Female"])
email = st.text_input("Enter Your Email")
category = st.selectbox("Choose Your Category", ["Select an option...", "Student", "Worker", "Traveller"])

if st.button("Submit"):
    if category == "Select an option...":
        st.error("Please choose a valid category")
    else:
        st.header("Submitting Details...")
        bar = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)

        timestamp = datetime.now().strftime("%d-%b-%Y %H:%M:%S")

        user_data = {
            "Name": name,
            "Gender": gender,
            "Email": email,
            "Category": category,
            "Timestamp": timestamp
        }

        data_collection.append(user_data)

        df = pd.DataFrame(data_collection)

        df.to_csv("user_data.csv", index=False)

        st.success("Successfully Submitted")
        st.write("Collected Data:", df)
