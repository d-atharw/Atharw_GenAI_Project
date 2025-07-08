# Medical Chatbot for Symptom Analysis

This project is an intelligent medical chatbot that analyzes user-entered symptoms and recommends the appropriate medical department to consult. It combines a simple frontend interface with a Python Flask backend, using OpenAI's GPT-3.5 language model for natural language reasoning, with rule-based fallback logic for reliability.


## Features

- AI-based interpretation of natural language symptom descriptions
- Maps symptoms to departments like Cardiology, Dermatology, Neurology, etc.
- Simple web interface built with HTML, CSS, and JavaScript
- Flask backend handles API requests and integrates with OpenAI
- Secure storage of API keys using `.env`
- Rule-based fallback system ensures robustness in case of LLM uncertainty
