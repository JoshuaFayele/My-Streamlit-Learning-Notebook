import streamlit as st

# Load EDA Packages
import pandas as pd


def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    #  The page hierarchy seemed to be the problem.
    #  I righ-clicked on the csv and copied the path 
    df = pd.read_csv("multi_app\data\heart-disease.csv")
    st.dataframe(df)