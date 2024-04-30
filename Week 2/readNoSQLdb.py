# SQL DAta imports
from pymongo import MongoClient

# We first make a connection with the database (MongoDB needs to be running).
# Create a Mango Connection
con = MongoClient()

# Data is read into pandas by combining a query with this connection.
# Create database (con.list_database_name() will display available database)
db = con.database_name

# Create a cursor object using a query
cursor = db.collection_name.find(query) # Here, query should be replaced with a MongoDB query string (or { } to select all).

# Expand cursor and construct DataFrame
df = db.DataFrame(list(cursor))
