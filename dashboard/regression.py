import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st
from sklearn.preprocessing import LabelEncoder


def show_regression(df):

    st.sidebar.markdown("## Options")

    # one hot encoding for 'location'
    df[['location']] = df[['location']].apply(LabelEncoder().fit_transform)

    # define all parameters
    possible_param = ['location', 'gender', 'MinimalRadius', 'VelocityAtMinRadius', 'VelocityAtTurnEntry',
                      'VelocityAtTurnExit', 'GATEDISTANCE', 'dist2Dtonext', 'STEEPNESS',
                      'azitonext', 'slopechangetonext', 'angletonext', 'projtonext',
                      'dist3Dtonextnext', 'dts2Dtonextnext', 'slopetonextnext',
                      'azitonextnext', 'HORIZONTALGATEDISTANCE', 'VERTICALGATEDISTANCE',
                      ]

    # 'steepness_A'

    # define parameters (x) and response variable (y)
    x = df[possible_param]
    y = df[['TimeStarttoEnd_2']]

    # define random state
    RANDOM_STATE = 89389

    # define train test split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=RANDOM_STATE)

    # create default values
    unique_loc = df["location"].unique().tolist()
    unique_gender = df["gender"].unique().tolist()
    avg_MinRad = df["MinimalRadius"].mean()
    avg_VelocityAtMinRadius = df["VelocityAtMinRadius"].mean()
    avg_VelocityAtTurnEntry = df["VelocityAtTurnEntry"].mean()
    avg_VelocityAtTurnExit = df["VelocityAtTurnExit"].mean()
    avg_HORIZONTALGATEDISTANCE = df["HORIZONTALGATEDISTANCE"].mean()
    avg_VERTICALGATEDISTANCE = df["VERTICALGATEDISTANCE"].mean()
    avg_STEEPNESS = df["STEEPNESS"].mean()
    avg_GATEDISTANCE = df["GATEDISTANCE"].mean()
    avg_dist2Dtonext = df["dist2Dtonext"].mean()
    avg_azitonext = df["azitonext"].mean()
    avg_slopechangetonext = df["slopechangetonext"].mean()
    avg_angletonext = df["angletonext"].mean()
    avg_projtonext = df["projtonext"].mean()
    avg_dist3Dtonextnext = df["dist3Dtonextnext"].mean()
    avg_dts2Dtonextnext = df["dts2Dtonextnext"].mean()
    avg_slopetonextnext = df["slopetonextnext"].mean()
    avg_azitonextnext = df["azitonextnext"].mean()
    # avg_steepness_A = df["steepness_A"].mean()

    # new values for prediction
    pred_location = st.sidebar.radio("Select location:", unique_loc, index=0)
    pred_gender = st.sidebar.radio("Select gender:", unique_gender, index=0)
    pred_MinimalRadius = st.sidebar.number_input('Enter MinimalRadius', value=avg_MinRad)
    pred_VelocityAtMinRadius = st.sidebar.number_input('Enter VelocityAtMinRadius', value=avg_VelocityAtMinRadius)
    pred_VelocityAtTurnEntry = st.sidebar.number_input('Enter VelocityAtTurnEntry', value=avg_VelocityAtTurnEntry)
    pred_VelocityAtTurnExit = st.sidebar.number_input('Enter VelocityAtTurnExit', value=avg_VelocityAtTurnExit)
    pred_HORIZONTALGATEDISTANCE = st.sidebar.number_input('Enter HorizontalGateDistanze',
                                                          value=avg_HORIZONTALGATEDISTANCE)
    pred_VERTICALGATEDISTANCE = st.sidebar.number_input('Enter VerticalGateDistance', value=avg_VERTICALGATEDISTANCE)
    pred_STEEPNESS = st.sidebar.number_input('Enter Steepness', value=avg_STEEPNESS)
    pred_GATEDISTANCE = st.sidebar.number_input('Enter GateDistance', value=avg_GATEDISTANCE)
    pred_dist2Dtonext = st.sidebar.number_input('Enter dist2Dtonext', value=avg_dist2Dtonext)
    pred_azitonext = st.sidebar.number_input('Enter Azitonext', value=avg_azitonext)
    pred_slopechangetonext = st.sidebar.number_input('Enter Slopechangetonext', value=avg_slopechangetonext)
    pred_angletonext = st.sidebar.number_input('Enter Angletonext', value=avg_angletonext)
    pred_projtonext = st.sidebar.number_input('Enter Projtonext', value=avg_projtonext)
    pred_dist3Dtonextnext = st.sidebar.number_input('Enter dist3Dtonextnext', value=avg_dist3Dtonextnext)
    pred_dts2Dtonextnext = st.sidebar.number_input('Enter dts2Dtonextnext', value=avg_dts2Dtonextnext)
    pred_slopetonextnext = st.sidebar.number_input('Enter Slopetonextnext', value=avg_slopetonextnext)
    pred_azitonextnext = st.sidebar.number_input('Enter Azitonextnext', value=avg_azitonextnext)
    # pred_steepness_A = st.sidebar.number_input('Enter Steepness_A', value=avg_steepness_A)

    # run the model
    model = MultiOutputRegressor(LinearRegression()).fit(X_train, y_train)

    with st.form("reg_form"):
        predict = st.form_submit_button("Predict")
        if predict:
            result = model.predict([[pred_location, pred_gender, pred_MinimalRadius, pred_VelocityAtMinRadius,
                                     pred_VelocityAtTurnEntry, pred_VelocityAtTurnExit, pred_HORIZONTALGATEDISTANCE,
                                     pred_VERTICALGATEDISTANCE, pred_STEEPNESS, pred_GATEDISTANCE, pred_dist2Dtonext,
                                     pred_azitonext, pred_slopechangetonext, pred_angletonext, pred_projtonext,
                                     pred_dist3Dtonextnext, pred_dts2Dtonextnext, pred_slopetonextnext,
                                     pred_azitonextnext]])
            st.text(result)

    # pred_steepness_A
