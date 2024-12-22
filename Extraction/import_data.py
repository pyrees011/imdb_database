import pandas as pd

imdb_data = pd.read_csv('title.principals.tsv', sep='\t', nrows=50, skiprows=500000)

print(imdb_data)