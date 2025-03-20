import pandas as pd

data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

data2 = {
    'Name': ['David', 'Eva', 'Frank'],
    'Age': [40, 45, 50]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df_row_wise = pd.concat([df1, df2], axis=0, ignore_index=True)

df_column_wise = pd.concat([df1, df2], axis=1)

print("Row-wise Concatenation:")
print(df_row_wise)

print("\nColumn-wise Concatenation:")
print(df_column_wise)
