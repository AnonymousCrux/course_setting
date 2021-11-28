import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.manifold import TSNE


def show_tsne(df):
    st.title('T-sne clustering')

    st.sidebar.markdown("## Options")

    ## create location and turn sets
    locations_and_turns = df[['location', 'TurnNr']]
    turn_no = df['TurnNr'].unique()
    location_set = df['location'].unique()

    ## create stream lit dashboard to select location and turn
    selected_location = st.sidebar.radio(
        "What's the location you want to inspect?",
        location_set)

    df = df.loc[df['location'] == selected_location]
    min_turn = min(df['TurnNr'])
    max_turn = max(df['TurnNr'])

    selected_turn = st.sidebar.slider('Which turn would you like to see?', min_turn, max_turn, 2)

    df = df.loc[df['TurnNr'] == selected_turn]

    ## remove unneeded columns
    df_clean = df.drop(
        ["date", "location", "Unnamed0", "vectortonext", "vector2Dtonext", "vectortonextnorm", "vector2Dtonextnorm",
         "projpttonext", "vectortonextnext", "vector2Dtonextnext", "vectortonextnextnorm", "vector2Dtonextnextnorm"],
        axis=1)

    ## assing feature columns
    features = df_clean.columns[4:17]

    # distribute the dataset into two components X and Y
    x = df_clean.iloc[:, 4:17]
    y = df_clean.iloc[:, 2]

    ## define number of components
    n_components = 2
    tsne = TSNE(n_components)
    tsne_result = tsne.fit_transform(x)

    sns.color_palette("rocket", n_colors=8)
    # Plot the result of our TSNE with the label color coded
    # A lot of the stuff here is about making the plot look pretty and not TSNE
    tsne_result_df = pd.DataFrame({'tsne_1': tsne_result[:, 0], 'tsne_2': tsne_result[:, 1], 'label': y})
    fig, ax = plt.subplots(1)
    sns.scatterplot(x='tsne_1', y='tsne_2', hue='label', data=tsne_result_df, ax=ax, s=120, palette="colorblind")
    lim = (tsne_result.min() - 5, tsne_result.max() + 5)
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect('equal')
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)
    st.pyplot(fig)
