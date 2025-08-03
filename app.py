# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('form.html')

# @app.route('/submit', methods=['POST'])  # ✅ POST allowed
# def submit():
#     name = request.form['name']
#     return f"Hello, {name}!"

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         transcript_file = request.files['transcript']

#         if transcript_file.filename == '':
#             return "No file selected."

#         # Read file content
#         content = transcript_file.read().decode('utf-8')

#         # Dummy logic for now: show transcript content
#         # Later, you can pass this content to your LinkedIn post generator
#         return render_template('result.html', transcript=content)

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# app.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from agent import Agent
# from task import Task
# from my_llm import call_llm
# import json

# app = Flask(__name__)
# CORS(app)  # allow frontend access

# # === Default Agent Config ===
# agent_config = {
#     "reader": {
#         "name": "TranscriptReader",
#         "role": "Analyzer",
#         "goal": "Identify one compelling insight or transformation...",
#         "backstory": "You are skilled at analyzing transcripts..."
#     },
#     "writer": {
#         "name": "PostWriter",
#         "role": "LinkedInWriter",
#         "goal": "Craft a single compelling, real LinkedIn story...",
#         "backstory": "You are an expert at writing viral LinkedIn posts..."
#     },
#     "reviewer": {
#         "name": "Reviewer",
#         "role": "Editor",
#         "goal": "Polish the LinkedIn post...",
#         "backstory": "You are a professional editor for LinkedIn content..."
#     }
# }

# def create_agents(config):
#     return {
#         "reader": Agent(**config["reader"], llm_fn=call_llm),
#         "writer": Agent(**config["writer"], llm_fn=call_llm),
#         "reviewer": Agent(**config["reviewer"], llm_fn=call_llm)
#     }

# @app.route("/agents", methods=["GET"])
# def get_agents():
#     return jsonify(agent_config)

# @app.route("/agents", methods=["POST"])
# def update_agents():
#     global agent_config
#     data = request.json
#     agent_config = data
#     return jsonify({"status": "updated"})

# @app.route("/generate", methods=["POST"])
# def generate():
#     data = request.json
#     transcript = data.get("transcript", "")
#     config = data.get("agents", agent_config)

#     agents = create_agents(config)
#     task1 = Task("read", agents["reader"], "Read the transcript and identify a story.")
#     task2 = Task("write_post", agents["writer"], "Write a compelling LinkedIn post.")
#     task3 = Task("review_post", agents["reviewer"], "Refine the post.")

#     step1 = task1.run(transcript)
#     step2 = task2.run(step1)
#     step3 = task3.run(step2)

#     return jsonify({"post": step3})

# if __name__ == "__main__":
#     app.run(port=5000)


# # app.py
# from flask import Flask, render_template, request
# from api.server import generate_post  # This should be your function to generate the post

# app = Flask(__name__, static_folder="static", template_folder="templates")

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         transcript_file = request.files.get("transcript")
#         if transcript_file:
#             transcript = transcript_file.read().decode("utf-8")
#             post = generate_post(transcript)  # Call your pipeline function
#             return post  # OR: return render_template("result.html", post=post)
#         return "No file uploaded"
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True,port=5050)



# from flask import Flask, render_template, request, jsonify
# import os

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/generate", methods=["POST"])
# def generate():
#     uploaded_file = request.files.get("transcript")
#     if uploaded_file:
#         content = uploaded_file.read().decode("utf-8")
#         # TODO: Replace below line with actual AI logic
#         generated_post = f"Here's a LinkedIn post based on your transcript:\n\n{content[:300]}..."
#         return jsonify({"post": generated_post})
#     else:
#         return jsonify({"post": "No transcript file uploaded."})

# if __name__ == "__main__":
#     app.run(debug=True, port=5050)


# from flask import Flask, request, render_template
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Dummy generate_post for now — replace this with your actual pipeline call
# def generate_post(transcript_text):
#     # Replace with: from main import generate_linkedin_post (or similar)
#     # return generate_linkedin_post(transcript_text)
#     return f"Here's your LinkedIn post:\n\n{transcript_text}\n\n(← replace with AI output)"

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         file = request.files["transcript"]
#         if file:
#             filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(filepath)
#             with open(filepath, "r", encoding="utf-8") as f:
#                 transcript = f.read()

#             post = generate_post(transcript)
#             return post  # this is shown in `resultDiv.innerHTML`
#         return "No file uploaded"
#     return render_template("index.html")




# from flask import Flask, request, render_template, jsonify
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'

# # Make sure the folder exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")

# @app.route("/", methods=["POST"])
# def generate_post():
#     if "transcript" not in request.files:
#         return "❌ No file part in the request.", 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         return "❌ No selected file.", 400

#     text = file.read().decode("utf-8")

