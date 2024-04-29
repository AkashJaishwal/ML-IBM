import pandas as pd 
filepath = 'Week 2\\cs.json'

# read a file 
data = pd.read_json(filepath)

# Write dataframe file to JSON
data.to_json('Week 2\\outputfile.json')
# print the values
# print(data.iloc[:5])