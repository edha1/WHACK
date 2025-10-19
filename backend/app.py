# Importing Flask and "predict"
from flask import Flask, request, jsonify
from flask_cors import CORS
from run import predict
from translate import translate_to_english

app = Flask(__name__)
# TODO: Restrict origins in prod
CORS(app)  

@app.route('/check', methods=['POST'])
def check_article():
    data = request.get_json()

    # Check data is intact (header and content exist)
    if not data or 'header' not in data or 'content' not in data:
        return jsonify({"error": "Missing 'header' or 'content'"}), 400

    # Handle Google API Cloud Translation
    if 'language' in data and not data['language'].startswith('en'):
        try:
            data = translate_to_english(data)
        except Exception as err:
            app.logger.error(f"Translation failed: {err}")
            return jsonify({"error": "Translation error"}), 500
        
    # Return confidence level, otherwise 500
    try:
        return jsonify({"accuracy": predict(data['header'], data['content'])}), 200
    except Exception as err:
        app.logger.error(f"Prediction failed: {err}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # TODO: Turn off debug in prod