from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['post'])
def submit():
    # Try getting JSON first, then form data
    data = request.get_json(silent=True)
    if not data:
        data = request.form

    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400
    
    return jsonify({
        "message": f"Backend received: Name={name}, Email={email}", 
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
