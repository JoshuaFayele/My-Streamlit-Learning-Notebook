# Plotting in Streamlit - Using st.pyplot for Matplotlib and Others

import streamlit as st

# Load EDA Packages
import pandas as pd
import numpy as np


# Load Data Viz Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #TkAgg
import seaborn as sns


def main():
    st.title("Plotting in Streamlit - Using st.pyplot for Matplotlib and Others")  
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
    # fig = plt.figure()
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot(fig)
    
    # Method 3
    # fig, ax = plt.subplots()
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot(fig)
    
    # Alternative for Matplotlib
    # fig = plt.figure()
    # sns.countplot(df['species'])
    # st.pyplot(fig)
    
    
    
if __name__ == '__main__':
    main()

# Plotting in Streamlit - Using Bar Charts, Area Charts and Altair Charts

# import streamlit as st

# EDA Packages
# import pandas as pd
# import numpy as np

# Import Altair
# import altair as alt


# def main():
#     st.title("Plotting in Streamlit - Using Bar Charts, Area Charts and Altair Charts")
#     # Load Dataset
#     # df = pd.read_csv("data/iris.csv")
#     df2 = pd.read_csv("data/lang_data.csv")
#     st.dataframe(df2.head())
    
    
    # Bar Chart
    # Using st.bar_chart
    # st.bar_chart(df[['sepal_length', 'petal_length']])
    
    # Line Chart      
    # lang_list = df2.columns.tolist()
    # lang_choices = st.multiselect("Choose Language", lang_list, default='Python')
    # new_df = df2[lang_choices]
    # st.line_chart(new_df)
    
    # Area Chart
    # st.area_chart(new_df, use_container_width=True)
        
    # Altair
    # df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
    # c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    # st.dataframe(df.head())
    
    # Method 1: Using Write
    # st.write(c)
    
    # Method 2: Using st.altair_chart
    # st.altair_chart(c, use_container_width=True)
          
    
# if __name__ == '__main__':
#     main()



# Plotting In Streamlit - Using Plotly

# import streamlit as st

# EDA Packages
# import pandas as pd
# import numpy as np

# # Load Data Vizualization Packages
# import plotly.express as px

# def main():
#     st.title("Plotting in Streamlit - Using Plotly")
#     df = pd.read_csv("data/prog_languages_data.csv")
#     st.dataframe(df)
    
#     fig = px.pie(df, values='Sum', names='lang', title='Pie Chart of Languages')
#     st.plotly_chart(fig)
    
#     fig2 = px.bar(df, x='lang', y='Sum')
#     st.plotly_chart(fig2)
    
    
# if __name__ == '__main__':
#     main()