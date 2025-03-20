import pandas as pd

employee = {
    'Name': ['Harishkumar','Shubha','Ganesh','David','Saran'],
    'emp_id': ['101', '102','103', '401', '402'],
    'age': [22,22,22,27,26]
}

department = {
    'emp_id': ['101', '102','103', '401', '402'],
    'department' : ['IT','IT','IT','Mech','IT']
}

df1 = pd.DataFrame(employee)
df2 = pd.DataFrame(department)

merged_df = pd.merge(df1,df2, on="emp_id", how='inner')

print(merged_df)