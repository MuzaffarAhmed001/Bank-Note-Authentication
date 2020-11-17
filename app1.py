#Creating Flask App
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

def home():
    return 'Welcome'

           

def predict_note_authentication(variance,skewness,entropy,curtosis):
    
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return 'The predicted  value is'+str(prediction)

def main():
    st.title('Bank Authentication')
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticatior ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("Variance","Type Here")
    skewness=st.text_input('Skewness',"Type Here")
    curtosis=st.text_input('curtosis',"Type Here")
    entropy=st.text_input('Entropy','Type Here')
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,entropy,curtosis)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text('Lets Earn')
        st.text('Build with Streamlit')

if __name__=='__main__':
    main()
    