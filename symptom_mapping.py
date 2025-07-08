SYMPTOM_TO_DEPARTMENT = {
    "chest pain": "Cardiology",
    "rash": "Dermatology",
    "shortness of breath": "Pulmonology",
    "joint pain": "Orthopedics",
    "headache": "Neurology",
    "fever": "General Medicine",
    "abdominal pain": "Gastroenterology",
    "vision problems": "Ophthalmology",
    "skin irritation": "Dermatology",
    "numbness": "Neurology",
    "palpitations": "Cardiology",
    "back pain": "Orthopedics"
}

def map_symptom_to_department(symptom_text):
    for keyword in SYMPTOM_TO_DEPARTMENT:
        if keyword in symptom_text.lower():
            return SYMPTOM_TO_DEPARTMENT[keyword]
    return "General Medicine"
