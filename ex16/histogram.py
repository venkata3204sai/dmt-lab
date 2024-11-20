import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\dmt\ex16\healthcare_data.csv")
# Plot the histogram for the 'Age' column
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()