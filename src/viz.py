import streamlit as st
from pathlib import Path
import pandas as pd  

def app():
    st.title("🐧 Let's Explore Our Penguin Data")

    with st.expander("ℹ️ Take a quick glance at the data"):
        st.write("Here’s the raw penguins dataset preview.")
        st.write(pd.read_csv(r"src\data\penguins.csv"))

    # Base directory for images
    BASE_DIR = Path(r"deployed_app\src\images")

    # List PNG/JPG files in the folder
    image_files = sorted([f for f in BASE_DIR.iterdir() if f.suffix.lower() in [".png", ".jpg", ".jpeg"]])

    st.markdown("### 📊 Visual Exploration")

    # Loop through in pairs (2 per row)
    for i in range(0, len(image_files), 2):
        col1, col2 = st.columns(2)

        with col1:
            st.image(image_files[i], use_container_width=True)

        # Check if there's a next image (in case of odd number of files)
        if i + 1 < len(image_files):
            with col2:
                st.image(image_files[i+1], use_container_width=True)

        # Example explanation for each row
        st.info(f"📌 Observation: Insights from {image_files[i].name} and {image_files[i+1].name if i+1 < len(image_files) else ''} go here.")
