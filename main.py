
from src.home import app as a
from src.predict import app as b
from src.viz import app as c

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
    a()   # call homepage function
elif choice == "Predict":
    b()
else:
    c()    # call contact function
