from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/comprehensive-triage', methods=['POST'])
def comprehensive_triage():
    try:
        # Retrieve the request data
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        user_profile = data.get('userProfile', {})

        # Placeholder triage logic for demonstration purposes
        triage_result = ""
        basic_advice = ""
        detailed_instructions = ""
        nearest_facilities = ["General Hospital", "Urgent Care Clinic"]
        
        # Assess the severity based on symptoms
        critical_symptoms = ["can't see", "can't breathe", "can't speak", "sudden physiological dysfunction"]
        severe_symptoms = ["slurred speech", "can't move hand", "heavy bleeding", "psychotic behavior"]

        if any(symptom in symptoms for symptom in critical_symptoms):
            triage_result = "0 - Immediate 999"
            basic_advice = "Dial emergency services immediately."
            detailed_instructions = "It appears you are experiencing critical symptoms requiring immediate attention."
        elif any(symptom in symptoms for symptom in severe_symptoms):
            triage_result = "1,1,1,0 - A&E"
            basic_advice = "Proceed to the nearest Accident & Emergency department."
            detailed_instructions = "You are experiencing symptoms that may need specialized care. Please visit an A&E department."
        elif len(symptoms) > 1:
            triage_result = "Urgent Care Required"
            basic_advice = "Consider visiting an urgent care clinic."
            detailed_instructions = "You have multiple symptoms that could indicate a condition needing prompt attention."
        else:
            triage_result = "Self-Care or GP"
            basic_advice = "Monitor symptoms and contact your GP if needed."
            detailed_instructions = "Your symptoms do not indicate an emergency, but please keep monitoring and seek GP advice if they persist or worsen."

        response = {
            "triage_result": triage_result,
            "basic_advice": basic_advice,
            "detailed_instructions": detailed_instructions,
            "nearest_facilities": nearest_facilities
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)