def build_prompt(symptom_input):
    return f"""
A user has described the following symptoms:

"{symptom_input}"

Your task is to recommend the most appropriate medical department that the user should consult. Respond with only the department name (e.g., Cardiology, Dermatology, Neurology, etc.) and nothing else.
"""