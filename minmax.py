import numpy as np
import pandas as pd
# Function to perform Min-Max Normalization
def min_max_normalization(data, new_min=0, new_max=1):
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data)) * (new_max - new_min) + new_min
    return normalized_data
# Read data from CSV file
file_path = r"C:\Users\HP\Desktop\dmt\data.csv"  # Replace with your file path
data = pd.read_csv(file_path)
# Display the original data
print("Original Data:\n", data)
# Applying Min-Max Normalization to each column
normalized_data = data.apply(min_max_normalization)
# Display the normalized data
print("\nNormalized Data:\n", normalized_data)