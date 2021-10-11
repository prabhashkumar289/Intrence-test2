import numpy as np
import pandas as pd
data = pd.read_csv('main.csv')
new_data = data.groupby('occupation').agg({'age': ['min', 'max']})
new_data.to_csv('answer-2.csv', index=False)