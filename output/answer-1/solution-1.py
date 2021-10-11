import numpy as np
import pandas as pd
data = pd.read_csv('main.csv')
new_data = pd.DataFrame(columns=data.columns)
i = 0
for d in pd.read_csv('main.csv', iterator=True, chunksize=10):
    new_data.loc[i] = d.sum(axis=0)
    new_data.loc[i]['Year'] = d.reset_index()['Year'][0]
    new_data.loc[i]['Population'] = d.reset_index(
    )['Population'][len(d.reset_index()['Population']) - 1]
    i += 1

new_data.drop(['Total'], axis=1).to_csv('answer-1.csv', index=False)