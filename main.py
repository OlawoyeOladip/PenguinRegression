
from src import predict, viz, home

import streamlit as st  
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Multi Page App",
    page_icon="❤️😊",
    layout="wide"
)

with st.sidebar:
    choice = option_menu(
        "Navigation", 
        ["HomePage", "Predict", "Visualization"],
        icons=["house", "database", "robot"]
    )
    
if choice == "HomePage":
    home.app()   # call homepage function
elif choice == "Predict":
    predict.app()
else:
    viz.app()    # call contact function