#     # Simulate LinkedIn post generation from transcript
#     linkedin_post = f"""Here’s what I learned from today’s session:
# {text}

# #learning #growth #linkedinpost"""

#     return linkedin_post


# @app.route("/", methods=["POST"])
# def generate_post():
#     if "transcript" not in request.files:
#         print("❌ transcript not in request.files")
#         return "❌ No file part in the request.", 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         print("❌ No selected file")
#         return "❌ No selected file.", 400

#     try:
#         text = file.read().decode("utf-8")
#         print("✅ Transcript content:", text)
#     except Exception as e:
#         print("❌ Error reading file:", e)
#         return f"❌ Error reading file: {e}", 500

#     linkedin_post = f"""Here’s what I learned from today’s session:
# {text}

# #learning #growth #linkedinpost"""
#     return linkedin_post


# if __name__ == "__main__":
#     app.run(debug=True, port=5050)

# from flask import Flask, request, render_template, jsonify
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")

# @app.route("/generate", methods=["POST"])
# def generate_post():
#     if "transcript" not in request.files:
#         return jsonify({"error": "No file part in the request."}), 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         return jsonify({"error": "No selected file."}), 400

#     try:
#         text = file.read().decode("utf-8")
#     except Exception as e:
#         return jsonify({"error": f"Error reading file: {e}"}), 500

#     linkedin_post = f"""Here’s what I learned from today’s session:\n{text}\n\n#learning #growth #linkedinpost"""
#     return jsonify({"post": linkedin_post})



# @app.route("/", methods=["POST"])
# def generate_post():
#     if "transcript" not in request.files:
#         print("❌ transcript not in request.files")
#         return "❌ No file part in the request.", 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         print("❌ No selected file")
#         return "❌ No selected file.", 400

#     try:
#         text = file.read().decode("utf-8")
#         print("✅ Transcript content:", text)
#     except Exception as e:
#         print("❌ Error reading file:", e)
#         return f"❌ Error reading file: {e}", 500

#     # You can later replace this logic with AI-generated post
#     linkedin_post = f"""Here’s what I learned from today’s session:

# {text}

# #learning #growth #linkedinpost"""
    
#     return jsonify({"post": linkedin_post})


# if __name__ == "__main__":
#     app.run(debug=True, port=5050)







# from flask import Flask, request, render_template, jsonify
# from main import generate_post
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route("/")
# def index():
#     return render_template("index.html")

# # @app.route("/generate", methods=["POST"])
# # def generate_post():
# #     if "transcript" not in request.files:
# #         return jsonify({"error": "No file uploaded."}), 400

# #     file = request.files["transcript"]
# #     if file.filename == "":
# #         return jsonify({"error": "Empty file name."}), 400

# #     try:
# #         text = file.read().decode("utf-8")
# #     except Exception as e:
# #         return jsonify({"error": f"Error reading file: {e}"}), 500

# #     try:
# #         linkedin_post = handle_transcript(text)  # ✅ this should return a full post
# #         return jsonify({"post": linkedin_post})
# #     except Exception as e:
# #         return jsonify({"error": f"❌ Post generation failed: {e}"}), 500

# @app.route("/generate", methods=["POST"])
# def generate_post_route():
#     if "transcript" not in request.files:
#         return jsonify({"error": "❌ No file uploaded"}), 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         return jsonify({"error": "❌ Empty file name"}), 400

#     try:
#         transcript = file.read().decode("utf-8")
#         post = generate_post(transcript)

#         print("📥 Transcript received:")
#         print(transcript)
#         print("📤 Generated post:")
#         print(post)

#         if post:
#             return jsonify({"post": post})
#         else:
#             return jsonify({"error": "❌ Something went wrong while generating the post."}), 500
#     except Exception as e:
#         print("❌ Exception during file handling:", e)
#         return jsonify({"error": "❌ Server error."}), 500

# if __name__ == "__main__":
#     print("✅ Flask app is starting...")
#     app.run(debug=True, port=5050)

 









# from flask import Flask, request, render_template, jsonify
# import os
# from main import generate_post
# # from crew import run_crew  # your main AI pipeline
# # from werkzeug.utils import secure_filename

# # app = Flask(__name__)
# # @app.route("/")
# # def index():
# #     return render_template("index.html")

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate_post():
#     if 'transcript' not in request.files:
#         return "No transcript file provided", 400

#     file = request.files['transcript']
#     if file.filename == '':
#         return "Empty filename", 400

#     filename = secure_filename(file.filename)
#     filepath = os.path.join(UPLOAD_FOLDER, filename)
#     file.save(filepath)

#     with open(filepath, 'r', encoding='utf-8') as f:
#         transcript = f.read()

#     final_post = run_crew(transcript)
#     return render_template('index.html', post=final_post)

