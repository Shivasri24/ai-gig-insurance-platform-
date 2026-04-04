from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/premium')
def premium():
    return jsonify({
        "risk": "medium",
        "weekly_premium": 45
    })

@app.route('/trigger')
def trigger():
    return jsonify({
        "trigger": True,
        "payout": 300
    })

if __name__ == '__main__':
    app.run(debug=True)