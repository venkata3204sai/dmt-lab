import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\dmt\ex16\healthcare_data.csv")
# Aggregate data for the pie chart
pie_data = df.groupby('Gender')['Cost'].sum()
# Plot the pie chart for 'Cost' by 'Gender'
plt.figure(figsize=(8, 8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Pie Chart of Cost by Gender')
plt.show()