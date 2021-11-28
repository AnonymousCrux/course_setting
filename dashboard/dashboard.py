import pandas as pd
import streamlit as st

from correlation import show_corr
from dim_reduction import show_tsne
from track_visualisation import show_track_visualisation

st.set_page_config(layout="wide")


@st.cache
def load_data():
    return pd.read_excel('Data/bereinigte_DATEN_ano.xlsx')


df = load_data()

pages = {"Track visualisation": 1, "Correlation": 2, "t-SNE": 3}

selected_page = st.sidebar.selectbox('Select the page', options=pages.keys())

if pages[selected_page] == 1:
    show_track_visualisation()
elif pages[selected_page] == 2:
    show_corr(df)
elif pages[selected_page] == 3:
    show_tsne(df)
