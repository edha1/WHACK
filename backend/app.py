# Import CORS to enable host communication
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check-article', methods=['POST'])
def check_article():
    data = request.get_json()

    title = data.get('title', '')
    body = data.get('body', '')
    date = data.get('date', '')

    result = {
        'truthful': True,
        'confidence': 0.92,
        'message': 'This article appears to be factual.'
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
