import pandas as pd
import joblib

model = joblib.load("models/demand_model.pkl")

data = {
"day_of_week":[2],
"month":[7],
"item_name":[3],
"time_slot":[1],
"price":[250],
"inventory_level":[300],
"year":[2024],
"day":[15],
"weekofyear":[28]
}

df = pd.DataFrame(data)

prediction = model.predict(df)

print("Predicted Demand:",int(prediction[0]))
