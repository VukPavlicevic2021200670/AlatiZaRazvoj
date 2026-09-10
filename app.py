from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # Očitavamo promenljivu iz okruženja (kasnije ćemo je podesiti u Kubernetesu)
    message = os.getenv('MESSAGE', 'Zdravo svete, ovo je test12!')
    return jsonify({
        "message": message,
        "version": "1.4",
        "timestamp": datetime.datetime.now().isoformat(),
        "hostname": os.getenv('HOSTNAME', 'nepoznat')
    })

@app.route('/health')
def health():
    # Ovo koristimo da proverimo da li je aplikacija živa
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
