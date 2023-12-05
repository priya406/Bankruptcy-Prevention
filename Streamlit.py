import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("model_poly.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome ALL"
def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
     prediction=classifier.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
     print(prediction)
     return prediction





def main():
    st.title("Bankruptcy Detector")
    html_temp = """
    <div style="background-color:#cdb4db;padding:10px">
    <h2 style="color:white;text-align:center;">Bankruptcy Detector</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    industrial_risk = st.slider("Industrial Risk", 0.0, 1.0, step=0.01, value=0.5)
    management_risk = st.slider("Management Risk", 0.0, 1.0, step=0.01, value=0.5)
    financial_flexibility = st.slider("Financial Flexibility", 0.0, 1.0, step=0.01, value=0.5)
    credibility = st.slider("Credibility", 0.0, 1.0, step=0.01, value=0.5)
    competitiveness = st.slider("Competitiveness", 0.0, 1.0, step=0.01, value=0.5)
    operating_risk = st.slider("Operating Risk", 0.0, 1.0, step=0.01, value=0.5)
    result=""
    if st.button("Predict"):
        prediction = predict_bankruptcy(
            industrial_risk, management_risk, financial_flexibility,
            credibility, competitiveness, operating_risk
        )
        if prediction == 0:
            result = "The company is bankrupted"
        else:
            result = "The company is not bankrupted"
    
    st.success('Prediction: {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
