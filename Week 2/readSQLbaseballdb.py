import pandas as pd
import sqlite3 as sq3
import pandas.io.sql as pds

# Download the database
# !wget -P data https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/baseball.db

# Create a variable, 'path', containing the path to the 'baseball.db' contained in 'resources/'
path = 'Week 2//data//baseball.db'

# Create a connection, 'con', that is connected to database at 'path'
con=sq3.Connection(path)

#Create a variable, 'query'm containing a SQL query which  reads in all data from the 'table'
query='''SELECT * FROM allstarfull;'''

allstar_observation =pd.read_sql(query, con)

#print (allstar_observation)

# Create a variable, tables, which reads in all data from the table sqlite_master
all_tables = pd.read_sql('SELECT * FROM sqlite_master', con)
print(all_tables)

# Pretend that you were interesting in creating a new baseball hall of fame. Join and analyze the tables to evaluate the top 3 all time best baseball players
best_query = """
SELECT playerID, sum(GP) AS num_games_played, AVG(startingPos) AS avg_starting_position
    FROM allstarfull
    GROUP BY playerID
    ORDER BY num_games_played DESC, avg_starting_position ASC
    LIMIT 3
"""
best = pd.read_sql(best_query, con)
print(best.head())
### END SOLUTION

