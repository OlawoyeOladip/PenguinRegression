import streamlit as st

def app():
    st.title("🐧 Penguin Body Mass Prediction App")

    # Display penguin image (you can replace the URL with a local file if available)
    st.image(
        "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png",
        caption="Palmer Penguins Dataset",
        use_container_width=True
    )

    st.markdown(
        """
        Welcome to the **Penguin Body Mass Prediction App**!  
        
        This app helps you explore the fascinating Palmer Penguins dataset and **predict the body mass of penguins**
        using features such as:

        - 🪶 Bill length  
        - 🪶 Bill depth  
        - 🪶 Flipper length  
        - 🪶 Species and Sex  

        ### 🌍 Why Penguins?
        Penguins are an excellent case study in biology and data science because they provide rich,
        real-world data for understanding species differences and making predictions.

        ### 🔮 What Can You Do Here?
        - 📊 Explore interactive visualizations of penguin features  
        - 🧮 Predict the body mass (`body_mass_g`) of a penguin  
        - 🔎 Compare patterns across different species and sexes  

        ---
        """
    )

    with st.expander("ℹ️ How to Use This App"):
        st.markdown(
            """
            1. Navigate to the **Project** page to upload or select penguin data.  
            2. View exploratory plots and relationships between penguin features.  
            3. Use the built-in model to **predict the body mass** of a penguin.  
            4. Check the **Contact** page if you'd like to reach out!  
            """
        )
    
    st.success("🐧 Ready to dive in? Use the sidebar to start exploring!")

