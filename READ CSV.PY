import pandas as pd
data = pd.read_csv("metadata.tsv",sep = '\t', names = ['a','b','c','d','e','r'])
print(data)