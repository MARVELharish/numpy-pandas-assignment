import pandas as pd

# Creating a sample DataFrame with a date column
data = {
    'Date': ['2023-01-15', '2024-03-25', '2025-07-30', '2026-11-05']
}

df = pd.DataFrame(data)

# Converting the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Extracting year, month, and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Display the DataFrame with extracted year, month, and day
print(df)
