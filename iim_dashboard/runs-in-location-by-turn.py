import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

@st.cache
def load_data():
    return pd.read_excel("Data/bereinigte_DATEN_ano.xlsx")

df = load_data()

st.title('Descriptive Analysis')

st.sidebar.markdown("## Filter options")

selectedLocation = st.sidebar.selectbox('Select the location',
                                    df['location'].unique())

dfRunsPerAthleteFilteredByLocation = df[df['location'] == selectedLocation]
dfRunsPerAthlete = dfRunsPerAthleteFilteredByLocation[['athlete', 'TurnNr', 'run']].groupby(['athlete', 'TurnNr']).agg('count').rename({'run':'runCount'}, axis=1).reset_index()
dfRunsPerAthlete = dfRunsPerAthlete.pivot(index='TurnNr', columns='athlete', values='runCount')

fig, ax = plt.subplots(figsize=(10, 5))
axRunsPerAthlete = dfRunsPerAthlete.plot(kind="bar", ax=ax, width=0.8)
plt.tight_layout()
plt.title(f"Runs in {selectedLocation}")
plt.xlabel("Turn number")
plt.ylabel("Number of runs")
st.pyplot(fig)
