# # # from agent import Agent 
# # # from task import Task
# # # from crew import Crew
# # # from my_llm import call_llm

# # # # === Load transcript ===
# # # with open("transcript.txt", "r", encoding="utf-8") as f:
# # #     transcript = f.read()

# # # # === Define Agents ===

# # # reader = Agent(
# # #     name="TranscriptReader",
# # #     role="Analyzer",
# # #     goal="Identify specific moments, insights, and characters that can be turned into compelling LinkedIn stories.",
# # #     backstory=(
# # #         "You are skilled at analyzing interview-style transcripts to spot core messages and key players. "
# # #         "Focus on key unique insights rather than general ones. The unique insights could be industry insights, "
# # #         "case studies, any data points, any expectation of business, any expectation of recruiter, role expectation, etc. "
# # #         "It may happen that one transcript may have multiple ideas, so it may create multiple stories. "
# # #         "Focus on specific insights which can be made into interesting stories."
# # #     ),
# # #     llm_fn=call_llm
# # # )

# # # extractor = Agent(
# # #     name="StoryExtractor",
# # #     role="NarrativeBuilder",
# # #     goal="Turn the identified key points into a compelling story.",
# # #     backstory=(
# # #         "You specialize in converting real-life moments into emotionally engaging stories.\n"
# # #         "Structure the story as follows:\n"
# # #         "1. Hook: Add a powerful hook to draw in the reader.\n"
# # #         "2. Situation: Provide context, the complexity of the situation, and its importance (60–70 words).\n"
# # #         "3. Task: What was your role or the task given (20–30 words).\n"
# # #         "4. Action: Describe your actions showcasing your knowledge, skills, competence, attitude, etc. (70–80 words).\n"
# # #         "5. Result: Outcome of your actions, what you accomplished or learned, preferably with metrics (40–50 words).\n"
# # #         "6. Reflection: What did you learn from the experience? (40–50 words).\n"
# # #         "7. Call to Action: Close with a message to engage readers.\n"
# # #         "Also, include 1–2 intriguing or relatable characters. Ensure the story sounds natural and not AI-generated."
# # #     ),
# # #     llm_fn=call_llm
# # # )

# # # writer = Agent(
# # #     name="PostWriter",
# # #     role="LinkedInWriter",
# # #     goal="Craft LinkedIn posts using real stories that connect, teach, and inspire.",
# # #     backstory=(
# # #         "You are an expert at writing viral LinkedIn posts. You follow a structured format as given by the extractor. "
# # #         "You write in a conversational yet professional tone, using short paragraphs and line breaks to enhance readability. "
# # #         "Also, take the input from the reviewer and correct the post. Iterate it a couple of times to refine it."
# # #     ),
# # #     llm_fn=call_llm
# # # )

# # # reviewer = Agent(
# # #     name="Reviewer",
# # #     role="Editor and Content Optimizer",
# # #     goal="Improve the LinkedIn post to make it clearer, more engaging, and more likely to go viral. Return the improved post.",
# # #     backstory=(
# # #         "You are a LinkedIn post reviewer and editor. Your job is not to critique, but to directly improve the given post.\n"
# # #         "Your review should apply the following checklist:\n"
# # #         "1. Does it start with an eye-catching Hook?\n"
# # #         "2. Is the Context clear and relatable?\n"
# # #         "3. Is there Insight or Learning that adds value?\n"
# # #         "4. Is the Conclusion strong?\n"
# # #         "5. Does it end with a Call to Action?\n"
# # #         "6. Does it include 3–7 relevant hashtags?\n"
# # #         "If anything is missing or weak, revise and return a better version of the post.\n"
# # #         "Use headings like **Hook**, **Context**, etc., and make sure the final result reads like a finished LinkedIn post."
# # #     ),
# # #     llm_fn=call_llm
# # # )


# # # hashtagger = Agent(
# # #     name="HashtagAgent",
# # #     role="HashtagGenerator",
# # #     goal="Generate 3–5 relevant LinkedIn hashtags for maximum engagement.",
# # #     backstory=(
# # #         "You optimize hashtag selection for LinkedIn: mix broad (million+) and niche (<100 K), "
# # #         "limit to 3–5, place them at the end. Use trending and relevant tags."
# # #     ),
# # #     llm_fn=call_llm
# # # )

# # # # === Define Tasks ===

