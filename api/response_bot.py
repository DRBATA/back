from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/response', methods=['POST'])
def get_response():
    data = request.json
    message = data.get('message', '').lower()

    if 'not ok' not in message and 'problem' not in message and 'issue' not in message:
        return jsonify({
            'status': 'OK',
            'recommendation': 'Everything appears fine. No immediate action is needed.'
        })

    # Determine domain
    if 'health' in message:
        domain = 'health'
    elif 'environment' in message:
        domain = 'environment'
    else:
        domain = 'general'

    # Determine urgency
    urgency = 'reactive' if 'urgent' in message or 'immediate' in message else 'proactive'

    # Construct response
    if domain == 'health':
        recommendation = 'Immediate medical attention is recommended.' if urgency == 'reactive' else 'You should schedule a regular check-up or consult with your healthcare provider.'
    elif domain == 'environment':
        recommendation = 'Take immediate action to mitigate the environmental risk.' if urgency == 'reactive' else 'Consider addressing environmental concerns when feasible.'
    else:
        recommendation = 'Take quick steps to address the problem.' if urgency == 'reactive' else 'Plan ahead to mitigate any foreseeable issues.'

    return jsonify({
        'status': 'Not OK',
        'recommendation': recommendation
    })

if __name__ == '__main__':
    app.run(debug=True)
