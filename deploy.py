import streamlit as st
import joblib
import time
model = joblib.load("model.joblib")

st.markdown(f"<h1 style='text-align:center'>AI Text Detection</h1>", unsafe_allow_html=True)

user_input = st.text_area('', placeholder="Enter text to analyze", height=200)

threshold = 0.6
den = 1-threshold
if st.button("Analyze"):
    text_placeholder = st.empty()    
    prog = st.progress(0, text='0')
    if user_input.strip():
        proba = model.predict_proba([user_input])[0][1]
        if proba >= threshold:
            indic = 0.5 + ((proba-threshold)/den) * 0.5
        else:
            indic = (proba/threshold) * 0.5
        
    indic = max(0.0, min(1.0, indic))
    
    for i in range(int(indic*100)):
        text_placeholder.markdown(f"<h4 style='text-align:center'>{i + 1}%</h4>", unsafe_allow_html=True)
        prog.progress(i+1)
        time.sleep(0.01)
    
    if proba>=threshold:
        st.markdown("Text is most likely by an AI")
    else:
        st.markdown("Text is most likely by a Human")
