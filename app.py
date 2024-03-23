import json
from flask import Flask, render_template, request, jsonify
from elGamalSign import sign as elgamal_sign
from elGamalVerify import verify as elgamal_verify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign', methods=['POST'])
def sign_message():
    text = request.form['text']
    prime, g, public_key, r, s = elgamal_sign(text)
    # Return the signature and public key information to the user
    signature = {'r': r, 's': s}
    public_key_info = {'prime': prime, 'g': g, 'public_key': public_key}
    return jsonify({'signature': signature, 'public_key': public_key_info})

@app.route('/verify', methods=['POST'])
def verify_message():
    text = request.form['text']
    signature_str = request.form['signature']
    public_key_str = request.form['public_key']
    
    # Parse the JSON strings into Python dictionaries
    signature = json.loads(signature_str)
    public_key = json.loads(public_key_str)

    r = int(signature['r'])
    s = int(signature['s'])
    prime = int(public_key['prime'])
    g = int(public_key['g'])
    y = int(public_key['public_key'])

    is_authentic, left_side, right_side = elgamal_verify(text, (r, s), (prime, g, y))
    return jsonify({'authentic': is_authentic, 'left_side': left_side, 'right_side': right_side})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
