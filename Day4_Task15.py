import pandas as pd
import numpy as np
student = {'Name': ["Harishkumar","ShubhaShree","Ganesh"],
           'Tamil':[100,0,np.nan],
           'English': [90,np.nan, 70],
           'Mathematics': [np.nan,100,100]}

df = pd.DataFrame(student)

df_mean = df.fillna(df.mean())
df_median = df.copy()

df_median_filled = df_median.fillna(df_median.median())

df_mixed = df.copy()

print(df)