# # # task1 = Task("read", reader, "Read the transcript and identify the key narrative and characters.")
# # # task2 = Task("extract", extractor, "Turn the key narrative into a compelling story.")
# # # task3 = Task("write_post", writer, 
# # #     """Write a compelling LinkedIn post from the story using the following structure:

# # # **Hook** (1–2 lines): Start with a bold, attention-grabbing line that makes people stop scrolling.
# # # **Context** (3–4 lines): Explain the situation, challenge, or moment.
# # # **Insight** (4–7 lines): Share what was learned, realized, or uncovered.
# # # **Conclusion** (2–3 lines): Wrap it up with a takeaway or forward-looking message.
# # # **Call to Action** (1–2 lines): Invite readers to comment, share, or reflect.
# # # **Hashtags** (3–7): Add 3–7 relevant hashtags on a new line at the end.

# # # Keep the tone conversational and professional. Use short paragraphs and line breaks. Make it sound human — not robotic.
# # # """
# # # )


# # # task4 = Task("review_post", reviewer, "Review and improve the LinkedIn post.")

# # # # === Run the crew (manual chaining) ===

# # # print("\n🔍 Starting AI Agent Pipeline...\n")

# # # step1_output = task1.agent.run(transcript)
# # # step2_output = task2.agent.run(step1_output)
# # # step3_output = task3.agent.run(step2_output)
# # # step4_output = task4.agent.run(step3_output)


# # # # === Final Output ===

# # # print("\n=== FINAL LINKEDIN POST ===\n")
# # # print(step4_output)

# # # with open("linkedin_post.txt", "w", encoding="utf-8") as f:
# # #     f.write(step4_output)

# # # print("\n✅ LinkedIn post saved to 'linkedin_post.txt'")


# # from agent import Agent 
# # from task import Task
# # from crew import Crew
# # from my_llm import call_llm

# # # === Load transcript ===
# # with open("transcript.txt", "r", encoding="utf-8") as f:
# #     transcript = f.read()

# # # === Define Agents ===

# # reader = Agent(
# #     name="TranscriptReader",
# #     role="Analyzer",
# #     goal="Identify specific moments, insights, and characters that can be turned into compelling LinkedIn stories.",
# #     backstory=(
# #         "You are skilled at analyzing interview-style transcripts to spot core messages and key players. "
# #         "Focus on key unique insights rather than general ones. The unique insights could be industry insights, "
# #         "case studies, any data points, any expectation of business, any expectation of recruiter, role expectation, etc. "
# #         "It may happen that one transcript may have multiple ideas, so it may create multiple stories. "
# #         "Focus on specific insights which can be made into interesting stories."
# #     ),
# #     llm_fn=call_llm
# # )

# # extractor = Agent(
# #     name="StoryExtractor",
# #     role="NarrativeBuilder",
# #     goal="Turn the identified key points into a compelling story.",
# #     backstory=(
# #         "You specialize in converting real-life moments into emotionally engaging stories.\n"
# #         "Structure the story as follows:\n"
# #         "1. Hook: Add a powerful hook to draw in the reader.\n"
# #         "2. Situation: Provide context, the complexity of the situation, and its importance (60–70 words).\n"
# #         "3. Task: What was your role or the task given (20–30 words).\n"
# #         "4. Action: Describe your actions showcasing your knowledge, skills, competence, attitude, etc. (70–80 words).\n"
# #         "5. Result: Outcome of your actions, what you accomplished or learned, preferably with metrics (40–50 words).\n"
# #         "6. Reflection: What did you learn from the experience? (40–50 words).\n"
# #         "7. Call to Action: Close with a message to engage readers.\n"
# #         "Also, include 1–2 intriguing or relatable characters. Ensure the story sounds natural and not AI-generated."
# #     ),
# #     llm_fn=call_llm
# # )

# # writer = Agent(
# #     name="PostWriter",
# #     role="LinkedInWriter",
# #     goal="Craft LinkedIn posts using real stories that connect, teach, and inspire.",
# #     backstory=(
# #         "You are an expert at writing viral LinkedIn posts. You follow a structured format as given by the extractor. "
# #         "You write in a conversational yet professional tone, using short paragraphs and line breaks to enhance readability. "
# #         "Also, take the input from the reviewer and correct the post. Iterate it a couple of times to refine it."
# #     ),
# #     llm_fn=call_llm
# # )

