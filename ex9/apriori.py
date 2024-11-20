# Write a Python program to generate frequent item sets / association rules using Apriori algorithm

# !pip install mlxtend

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
csv_file_path = r"C:\Users\HP\Desktop\dmt\ex9\items.csv" 
df = pd.read_csv(csv_file_path)
min_support = 0.6 
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
min_confidence = 0.7 
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence,num_itemsets=2)
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)