import pandas as pd
import joblib

model = joblib.load("models/demand_model.pkl")

data = {
    "day_of_week": [4],
    "month": [8],
    "item_name": [1],
    "time_slot": [1],
    "price": [200],
    "inventory_level": [150],
    "year": [2024],
    "day": [20],
    "weekofyear": [34]
}

df = pd.DataFrame(data)

predicted_demand = model.predict(df)[0]

current_inventory = data["inventory_level"][0]

safety_stock = 50

reorder_level = predicted_demand + safety_stock

if current_inventory < reorder_level:
    reorder_quantity = int(reorder_level - current_inventory)
    print("Predicted Demand:", int(predicted_demand))
    print("Current Inventory:", current_inventory)
    print("Reorder Required:", reorder_quantity)
else:
    print("Predicted Demand:", int(predicted_demand))
    print("Current Inventory:", current_inventory)
    print("Inventory Level is Sufficient")