from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/predict_score', methods=['POST'])
def predict_score():
    study_hours = float(request.form['study_hours'])

    response = jsonify({
        'predicted_score': util.estimated_score(study_hours)
    })

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()
