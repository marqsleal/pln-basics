import streamlit as st
import nltk as nl

st.write('# Analise de Satisfação do Cliente')

usr_input = st.text_input('## Como você avalia o nosso atendimento? (EN)')

nl.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

score = sia.polarity_scores(usr_input)

if score == 0:
    st.write('')
elif score['neg'] != 0:
    st.write('Analise Negativa')
elif score['pos'] != 0:
    st.write('Analise Positiva')