# # ✅ Code viewer/editor route
# @app.route("/code/<filename>", methods=["GET", "POST"])
# def code_editor(filename):
#     if not filename.endswith(".py"):
#         return jsonify({"error": "Only .py files allowed"}), 400

#     filepath = os.path.join(os.getcwd(), filename)

#     if request.method == "GET":
#         try:
#             with open(filepath, "r", encoding="utf-8") as f:
#                 code = f.read()
#             return jsonify({"filename": filename, "code": code})
#         except FileNotFoundError:
#             return jsonify({"error": "File not found"}), 404

#     elif request.method == "POST":
#         new_code = request.json.get("code", "")
#         try:
#             with open(filepath, "w", encoding="utf-8") as f:
#                 f.write(new_code)
#             return jsonify({"message": "✅ File saved successfully"})
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

#     app = Flask(__name__)

# app = Flask(__name__)

# from flask import Flask, request, render_template
# import os
# from crew import Crew
# from agent import transcript_reader_agent, post_writer_agent, reviewer_agent
# from task import Task
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # This serves the frontend
# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")

# # This handles the uploaded transcript
# @app.route("/generate", methods=["POST"])
# def generate():
#     transcript_file = request.files["transcript"]
#     filename = secure_filename(transcript_file.filename)
#     filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#     transcript_file.save(filepath)

#     with open(filepath, "r", encoding="utf-8") as f:
#         transcript = f.read()

#     # Run your AI pipeline
#     tasks = [
#         Task("Read Transcript", transcript_reader_agent, "Extract key story from the transcript."),
#         Task("Write LinkedIn Post", post_writer_agent, "Write a LinkedIn post based on the story."),
#         Task("Polish Post", reviewer_agent, "Polish the LinkedIn post to make it engaging and professional.")
#     ]
#     crew = Crew(agents=[transcript_reader_agent, post_writer_agent, reviewer_agent], tasks=tasks, verbose=True)
#     final_post = crew.run(transcript)

#     return render_template("index.html", result=final_post)

# if __name__ == "__main__":
#     app.run(debug=True)












# from flask import Flask, request, render_template, jsonify
# from main import generate_post
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route("/")
# def index():
#     return render_template("index.html")  # this will load your HTML file

# @app.route("/generate", methods=["POST"])
# def generate_post_route():
#     if "transcript" not in request.files:
#         return jsonify({"error": "❌ No file uploaded"}), 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         return jsonify({"error": "❌ Empty file name"}), 400

#     try:
#         transcript = file.read().decode("utf-8")
#         post = generate_post(transcript)
#         return jsonify({"post": post})
#     except Exception as e:
#         return jsonify({"error": "❌ Server error."}), 500

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)



# from flask import Flask, request, render_template, jsonify
# from main import generate_post
# from crew import run_crew

# import os

# app = Flask(__name__, template_folder="templates")
# app.config['UPLOAD_FOLDER'] = 'uploads'
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")

# @app.route("/generate", methods=["POST"])
# # def generate():
# #     if "transcript" not in request.files:
# #         return jsonify({"error": "No file uploaded"}), 400

# #     file = request.files["transcript"]
# #     if file.filename == "":
# #         return jsonify({"error": "Empty file name"}), 400

# #     try:
# #         transcript = file.read().decode("utf-8")
# #         post = generate_post(transcript)
# #         return jsonify({"post": post})
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500


# @app.route("/generate", methods=["POST"])
# def generate():
#     if "transcript" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         return jsonify({"error": "Empty file name"}), 400

#     try:
#         transcript = file.read().decode("utf-8")
#         print("📄 Transcript received:\n", transcript[:200])  # Optional: preview
#         post = generate_post(transcript)
#         return jsonify({"post": post})
#     except Exception as e:
#         print("❌ Error while generating post:", e)
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)



# from flask import Flask, render_template, request, jsonify
# from crew import run_crew  # make sure crew.py contains run_crew()

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")  # templates/index.html


# @app.route("/generate", methods=["POST"])
# def generate():
#     if "transcript" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         return jsonify({"error": "Empty file name"}), 400

#     try:
#         transcript = file.read().decode("utf-8")
#         print("📄 Transcript received:\n", transcript[:300])

#         post = generate_post(transcript)
#         if post is None:
#             return jsonify({"error": "Failed to generate post"}), 500

#         return jsonify({"post": post})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# def generate_post(transcript):
#     try:
#         print("🚀 Running full crew pipeline...")
#         print("📥 Received transcript:", transcript[:200])
#         final_output = run_crew(transcript)  # Make sure this is defined in crew.py
#         print("✅ Final polished post:", final_output)
#         return final_output
#     except Exception as e:
#         print("❌ Error in generate_post:", e)
#         return None


# if __name__ == "__main__":
#     app.run(debug=True)



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

