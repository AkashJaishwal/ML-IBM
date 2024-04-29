import pandas as pd 

filepath = 'D:\\Acadamic\\ML IBM\\Week 2\\CS 21-25.csv'

#import the data
# data = pd.read_csv(filepath) # 'data' is a variable which store the value in it form the filepath

data = pd.read_csv(filepath, names=['Roll NO.', 'Student Name', 'Program']) #used to specify the heading of the column or to give the name to the coumn 

#print a few rows 
print (data.iloc[:5]) #we have accessed the file data and printed the rows

## Useful arguements 

# # Different delimiters - tab-separated file (.tsv):
# data = pd.read_csv(filepath, sep='\t')

# # Different delimiters - space-sepated file:
# data = pd.read_csv(filepath, delim_whitespace=True)

# #Don't use first row for coumn names
# data = pd.read_csv(filepath, header=None)

# #Specify column names:
# data = pd.read_csv(filepath, names=['Name1', 'Name2'])

# #custome missing vales:
# data = pd.read_csv(filepath, na_values=['NA'])
