import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from mpl_toolkits import mplot3d
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable

st.set_page_config(layout="wide")

st.sidebar.markdown("## Filter options")

path = "Runs Computed"

@st.cache
def get_list():
    files = os.listdir(path)
    filename_split_list = []
    for file in files:
        if re.match('[0-9]{6}_[0-9]_.*\\.csv', file):
            filename_split = file.split('.')[0].split('_')
            filename_split_list.append(filename_split)
    df_filenames = pd.DataFrame(filename_split_list).rename({0: 'date', 1: 'athlete', 2: 'run'}, axis=1)
    return df_filenames
    

possible_dates = get_list()['date'].unique()
possible_dates.sort()

selected_date = st.sidebar.selectbox('Select the Date', options=possible_dates)

possible_athletes = get_list()[get_list()['date'] == selected_date]['athlete'].unique()
possible_athletes.sort()

selected_athlete = st.sidebar.selectbox('Select the Athlete', options=possible_athletes)

possible_runs = get_list()[(get_list()['date'] == selected_date) & (get_list()['athlete'] == selected_athlete)]['run'].unique()

possible_runs.sort()

selected_run = st.sidebar.selectbox('Select the Run', options=possible_runs)

st.title('Descriptive Analysis')




############## COURSE ELEVATION PROFILE #################


df = pd.read_csv(f'Runs Computed/{selected_date}_{selected_athlete}_{selected_run}.csv')

x_coordinates = []
y_coordinates = []
z_coordinates = []
time_list= []
speed = []

for xpoint in df['xPos[m]']:
    x_coordinates.append(xpoint)

for ypoint in df['yPos[m]']:
    y_coordinates.append(ypoint)
    
for zpoint in df['zPos[m]']:
    z_coordinates.append(zpoint)
    
for velocity in df['speed[m/s]']:
    speed.append(velocity)
    
for time in df['time[s]']:
    time_list.append(time)
    
fig = plt.figure(figsize=(20,20))
ax = fig.gca(projection='3d')
x = x_coordinates
y = y_coordinates
z = z_coordinates
scat_plot = ax.scatter(xs = x_coordinates, ys = y_coordinates, zs = z_coordinates, c=speed, linewidth=2, cmap="viridis")
plt.gca().invert_zaxis()
ax.set_xlabel("x position", size=15)
ax.set_ylabel("y position", size=15)
ax.set_zlabel("Absolute Elevation [m.a.s.l]", size=15)
ax.view_init(-170, -80)
ax.grid(True)
cb = plt.colorbar(scat_plot, shrink=0.5)
cb.set_label('Speed [m/s]',size=18)
plt.show()
st.pyplot(fig)

sns.set_style("whitegrid")
cmap = sns.cubehelix_palette(as_cmap=True)
fig, ax1 = plt.subplots(figsize=(15,8))
points = ax1.scatter(x=time_list, y=z_coordinates, c=speed, s=3, cmap="viridis")
fig.colorbar(points, label='Speed [m/s]')
ax1.set(xlabel='Time [s]', ylabel='Absolute Elevation [m.a.s.l]')
ax1.set_title("Course Elevation Profile ", size=20)
st.pyplot(fig)