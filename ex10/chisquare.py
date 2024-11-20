# Write a program to calculate chi-square value using Python/R. Report your observation.

import pandas as pd 
from scipy.stats import chi2_contingency 
# Path to the CSV file 
file_path = r"C:\Users\HP\Desktop\dmt\ex10\a.csv" 
# Read data from CSV file 
df = pd.read_csv(file_path, header=None) 
# Convert DataFrame to a list of lists 
data = df.values.tolist() 
# Perform Chi-square test 
stat, p, dof, expected = chi2_contingency(data) 
# Interpret p-value 
alpha = 0.05 
print("Chi-square statistic:", stat) 
print("p value is:", p) 
print("Degrees of freedom:", dof) 
print("Expected frequencies table:") 
print(expected) 
if p <= alpha: 
    print('The data is correlated (reject H0)') 
else: 
    print('The data is not correlated (H0 holds true)')