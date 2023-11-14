# Core Packages
import streamlit as st

# Import the mini Apps
import eda_app 

def main():
    st.title("Main App")
    
    menu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
    elif choice == "EDA":
        eda_app.run_eda_app()
    elif choice == "ML":
        pass
    else:
        st.subheader("About")


if __name__ == '__main__':
    main()