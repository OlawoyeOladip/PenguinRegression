import pickle
import pandas as pd
import streamlit as st

# Load trained model and scaler
with open('artifact/model.pkl', 'rb') as file:
    model = pickle.load(file)

with open("artifact/scaler.pkl", 'rb') as file:
    scaling = pickle.load(file)

def app():
    st.title("🐧 Penguin Body Mass Prediction")

    st.markdown("### Enter Penguin Details")

    # User inputs
    species = st.selectbox("Species", ["Adelie", "Chinstrap", "Gentoo"])
    island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    bill_length_mm = st.number_input("Bill Length (mm)", min_value=30.0, max_value=70.0, step=0.1)
    bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=10.0, max_value=25.0, step=0.1)
    flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=150, max_value=250, step=1)
    body_mass_g = st.number_input("Body Mass (g)", min_value=2000, max_value=7000, step=10)

    if st.button("Predict Body Mass"):
        # Create DataFrame from inputs
        input_df = pd.DataFrame([{
            "species": species,
            "island": island,
            "sex": sex,
            "bill_length_mm": bill_length_mm,
            "bill_depth_mm": bill_depth_mm,
            "flipper_length_mm": flipper_length_mm,
            "body_mass_g": body_mass_g
        }])

        # 🔹 Feature Engineering
        input_df['Area'] = input_df['bill_length_mm'] * input_df['bill_depth_mm']
        input_df['volume_mm3'] = input_df['Area'] * input_df['bill_depth_mm']

        # 🔹 One-Hot Encoding
        input_encoded = pd.get_dummies(input_df)

        # Ensure the encoded input has same columns as training
        # Fill missing dummy columns if any
        expected_cols = scaling.feature_names_in_  # from fitted scaler
        for col in expected_cols:
            if col not in input_encoded:
                input_encoded[col] = 0

        # Reorder columns to match scaler/model
        input_encoded = input_encoded[expected_cols]

        # 🔹 Apply scaling
        input_scaled = scaling.transform(input_encoded)

        st.subheader("Engineered & Encoded Features")
        st.write(pd.DataFrame(input_scaled, columns=expected_cols))

        # 🔹 Make prediction
        prediction = model.predict(input_scaled)
        st.success(f"🐧 Predicted Body Mass: {prediction[0]:.2f} g")
