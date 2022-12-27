import streamlit as st

import joblib

model_nb = joblib.load('Fake_job_postings')
vect = joblib.load('vect.pkl')

def main():
  st.title('Fake Job Detection') #creates a title in web app
  ip = st.text_input('Enter Job Description:') #creates a text box in web app
  if st.button('Predict'):
    data=[ip]
    cv=vect.transform(data).toarray()
    prediction=model_nb.predict(cv)
    result=prediction[0]
    if result==0:
      st.error("Fraudulant Job")
    else:
      st.success("Real Job")
   
main()  
