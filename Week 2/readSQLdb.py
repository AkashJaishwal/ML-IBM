import sqlite3 as sq3
import pandas as pd

# Initialize path to SQLite database
path = 'Weeks 2\\cs.db'

# Create connection SQL database
con = sq3.Connection(path)

# Write query 
query = '''SELECT * FROM rock_songs;'''

# Execute query 
data = pd.read_sql(query, con)