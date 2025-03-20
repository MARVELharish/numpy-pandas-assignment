import pandas as pd

sales = {
    'Product_name': ['Oil', "lipstick", "shirt","pant", "Rice", "Mobile","laptop", "charger"],
    'Category': ["cosmetics", "cosmetics","cloths", "cloths", "Food", "electronics", "electronics", "electronics"],
    'No_Product': [20, 15,25, 15, 50, 10, 8, 23],
    'Sales' : [4000, 8000, 10000, 8000, 15000, 45000, 100000, 3000] }

df = pd.DataFrame(sales)

pivot_df = pd.pivot_table(df, values="Sales", index= "Category", columns= "Product_name", aggfunc="sum", fill_value=0)

print(pivot_df)
