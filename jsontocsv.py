import pandas as pd

with open('stations.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('stations.csv', encoding='utf-8', index=False)
