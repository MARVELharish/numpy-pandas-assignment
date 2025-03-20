import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [150, 200, 250, 300, 350, 400]
}

df = pd.DataFrame(data)

# plt.figure(figsize=(10, 6))
# df.plot(x='Month', y='Sales', kind='line', marker='o', title='Monthly Sales - Line Plot', color='b')
# plt.ylabel('Sales')
# plt.xlabel('Month')
# plt.grid(True)
# plt.show()

plt.figure(figsize=(10, 6))
df.plot(x='Month', y='Sales', kind='bar', title='Monthly Sales - Bar Chart', color='g')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.grid(True)
plt.show()
