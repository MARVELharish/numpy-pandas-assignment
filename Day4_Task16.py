import pandas as pd

employee = {
    'Name': ["Harishkumar","Shubhashree","Ganesh","Ragav","Mahur"],
    'age': [22,22,22,30,30],
    'Salary': [15000, 15000, 15000, 60000, 80000]
}

df = pd.DataFrame(employee)

filted_df = df[df['Salary'] > 50000]

sort_filted_df = filted_df.sort_values(by="Salary", ascending = False)

print(sort_filted_df)
