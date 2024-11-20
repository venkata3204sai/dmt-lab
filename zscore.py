import pandas as pd
# Function to perform Z-score Normalization
def z_score_normalization(data):
    normalized_data = (data - data.mean()) / data.std()
    return normalized_data
# Read data from CSV file
file_path = r"C:\Users\HP\Desktop\dmt\data.csv"  # Replace with your file path
data = pd.read_csv(file_path)
# Display the original data
print("Original Data:\n", data)
# Applying Z-score Normalization to each column
normalized_data = data.apply(z_score_normalization)
# Display the normalized data
print("\nZ-score Normalized Data:\n", normalized_data)