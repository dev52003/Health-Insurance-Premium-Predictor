import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Page config
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🛡️",
    layout="centered"
)

# Simple custom CSS
st.markdown("""
<style>
.main-title {
    text-align: center;
    color: #2c3e50;
    font-size: 2.5rem;
    margin-bottom: 2rem;
    font-weight: 600;
}

.result-box {
    background: #f8f9fa;
    border-left: 5px solid #28a745;
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1.5rem 0;
}

.result-amount {
    font-size: 2rem;
    font-weight: bold;
    color: #28a745;
    text-align: center;
}

.error-box {
    background: #fff5f5;
    border-left: 5px solid #e53e3e;
    padding: 1rem;
    border-radius: 8px;
    color: #e53e3e;
    margin: 1rem 0;
}

.stButton > button {
    width: 100%;
    background: #007bff;
    color: white;
    border: none;
    padding: 0.75rem;
    border-radius: 8px;
    font-size: 1.1rem;
    margin-top: 1rem;
}

.stButton > button:hover {
    background: #0056b3;
}
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_data
def load_model():
    try:
        with open('model.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("Model file not found.")
        return None

# Main app
def show_predict_page():
    # Title
    st.markdown('<h1 class="main-title">🛡️ Insurance Premium Predictor</h1>', unsafe_allow_html=True)
    
    # Form
    with st.form('prediction_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.text_input('Age', placeholder='e.g., 30')
            bmi = st.text_input('BMI', placeholder='e.g., 25.5')
            children = st.text_input('Children', placeholder='e.g., 2')
        
        with col2:
            sex = st.selectbox("Gender", ['Male', 'Female'])
            smoker = st.selectbox('Smoker', ['No', 'Yes'])
            region = st.selectbox('Region', ['Northeast', 'Northwest', 'Southeast', 'Southwest'])
        
        predict = st.form_submit_button("Predict Premium")
        
        if predict:
            # Validate inputs
            if not all([age, bmi, children]):
                st.markdown('<div class="error-box">Please fill in all fields.</div>', unsafe_allow_html=True)
                return
            
            try:
                # Convert inputs
                age_val = int(age)
                bmi_val = float(bmi)
                children_val = int(children)
                
                # Basic validation
                if not (0 <= age_val <= 120):
                    st.markdown('<div class="error-box">Age must be between 0 and 120.</div>', unsafe_allow_html=True)
                    return
                if not (10 <= bmi_val <= 60):
                    st.markdown('<div class="error-box">BMI must be between 10 and 60.</div>', unsafe_allow_html=True)
                    return
                if not (0 <= children_val <= 20):
                    st.markdown('<div class="error-box">Children must be between 0 and 20.</div>', unsafe_allow_html=True)
                    return
                
                # Make prediction
                X = pd.DataFrame([[age_val, sex, bmi_val, children_val, smoker, region]], 
                               columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
                
                model = load_model()
                if model:
                    premium = model.predict(X)[0]
                    
                    # Display result
                    st.markdown(f'''
                    <div class="result-box">
                        <div class="result-amount">${premium:,.2f}</div>
                        <div style="text-align: center; margin-top: 0.5rem; color: #666;">
                            Annual Premium
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # Simple breakdown
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Monthly", f"${premium/12:,.2f}")
                    with col2:
                        st.metric("Daily", f"${premium/365:.2f}")
                
            except ValueError:
                st.markdown('<div class="error-box">Please enter valid numbers for age, BMI, and children.</div>', unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="error-box">Error: {str(e)}</div>', unsafe_allow_html=True)

# Run app
if __name__ == "__main__":
    show_predict_page()