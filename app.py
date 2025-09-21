import streamlit as st
import pandas as pd
import pickle as pkl

model = pkl.load(open("CPP.pkl", "rb+"))
df = pd.read_csv("cleaned_data.csv")

companies = sorted(df["company"].unique())

st.title("Welcome to Car Price Prediction Project")
company = st.selectbox("Select you car company", companies)
names = sorted(df["name"][df["company"] == company].unique())
name = st.selectbox("Select you car", names)
year = st.number_input("Enter you car model:", min_value=1990, max_value = 2025)
kms_driven = st.number_input("Enter you car running:", min_value=0, max_value = 200000)
fuel_type = st.selectbox("Select fuel type", ["Petrol", "Diesel", "LPG"])

if st.button("Predict"):

    myinput = pd.DataFrame(data = [[company, name, year, kms_driven, fuel_type]], 
                       columns = ["company", "name", "year", "kms_driven", "fuel_type"])
    
    st.write("Your input")
    st.write(myinput)
    price = model.predict(myinput)
    st.write("Predicted price:" + str(round(price[0,0])))