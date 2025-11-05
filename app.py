import streamlit as st
import joblib

tfidf = joblib.load("tfidfvectorizer.pk1")
clf = joblib.load("passmodel.pk1")

st.set_page_config(page_title="Explainable Healthcare chatbot", layout="centered")

st.markdown("<h1 style='font-family:Playfair Display; text-align:center; color:#d6336c;'>Explainable Healthcare Chatbot</h1>", unsafe_allow_html=True)

text = st.text_area("🩺 Paste the health note or review here:", height=150)

if st.button("Predict"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        x = tfidf.transform([text])
        pred = clf.predict(x)[0]
        st.success(f"🌿 Predicted Condition: {pred}")
