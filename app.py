from flask import Flask, request, jsonify, render_template
from crew import run_crew  # Make sure run_crew is defined in crew.py
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'transcript' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['transcript']
    if file.filename == '':
        return jsonify({'error': 'Empty file name'}), 400

    try:
        transcript = file.read().decode('utf-8')
        post = run_crew(transcript)
        return jsonify({'post': post})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

