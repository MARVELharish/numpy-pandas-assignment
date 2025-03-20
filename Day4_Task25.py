import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [150, 200, 250, 300, 350, 400]
}

df = pd.DataFrame(data)

df['Profit'] = df['Sales'] * 0.20

file_path = 'sales_data.xlsx' 
df.to_excel(file_path, index=False)

print(f"Data has been exported to {file_path}")