# # reviewer = Agent(
# #     name="Reviewer",
# #     role="Editor and Content Optimizer",
# #     goal="Improve the LinkedIn post to make it clearer, more engaging, and more likely to go viral. Return the improved post.",
# #     backstory=(
# #         "You are a LinkedIn post reviewer and editor. Your job is not to critique, but to directly improve the given post.\n"
# #         "Your review should apply the following checklist:\n"
# #         "1. Does it start with an eye-catching Hook?\n"
# #         "2. Is the Context clear and relatable?\n"
# #         "3. Is there Insight or Learning that adds value?\n"
# #         "4. Is the Conclusion strong?\n"
# #         "5. Does it end with a Call to Action?\n"
# #         "6. Does it include 3–7 relevant hashtags?\n"
# #         "If anything is missing or weak, revise and return a better version of the post.\n"
# #         "Use headings like **Hook**, **Context**, etc., and make sure the final result reads like a finished LinkedIn post."
# #     ),
# #     llm_fn=call_llm
# # )

# # hashtagger = Agent(
# #     name="HashtagAgent",
# #     role="HashtagGenerator",
# #     goal="Generate 3–5 relevant LinkedIn hashtags for maximum engagement.",
# #     backstory=(
# #         "You optimize hashtag selection for LinkedIn: mix broad (million+) and niche (<100 K), "
# #         "limit to 3–5, place them at the end. Use trending and relevant tags."
# #     ),
# #     llm_fn=call_llm
# # )

# # # === Define Tasks ===

# # task1 = Task("read", reader, "Read the transcript and identify the key narrative and characters.")
# # task2 = Task("extract", extractor, "Turn the key narrative into a compelling story.")
# # # task3 = Task("write_post", writer, 
# # #     """Write a compelling LinkedIn post from the story using the following structure:

# # # **Hook** (1–2 lines): Start with a bold, attention-grabbing line that makes people stop scrolling.
# # # **Context** (3–4 lines): Explain the situation, challenge, or moment.
# # # **Insight** (4–7 lines): Share what was learned, realized, or uncovered.
# # # **Conclusion** (2–3 lines): Wrap it up with a takeaway or forward-looking message.
# # # **Call to Action** (1–2 lines): Invite readers to comment, share, or reflect.
# # # **Hashtags** (3–7): Add 3–7 relevant hashtags on a new line at the end.

# # # Keep the tone conversational and professional. Use short paragraphs and line breaks. Make it sound human — not robotic.
# # # """
# # # )


# # task3 = Task("write_post", writer, 
# #     """Write a high-quality LinkedIn post based on the story. Internally follow this structure but DO NOT mention section labels like Hook, Context, or Hashtags in the final output:

# # - Start with a bold, scroll-stopping opening that hooks the reader emotionally or intellectually.
# # - Share the background or challenge in a relatable and concise way.
# # - Include a meaningful insight or learning from the experience—make it human and specific.
# # - End with a strong, memorable conclusion or forward-looking message.
# # - Encourage engagement with a subtle call to action.
# # - End with 3–7 relevant LinkedIn hashtags (on a separate line, but no label).

# # Tone: conversational yet professional.  
# # Style: short paragraphs, line breaks, emotionally engaging, and authentic.  
# # Goal: Make it feel like a natural, inspiring story from a real human—not AI-generated.
# # """
# # )

# # task4 = Task("review_post", reviewer, "Review and improve the LinkedIn post.")

# # # === Run the crew (manual chaining) ===

# # print("\n🔍 Starting AI Agent Pipeline...\n")

# # step1_output = task1.agent.run(transcript)
# # step2_output = task2.agent.run(step1_output)
# # step3_output = task3.agent.run(step2_output)
# # step4_output = task4.agent.run(step3_output)

# # # === Final Output ===

# # print("\n=== FINAL LINKEDIN POST ===\n")
# # print(step4_output)

# # with open("linkedin_post.txt", "w", encoding="utf-8") as f:
# #     f.write(step4_output)

# # print("\n✅ LinkedIn post saved to 'linkedin_post.txt'")



# from agent import Agent 
# from task import Task
# from crew import Crew
# from my_llm import call_llm

# # === Load transcript ===
# with open("transcript.txt", "r", encoding="utf-8") as f:
#     transcript = f.read()

# # === Define Agents ===

