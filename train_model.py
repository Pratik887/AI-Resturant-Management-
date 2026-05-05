import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import numpy as np

df = pd.read_csv("data/processed/cleaned_data.csv")

X = df.drop(columns=["quantity_sold"])
y = df["quantity_sold"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestRegressor(n_estimators=200,random_state=42)

model.fit(X_train,y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test,predictions)
rmse = np.sqrt(mean_squared_error(y_test,predictions))

print("MAE:",mae)
print("RMSE:",rmse)

joblib.dump(model,"models/demand_model.pkl")

print("Model Saved Successfully")
