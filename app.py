from flask import Flask, request, jsonify
from symptom_mapping import map_symptom_to_department
from openai_api import query_openai

app = Flask(__name__)

@app.route('/')
def home():
    return "Medical Chatbot Backend is Running"

@app.route('/analyze', methods=['POST'])
def analyze_symptoms():
    data = request.get_json()
    user_input = data.get("symptoms", "")

    if not user_input:
        return jsonify({"error": "No symptoms provided"}), 400

    department = query_openai(user_input)

    if department.lower() in ["i'm not sure", "unknown", "general", "medicine", ""]:
        department = map_symptom_to_department(user_input)

    return jsonify({
        "symptoms": user_input,
        "recommended_department": department
    })

if __name__ == "__main__":
    app.run(debug=True)