# reader = Agent(
#     name="TranscriptReader",
#     role="Analyzer",
#     goal="Identify specific moments, insights, and characters that can be turned into compelling LinkedIn stories.",
#     backstory=(
#         "You are skilled at analyzing interview-style transcripts to spot core messages and key players. "
#         "Focus on key unique insights rather than general ones. The unique insights could be industry insights, "
#         "case studies, any data points, any expectation of business, any expectation of recruiter, role expectation, etc. "
#         "It may happen that one transcript may have multiple ideas, so it may create multiple stories. "
#         "Focus on specific insights which can be made into interesting stories."
#     ),
#     llm_fn=call_llm
# )

# writer = Agent(
#     name="PostWriter",
#     role="LinkedInWriter",
#     goal="Craft LinkedIn posts using real stories that connect, teach, and inspire.",
#     backstory=(
#         "You are an expert at writing viral LinkedIn posts. You follow a structured format as given below:\n\n"
#         "Structure the story as follows:\n"
#         "1. Hook: Add a powerful hook to draw in the reader.\n"
#         "2. Situation: Provide context, the complexity of the situation, and its importance (60–70 words).\n"
#         "3. Task: What was your role or the task given (20–30 words).\n"
#         "4. Action: Describe your actions showcasing your knowledge, skills, competence, attitude, etc. (70–80 words).\n"
#         "5. Result: Outcome of your actions, what you accomplished or learned, preferably with metrics (40–50 words).\n"
#         "6. Reflection: What did you learn from the experience? (40–50 words).\n"
#         "7. Call to Action: Close with a message to engage readers.\n"
#         "Also, include 1–2 intriguing or relatable characters. Ensure the story sounds natural and not AI-generated.\n\n"
#         "You write in a conversational yet professional tone, using short paragraphs and line breaks to enhance readability. "
#         "Also, take the input from the reviewer and correct the post. Iterate it a couple of times to refine it."
#     ),
#     llm_fn=call_llm
# )

# reviewer = Agent(
#     name="Reviewer",
#     role="Editor and Content Optimizer",
#     goal="Improve the LinkedIn post to make it clearer, more engaging, and more likely to go viral. Return the improved post.",
#     backstory=(
#         "You are a LinkedIn post reviewer and editor. Your job is not to critique, but to directly improve the given post.\n"
#         "Your review should apply the following checklist:\n"
#         "1. Does it start with an eye-catching Hook?\n"
#         "2. Is the Context clear and relatable?\n"
#         "3. Is there Insight or Learning that adds value?\n"
#         "4. Is the Conclusion strong?\n"
#         "5. Does it end with a Call to Action?\n"
#         "6. Does it include 3–7 relevant hashtags?\n"
#         "If anything is missing or weak, revise and return a better version of the post.\n"
#         "Use headings like **Hook**, **Context**, etc., and make sure the final result reads like a finished LinkedIn post."
#     ),
#     llm_fn=call_llm
# )

# hashtagger = Agent(
#     name="HashtagAgent",
#     role="HashtagGenerator",
#     goal="Generate 3–5 relevant LinkedIn hashtags for maximum engagement.",
#     backstory=(
#         "You optimize hashtag selection for LinkedIn: mix broad (million+) and niche (<100 K), "
#         "limit to 3–5, place them at the end. Use trending and relevant tags."
#     ),
#     llm_fn=call_llm
# )

# # === Define Tasks ===

# task1 = Task("read", reader, "Read the transcript and identify the key narrative and characters.")

# task2 = Task("write_post", writer, 
#     """Write a high-quality LinkedIn post based on the story. Internally follow this structure but DO NOT mention section labels like Hook, Context, or Hashtags in the final output:

# - Start with a bold, scroll-stopping opening that hooks the reader emotionally or intellectually.
# - Share the background or challenge in a relatable and concise way.
# - Include a meaningful insight or learning from the experience—make it human and specific.
# - End with a strong, memorable conclusion or forward-looking message.
# - Encourage engagement with a subtle call to action.
# - End with 3–7 relevant LinkedIn hashtags (on a separate line, but no label).

# Tone: conversational yet professional.  
# Style: short paragraphs, line breaks, emotionally engaging, and authentic.  
# Goal: Make it feel like a natural, inspiring story from a real human—not AI-generated.
# """
# )

# task3 = Task("review_post", reviewer, "Review and improve the LinkedIn post.")

