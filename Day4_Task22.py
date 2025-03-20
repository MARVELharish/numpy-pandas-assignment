import pandas as pd

employee = {
    'Name': ['Harishkumar','Shubha','Ganesh','David','Saran','Harishkumar'],
    'emp_id': ['101', '102','103', '401', '402', '101'],
    'age': [22,22,22,27,26,22]
}

df = pd.DataFrame(employee)
print(df)

final_df = df.drop_duplicates()
print(final_df)