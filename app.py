import streamlit as st
import pickle
import time

model = pickle.load(open('models/twitter_sentiment.pkl', 'rb'))

st.set_page_config(page_title="Twitter Sentiment Analysis")
st.title('Twitter Sentiment Analysis')

tweet = st.text_input('Enter your tweet')

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')

    st.write('Sentiment: ', prediction[0])