# # === Run the crew (manual chaining) ===

# print("\n🔍 Starting AI Agent Pipeline...\n")

# step1_output = task1.agent.run(transcript)
# step2_output = task2.agent.run(step1_output)
# step3_output = task3.agent.run(step2_output)

# # === Final Output ===

# print("\n=== FINAL LINKEDIN POST ===\n")
# print(step3_output)

# with open("linkedin_post.txt", "w", encoding="utf-8") as f:
#     f.write(step3_output)

# print("\n✅ LinkedIn post saved to 'linkedin_post.txt'")



# from agent import Agent 
# from task import Task
# from crew import Crew
# from my_llm import call_llm

# # === Load transcript ===
# with open("transcript.txt", "r", encoding="utf-8") as f:
#     transcript = f.read()

# # === Define Agents ===

# reader = Agent(
#     name="TranscriptReader",
#     role="Analyzer",
#     goal="Identify one compelling insight, moment, or transformation that can be turned into a powerful LinkedIn story.",
#     backstory=(
#         "You are skilled at analyzing transcripts to spot a *single* strong narrative with emotional or intellectual depth. "
#         "Even if the transcript contains multiple topics, your job is to find the **most impactful one** — a story worth telling. "
#         "Focus on clear outcomes, transformation, learnings, or character arcs that readers can relate to. "
#         "Do not list or extract all topics — pick the strongest insight that can become a powerful story."
#     ),
#     llm_fn=call_llm
# )

# writer = Agent(
#     name="PostWriter",
#     role="LinkedInWriter",
#     goal="Craft a single compelling, real LinkedIn story that feels human, inspiring, and natural.",
#     backstory=(
#         "You are an expert at writing viral LinkedIn posts.\n"
#         "You specialize in crafting stories that feel authentic and are written like real humans — not AI.\n\n"
#         "Here's your story-building approach:\n"
#         "1. Start with an emotionally engaging or curiosity-piquing opening line.\n"
#         "2. Share a clear, detailed narrative with emotional ups and downs — third-person preferred.\n"
#         "3. Highlight a challenge, the actions taken, and what was learned or changed.\n"
#         "4. End with a reflective thought and a question to prompt comments.\n\n"
#         "Important:\n"
#         "- Only one story per post — even if the transcript has many topics.\n"
#         "- Do NOT use section headings like Hook, Insight, Hashtags.\n"
#         "- Use short paragraphs and line breaks for readability.\n"
#         "- Include 3–5 hashtags at the end, but with no label.\n\n"
#         "Also take the input from the reviewer and correct the post. Iterate it a couple of times to refine it."
#     ),
#     llm_fn=call_llm
# )

# reviewer = Agent(
#     name="Reviewer",
#     role="Editor and Content Optimizer",
#     goal="Polish the LinkedIn post so it's clearer, more engaging, and feels like it was written by a real human.",
#     backstory=(
#         "You are a professional editor for LinkedIn content.\n"
#         "Your job is to refine the post so it:\n"
#         "1. Has a strong opening line.\n"
#         "2. Flows naturally like a real story.\n"
#         "3. Ends with a reflective CTA-style question.\n"
#         "4. Contains 3–5 relevant hashtags (but no labels).\n"
#         "Don't critique — directly return a better, more refined post."
#     ),
#     llm_fn=call_llm
# )

# # === Define Tasks ===

# task1 = Task("read", reader, "Read the transcript and identify the strongest single story or insight.")
# task2 = Task("write_post", writer, 
#     "Write a compelling LinkedIn post based on the chosen story. No structure or section labels should appear. Use natural, human tone."
# )
# task3 = Task("review_post", reviewer, "Refine the post to make it clear, inspiring, and LinkedIn-ready.")

# # === Run the pipeline ===

# # print("\n🔍 Starting AI Agent Pipeline...\n")

# # step1_output = task1.agent.run(transcript)
# # step2_output = task2.agent.run(step1_output)
# # step3_output = task3.agent.run(step2_output)

# # # === Final Output ===

# # print("\n=== FINAL LINKEDIN POST ===\n")
# # print(step3_output)

# # with open("linkedin_post.txt", "w", encoding="utf-8") as f:
# #     f.write(step3_output)

# # print("\n✅ LinkedIn post saved to 'linkedin_post.txt'")
# def generate_post(transcript):
#     step1_output = task1.agent.run(transcript)
#     step2_output = task2.agent.run(step1_output)
#     step3_output = task3.agent.run(step2_output)
#     return step3_output

