# # server.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from main import generate_post

# app = Flask(__name__)
# CORS(app)  # allow your webpage to call the API

# @app.route('/api/run', methods=['POST'])
# def run_api():
#     transcript = request.json.get('transcript', '')
#     result = generate_post(transcript)
#     return jsonify({'post': result})

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from flask import Flask, render_template, request
from main import generate_post

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["transcript"]
        content = file.read().decode("utf-8")
        post = generate_post(content)
        return render_template("result.html", linkedin_post=post)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

