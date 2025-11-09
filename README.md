# 🩺 Healthcare Text Classification Chatbot  

> **A simple NLP-based healthcare chatbot** that predicts possible medical conditions from user-entered text using a trained TF-IDF and machine learning model.

---

## 🚀 Overview  

This project demonstrates the use of **Natural Language Processing (NLP)** and **text classification** for healthcare-related predictions.  
It allows users to enter symptom descriptions or health notes and returns the most likely condition using a trained ML model.  

---

## ✨ Features  

💬 Takes natural language input (symptom or health description)  
🧠 Uses TF-IDF vectorization and an ML classifier for prediction  
⚙️ Lightweight and easy to deploy using **Streamlit**  
🌐 Simple, user-friendly interface for quick analysis  

---

## 🧩 Tech Stack  

| Component | Technology |
|------------|-------------|
| 🐍 Language | Python |
| 🧠 NLP | TF-IDF Vectorizer |
| 🔍 ML Model | scikit-learn |
| 🌐 Web Interface | Streamlit |
| 🗂️ Serialization | joblib |

---

## 🧠 How It Works  

1️⃣ User enters text (e.g., symptoms or medical note).  
2️⃣ Text is vectorized using a **TF-IDF model**.  
3️⃣ A **trained classifier** predicts the most probable condition.  
4️⃣ The predicted condition is displayed in the Streamlit interface.  

---

## 🖥️ Demo  

🗣️ *“I have a headache and feeling dizzy.”*  
➡️ **Predicted Condition:** Migraine 🌿  

---

## 🛠️ Setup Instructions  

```bash
# Clone the repository
git clone https://github.com/taaniaghosh/Explainable-Healthcare-Chatbot.git

# Navigate to the project folder
cd Explainable-Healthcare-Chatbot

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
