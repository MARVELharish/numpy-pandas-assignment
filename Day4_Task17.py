import pandas as pd 

sales = {
    'Product_name': ['Oil', "lipstick", "shirt","pant", "Rice", "Mobile","laptop", "charger"],
    'Category': ["cosmetics", "cosmetics","cloths", "cloths", "Food", "electronics", "electronics", "electronics"],
    'Sales' : [4000, 8000, 10000, 8000, 15000, 45000, 100000, 3000]
}

df = pd.DataFrame(sales)

categorized_df = df.groupby('Category')['Sales'].sum().reset_index()

print(categorized_df)