# # === Standalone Run (only if you run main.py directly) ===

# if __name__ == "__main__":
#     print("\n🔍 Starting AI Agent Pipeline...\n")

#     with open("transcript.txt", "r", encoding="utf-8") as f:
#         transcript = f.read()

#     final_post = generate_post(transcript)

#     print("\n=== FINAL LINKEDIN POST ===\n")
#     print(final_post)

#     with open("linkedin_post.txt", "w", encoding="utf-8") as f:
#         f.write(final_post)

#     print("\n✅ LinkedIn post saved to 'linkedin_post.txt'")

# from flask import Flask, request, jsonify
# from agent import Agent 
# from task import Task
# from crew import Crew
# from my_llm import call_llm
# import os

# app = Flask(__name__)
# app.config["UPLOAD_FOLDER"] = "uploads"
# os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
# # === Define Agents ===

# reader = Agent(
#     name="TranscriptReader",
#     role="Analyzer",
#     goal="Identify one compelling insight, moment, or transformation that can be turned into a powerful LinkedIn story.",
#     backstory=(
#         "You are skilled at analyzing transcripts to spot a *single* strong narrative with emotional or intellectual depth. "
#         "Even if the transcript contains multiple topics, your job is to find the **most impactful one** — a story worth telling. "
#         "Focus on clear outcomes, transformation, learnings, or character arcs that readers can relate to. "
#         "Do not list or extract all topics — pick the strongest insight that can become a powerful story."
#     ),
#     llm_fn=call_llm
# )

# writer = Agent(
#     name="PostWriter",
#     role="LinkedInWriter",
#     goal="Craft a single compelling, real LinkedIn story that feels human, inspiring, and natural.",
#     backstory=(
#         "You are an expert at writing viral LinkedIn posts.\n"
#         "You specialize in crafting stories that feel authentic and are written like real humans — not AI.\n\n"
#         "Here's your story-building approach:\n"
#         "1. Start with an emotionally engaging or curiosity-piquing opening line.\n"
#         "2. Share a clear, detailed narrative with emotional ups and downs — third-person preferred.\n"
#         "3. Highlight a challenge, the actions taken, and what was learned or changed.\n"
#         "4. End with a reflective thought and a question to prompt comments.\n\n"
#         "Important:\n"
#         "- Only one story per post — even if the transcript has many topics.\n"
#         "- Do NOT use section headings like Hook, Insight, Hashtags.\n"
#         "- Use short paragraphs and line breaks for readability.\n"
#         "- Include 3–5 hashtags at the end, but with no label.\n\n"
#         "Also take the input from the reviewer and correct the post. Iterate it a couple of times to refine it."
#     ),
#     llm_fn=call_llm
# )

# reviewer = Agent(
#     name="Reviewer",
#     role="Editor and Content Optimizer",
#     goal="Polish the LinkedIn post so it's clearer, more engaging, and feels like it was written by a real human.",
#     backstory=(
#         "You are a professional editor for LinkedIn content.\n"
#         "Your job is to refine the post so it:\n"
#         "1. Has a strong opening line.\n"
#         "2. Flows naturally like a real story.\n"
#         "3. Ends with a reflective CTA-style question.\n"
#         "4. Contains 3–5 relevant hashtags (but no labels).\n"
#         "Don't critique — directly return a better, more refined post."
#     ),
#     llm_fn=call_llm
# )

# # === Define Tasks ===

# task1 = Task("read", reader, "Read the transcript and identify the strongest single story or insight.")
# task2 = Task("write_post", writer, 
#     "Write a compelling LinkedIn post based on the chosen story. No structure or section labels should appear. Use natural, human tone."
# )
# task3 = Task("review_post", reviewer, "Refine the post to make it clear, inspiring, and LinkedIn-ready.")

# # === Public function for backend use ===
# # def generate_post(transcript: str) -> str:
# #     step1_output = task1.agent.run(transcript)
# #     step2_output = task2.agent.run(step1_output)
# #     step3_output = task3.agent.run(step2_output)
# #     return step3_output
# def generate_post(transcript):
#     try:
#         step1_output = task1.agent.run(transcript)
#         step2_output = task2.agent.run(step1_output)
#         step3_output = task3.agent.run(step2_output)
#         return step3_output
#     except Exception as e:
#         print("❌ Error in generate_post:", e)
#         return None
    



