import streamlit as st

# EDA Packages
import pandas as pd
import numpy as np

# Load Data Viz Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #TkAgg
import seaborn as sns


def main():
    # st.title("Plotting with St.Pyplot")
    st.title("Plotting in Streamlit")
    # Load Dataset
    df = pd.read_csv("data/iris.csv")
    
    st.dataframe(df.head())
    
    # Previous Method
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot()
    
    # plt.scatter(*np.random.random(size=(2,100)))
    # st.pyplot()
    
    # Recommended Method
    # fig, ax = plt.subplots()
    # ax.scatter(*np.random.random(size=(2,100)))
    # st.pyplot(fig)
    
    # Method 2: Simple Method
    fig = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig)
    
    # Method 3
    # fig, ax = plt.subplots()
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot(fig)
    
    # Alternative for Matplotlib
    # fig = plt.figure()
    # sns.countplot(df['species'])
    # st.pyplot(fig)
    
    # Bar Chart
    # Using st.bar_chart
    st.bar_chart(df['sepal_length'])
    
    
if __name__ == '__main__':
    main()