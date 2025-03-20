import pandas as pd

sales = {
    'Product_name': ['Oil', "lipstick", "shirt","pant", "Rice", "Mobile","laptop", "charger"],
    'Category': ["cosmetics", "cosmetics","cloths", "cloths", "Food", "electronics", "electronics", "electronics"],
    'No_Product': [20, 15,25, 15, 50, 10, 8, 23],
    'Sales' : [4000, 8000, 10000, 8000, 15000, 45000, 100000, 3000] }

df = pd.DataFrame(sales)

def increase_sales_10(Sales_value):
    return Sales_value * 1.10

df['Sales'] = df["Sales"].apply(increase_sales_10)

print(df)