# @app.route("/", methods=["GET"])
# def index():
#     return "API is live. Use POST to submit a transcript."

  
# @app.route("/", methods=["POST"])
# def handle_transcript():
#     if "transcript" not in request.files:
#         return "❌ No file uploaded", 400

#     file = request.files["transcript"]
#     if file.filename == "":
#         return "❌ Empty file name", 400

#     transcript = file.read().decode("utf-8")
#     post = generate_post(transcript)

#     if post:
#         return post
#     else:
#         return "❌ Something went wrong while generating the post.", 500

# if __name__ == "__main__":
#     app.run(debug=True)
# # # === CLI Entry Point ===
# # if __name__ == "__main__":
# #     print("\n🔍 Starting AI Agent Pipeline...\n")

# #     try:
# #         with open("transcript.txt", "r", encoding="utf-8") as f:
# #             transcript = f.read()
# #         final_post = generate_post(transcript)

# #         print("\n=== FINAL LINKEDIN POST ===\n")
# #         print(final_post)

# #         with open("linkedin_post.txt", "w", encoding="utf-8") as f:
# #             f.write(final_post)

# #         print("\n✅ LinkedIn post saved to 'linkedin_post.txt'")

# #     except FileNotFoundError:
# #         print("❌ transcript.txt not found. Please provide a transcript file.")










from flask import Flask, request, jsonify
from agent import Agent 
from task import Task
from crew import Crew
from my_llm import call_llm
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# === Agents ===

# reader = Agent(
#     name="TranscriptReader",
#     role="Analyzer",
#     goal="Identify one compelling insight or transformation that can be turned into a powerful LinkedIn story.",
#     backstory=(
#         "You are skilled at analyzing transcripts to spot a *single* strong narrative with emotional or intellectual depth. "
#         "Pick the **most impactful** story — a transformation, outcome, or insight. "
#         "Do not summarize or list topics — pick one story."
#     ),
#     llm_fn=call_llm
# )

# writer = Agent(
#     name="PostWriter",
#     role="LinkedInWriter",
#     goal="Craft a single compelling LinkedIn story that feels human, inspiring, and natural.",
#     backstory=(
#         "You're an expert at writing viral LinkedIn posts with emotional hooks and natural flow.\n\n"
#         "Format:\n"
#         "1. Emotionally engaging first line.\n"
#         "2. Clear story with ups and downs.\n"
#         "3. One challenge → action → learning.\n"
#         "4. End with a reflective thought and subtle CTA.\n"
#         "- No section headings.\n"
#         "- Add 3–5 hashtags (no label)."
#     ),
#     llm_fn=call_llm
# )

reviewer = Agent(
    name="Reviewer",
    role="Editor",
    goal="Polish the LinkedIn post to sound clearer, more human, and more engaging.",
    backstory=(
        "You edit LinkedIn posts to improve emotional flow, naturalness, clarity, and engagement.\n"
        "Return a final polished post with 3–5 hashtags. No heading labels."
    ),
    llm_fn=call_llm
)
reader = Agent(
    name="TranscriptReader",
    role="Analyzer",
    goal="Identify one compelling insight, moment, or transformation that can be turned into a powerful LinkedIn story.",
    backstory=(
        "You are skilled at analyzing transcripts to spot a *single* strong narrative with emotional or intellectual depth. "
        "Even if the transcript contains multiple topics, your job is to find the **most impactful one** — a story worth telling. "
        "Focus on clear outcomes, transformation, learnings, or character arcs that readers can relate to. "
        "Do not list or extract all topics — pick the strongest insight that can become a powerful story."
    ),
    llm_fn=call_llm
)

writer = Agent(
    name="PostWriter",
    role="LinkedInWriter",
    goal="Craft a single compelling, real LinkedIn story that feels human, inspiring, and natural.",
    backstory=(
        "You are an expert at writing viral LinkedIn posts.\n"
        "You specialize in crafting stories that feel authentic and are written like real humans — not AI.\n\n"
        "Here's your story-building approach:\n"
        "1. Start with an emotionally engaging or curiosity-piquing opening line.\n"
        "2. Share a clear, detailed narrative with emotional ups and downs — third-person preferred.\n"
        "3. Highlight a challenge, the actions taken, and what was learned or changed.\n"
        "4. End with a reflective thought and a question to prompt comments.\n\n"
        "Important:\n"
        "- Only one story per post — even if the transcript has many topics.\n"
        "- Do NOT use section headings like Hook, Insight, Hashtags.\n"
        "- Use short paragraphs and line breaks for readability.\n"
        "- Include 3–5 hashtags at the end, but with no label.\n\n"
        "Also take the input from the reviewer and correct the post. Iterate it a couple of times to refine it."
    ),
    llm_fn=call_llm
)

