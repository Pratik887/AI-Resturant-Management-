import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/demand_model.pkl")

st.title("AI Restaurant Demand Forecasting & Inventory Optimization")

day_of_week = st.selectbox("Day of Week",[0,1,2,3,4,5,6])
month = st.selectbox("Month",[1,2,3,4,5,6,7,8,9,10,11,12])
item_name = st.selectbox("Item",[0,1,2,3,4])
time_slot = st.selectbox("Time Slot",[0,1,2])
price = st.number_input("Price",100,500,200)
inventory_level = st.number_input("Current Inventory",0,500,150)
year = st.number_input("Year",2024,2030,2024)
day = st.number_input("Day",1,31,20)
weekofyear = st.number_input("Week Of Year",1,52,30)

if st.button("Predict Demand"):

    data = {
        "day_of_week":[day_of_week],
        "month":[month],
        "item_name":[item_name],
        "time_slot":[time_slot],
        "price":[price],
        "inventory_level":[inventory_level],
        "year":[year],
        "day":[day],
        "weekofyear":[weekofyear]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)[0]

    safety_stock = 50
    reorder_level = prediction + safety_stock

    st.subheader("Prediction Result")
    st.write("Predicted Demand:", int(prediction))
    st.write("Current Inventory:", inventory_level)

    if inventory_level < reorder_level:
        reorder_quantity = int(reorder_level - inventory_level)
        st.error(f"Reorder Required: {reorder_quantity} units")
    else:
        st.success("Inventory Level is Sufficient")