import pandas as pd 
import sqlite3 as sq3

filepath = 'D:\\Acadamic\\ML IBM\\Week 2\\CS 21-25.csv'

#import the data
data = pd.read_csv(filepath) # 'data' is a variable which store the value in it form the filepath

#print a few rows 
print (data.iloc[:5]) #we have accessed the file data and printed the rows

#write data to new file or existing
data.to_json('Week 2\\cs21-25.json')

data.to_sql('Week 2\\cs21-25.db')
