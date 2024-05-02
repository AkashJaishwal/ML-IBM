# We can also run any supported SQL query
# # Write the query
# query = '''
# SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) AS avg_plays  
#     FROM rock_songs
#     GROUP BY Artist, Release_Year
#     ORDER BY num_songs desc;
# '''
