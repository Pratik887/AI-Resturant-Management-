import pandas as pd
import random

items = ["Pizza","Burger","Pasta","Sandwich","Salad","Biryani","Fried Rice","Noodles","Ice Cream","Coffee"]

base_demand = {
    "Pizza":120,
    "Burger":100,
    "Pasta":80,
    "Sandwich":70,
    "Salad":50,
    "Biryani":130,
    "Fried Rice":90,
    "Noodles":85,
    "Ice Cream":60,
    "Coffee":110
}

prices = {
    "Pizza":350,
    "Burger":200,
    "Pasta":300,
    "Sandwich":180,
    "Salad":150,
    "Biryani":250,
    "Fried Rice":220,
    "Noodles":210,
    "Ice Cream":120,
    "Coffee":100
}

dates = pd.date_range(start="2023-01-01", end="2024-12-31")

data = []

for date in dates:

    day_of_week = date.day_name()
    month = date.month

    if day_of_week in ["Saturday","Sunday"]:
        weekend_factor = 1.4
    else:
        weekend_factor = 1

    if month in [11,12]:
        seasonal_factor = 1.3
    elif month in [4,5,6]:
        seasonal_factor = 1.1
    else:
        seasonal_factor = 1

    for item in items:

        for time_slot in ["Lunch","Dinner"]:

            demand = base_demand[item]

            if time_slot == "Dinner":
                demand = demand * 1.2

            demand = demand * weekend_factor * seasonal_factor

            noise = random.randint(-20,20)

            quantity_sold = int(demand + noise)

            inventory_level = random.randint(200,500)

            data.append([
                date,
                day_of_week,
                month,
                item,
                time_slot,
                prices[item],
                quantity_sold,
                inventory_level
            ])

df = pd.DataFrame(data, columns=[
    "date",
    "day_of_week",
    "month",
    "item_name",
    "time_slot",
    "price",
    "quantity_sold",
    "inventory_level"
])

df.to_csv("data/raw/restaurant_sales.csv", index=False)

print("Dataset Generated Successfully")
print("Total Rows:", len(df))