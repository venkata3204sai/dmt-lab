import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\dmt\ex16\healthcare_data.csv")
# Plot the bar chart for 'Visits' by 'Region'
plt.figure(figsize=(10, 6))
df.groupby('Region')['Visits'].sum().plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Bar Chart of Visits by Region')
plt.xlabel('Region')
plt.ylabel('Total Visits')
plt.show()