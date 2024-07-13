from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    if re.search(r'[!@#\$%\^&\*]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*).")

    return strength, feedback

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    strength, feedback = check_password_strength(password)
    return jsonify({'strength': strength, 'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True)
