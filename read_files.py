import os
import re

import pandas as pd

path = "Runs Computed"

files = os.listdir(path)
filename_split_list = []
for file in files:
    if re.match('[0-9]{6}_[0-9]_.*\\.csv', file):
        filename_split = file.split('.')[0].split('_')
        filename_split_list.append(filename_split)

df_filenames = pd.DataFrame(filename_split_list).rename({0: 'date', 1: 'athlete', 2: 'run'}, axis=1)

possible_dates = df_filenames['date'].unique()

selected_date = '200908'

possible_athletes = df_filenames[df_filenames['date'] == selected_date].unique()

print(possible_athletes)
