import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\dmt\ex16\healthcare_data.csv")
# Plot the box plot for the 'Cost' column
plt.figure(figsize=(8, 6))
plt.boxplot(df['Cost'])
plt.title('Box Plot of Cost')
plt.ylabel('Cost')
plt.show()