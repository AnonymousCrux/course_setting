import matplotlib.pyplot as plt
import streamlit as st


def show_runs_in_location(df):
    st.title('Runs in location')

    st.sidebar.markdown("## Filter options")

    selectedLocation = st.sidebar.selectbox('Select the location',
                                            df['location'].unique())

    dfRunsPerAthleteFilteredByLocation = df[df['location'] == selectedLocation]
    dfRunsPerAthlete = dfRunsPerAthleteFilteredByLocation[['athlete', 'TurnNr', 'run']].groupby(
        ['athlete', 'TurnNr']).agg('count').rename({'run': 'runCount'}, axis=1).reset_index()
    dfRunsPerAthlete = dfRunsPerAthlete.pivot(index='TurnNr', columns='athlete', values='runCount')

    fig, ax = plt.subplots(figsize=(10, 5))
    axRunsPerAthlete = dfRunsPerAthlete.plot(kind="bar", ax=ax, width=0.8)
    plt.tight_layout()
    plt.title(f"Runs in {selectedLocation}")
    plt.xlabel("Turn number")
    plt.ylabel("Number of runs")
    st.pyplot(fig)
