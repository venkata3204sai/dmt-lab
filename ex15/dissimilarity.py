# Write a program to compute/display dissimilarity matrix (for your own dataset containing at least four instances with two attributes) using Python 

import numpy as np 
import pandas as pd 
from scipy.spatial.distance import pdist, squareform 
# Load the dataset from a CSV file 
df = pd.read_csv(r"C:\Users\HP\Desktop\dmt\ex15\dissimilarity_matrix.csv") 
# Display the dataset 
print("Dataset:") 
print(df) 
# Convert the DataFrame to a NumPy array 
data = df.values 
# Compute the pairwise Euclidean distances between the instances 
dissimilarity_matrix = squareform(pdist(data, metric='euclidean')) 
# Display the dissimilarity matrix 
print("\nDissimilarity Matrix (Euclidean Distance):") 
dissimilarity_df = pd.DataFrame(dissimilarity_matrix, index=range(1, len(data) + 1), 
columns=range(1, len(data) + 1)) 
print(dissimilarity_df) 
# Save the dissimilarity matrix to a CSV file 
dissimilarity_df.to_csv("dissimilarity_matrix.csv", index=True)