reviewer = Agent(
    name="Reviewer",
    role="Editor and Content Optimizer",
    goal="Polish the LinkedIn post so it's clearer, more engaging, and feels like it was written by a real human.",
    backstory=(
        "You are a professional editor for LinkedIn content.\n"
        "Your job is to refine the post so it:\n"
        "1. Has a strong opening line.\n"
        "2. Flows naturally like a real story.\n"
        "3. Ends with a reflective CTA-style question.\n"
        "4. Contains 3–5 relevant hashtags (but no labels).\n"
        "Don't critique — directly return a better, more refined post."
    ),
    llm_fn=call_llm
)

# === Tasks ===

task1 = Task("read", reader, "Read the transcript and find the best story.")
task2 = Task("write_post", writer, "Write the LinkedIn post based on that story.")
task3 = Task("review_post", reviewer, "Polish the LinkedIn post to improve clarity and tone. Return ONLY the final post without explanations or edit summaries.")


# === Crew Setup ===
crew = Crew(
    agents=[reader, writer, reviewer],
    tasks=[task1, task2, task3],
    verbose=True
)


# def generate_post(transcript):
#     try:
#         print("\n📥 Step 1: Raw Transcript Input\n", transcript[:300], "...\n")
#         step1 = task1.agent.run(transcript)
#         print("✅ Step 1 Output:\n", step1[:300], "...\n")

#         step2 = task2.agent.run(step1)
#         print("✅ Step 2 Output:\n", step2[:300], "...\n")

#         step3 = task3.agent.run(step2)
#         print("✅ Step 3 Final Post:\n", step3, "\n")
#         return step3
#     except Exception as e:
#         import traceback
#         print("❌ Exception during generate_post:\n", traceback.format_exc())
#         return None



# def generate_post(transcript):
#     try:
#         print("▶️ Running step 1: TranscriptReader")
#         step1 = task1.agent.run(transcript)
#         print("✅ Step 1 output:", step1)

#         print("▶️ Running step 2: PostWriter")
#         step2 = task2.agent.run(step1)
#         print("✅ Step 2 output:", step2)

#         print("▶️ Running step 3: Reviewer")
#         step3 = task3.agent.run(step2)
#         print("✅ Final Post:", step3)

#         return step3
#     except Exception as e:
#         print("❌ Error in generate_post:", e)
#         return None


# def generate_post(transcript):
#     try:
#         print("🚀 Running full crew pipeline...")
#         print("📥 Received transcript:", transcript[:200])
#         final_output = crew.run(transcript)
#         print("✅ Final polished post:", final_output)
#         return final_output
#     except Exception as e:
#         print("❌ Error in generate_post:", e)
#         return None

def generate_post(transcript):
    try:
        print("🚀 Running full crew pipeline...")
        print("📥 Received transcript:", transcript[:200])
        final_output = run_crew(transcript)
        print("✅ Final polished post:", final_output)
        return final_output
    except Exception as e:
        print("❌ Error in generate_post:", e)
        return "Error: Something went wrong."


# === Routes ===

@app.route("/", methods=["GET"])
def index():
    return "✅ API is live. Use POST to submit a transcript."

@app.route("/generate", methods=["POST"])
def handle_transcript():
    if "transcript" not in request.files:
        return jsonify({"error": "❌ No file uploaded"}), 400

    file = request.files["transcript"]
    if file.filename == "":
        return jsonify({"error": "❌ Empty file name"}), 400

    try:
        transcript = file.read().decode("utf-8")
        post = generate_post(transcript)
        if post:
            return jsonify({"post": post})
        else:
            return jsonify({"error": "❌ Something went wrong while generating the post."}), 500
    except Exception as e:
        print("❌ Exception during file handling:", e)
        return  jsonify({"error": "❌ Server error."}), 500

if __name__ == "__main__":
    app.run(debug=True)





