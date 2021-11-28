import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


def show_corr(df):
    st.sidebar.markdown("## Options")

    sns.color_palette("colorblind")
    sns.set(rc={"figure.figsize": (5, 5)})

    df_clean = df.drop(
        ["Unnamed: 0", "V1", "date", "vectortonext", "vector2Dtonext", "vectortonextnorm", "vector2Dtonextnorm",
         "projpttonext", "vectortonextnext", "vector2Dtonextnext", "vectortonextnextnorm", "vector2Dtonextnextnorm",
         'DistanzSchätz', 'Zehen1_Fersen2', '@2Ferse_3Zehe_4Ferse', 'filter_$', 'goofy2_regular1', 'athlete', 'run'],
        axis=1)

    possible_param = df_clean.columns.tolist()

    parameters = st.sidebar.multiselect('Which parameters would you like to inspect?', possible_param,
                                        ["VelocityAtTurnExit", "VelocityAtTurnEntry", "STEEPNESS"])

    possible_loc = df["location"].unique().tolist()

    locations = st.sidebar.multiselect('What location(s) would you like to inspect?', possible_loc, "Zermatt")

    possible_ath = df["athlete"].unique().tolist()

    athletes = st.sidebar.multiselect('What athlete(s) do you like to inspect?', possible_ath, default=possible_ath)

    # create subset
    df_clean = df_clean[parameters]
    df_clean = df_clean.loc[df["location"].isin(locations)]
    df_clean = df_clean.loc[df["athlete"].isin(athletes)]

    corr = df_clean.corr()
    fig, ax = plt.subplots(1)
    ax = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True,
        cbar_kws={"shrink": 0.75},
        annot=True
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    );
    st.pyplot(fig)
