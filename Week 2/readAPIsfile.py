import pandas as pd
#UCI Cars data set -url location
data_url= 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

#Read data into pandas
df = pd.read_csv(data_url, header = None)
