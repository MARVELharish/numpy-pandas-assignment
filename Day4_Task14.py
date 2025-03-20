import pandas as pd

file = r"D:\VDI_Source_File\edna_scada map.xlsx"
df = pd.read_excel(file, header=None)
print(df.head(5))
df = df.drop(1, axis='columns')

df_changed = df.to_excel("Python_assignment.xlsx", index=False)

