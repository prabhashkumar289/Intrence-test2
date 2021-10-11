import numpy as np
import pandas as pd
data = pd.read_csv('main.csv')
data[['Team', 'Yellow Cards', 'Red Cards']].sort_values(
    by=['Red Cards'], ascending=False).to_csv('answer-3.csv', index=False)