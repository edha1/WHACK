from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # for local testing, need to change for prod 

@app.route('/check-article', methods=['POST'])
def check_article():
    data = request.get_json()

    print("Received POST data:", data)  # log to terminal

    # TODO: put data into model and return the output 
    # Just send back what was received for debugging
    return jsonify({
        "received": data,
        "status": "success",
        "message": "Data received successfully!"
    })

if __name__ == '__main__':
    app.run(port=5000)
