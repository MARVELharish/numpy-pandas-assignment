import pandas as pd

student = {'Name': ["Harishkumar","ShubhaShree","Ganesh"],
           'Tamil':[100,0,0],
           'English': [90,80,70],
           'Mathematics': [100,100,100]}

df = pd.DataFrame(student)
print(df)