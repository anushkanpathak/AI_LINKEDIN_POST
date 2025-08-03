
# from ollama import Client

# client = Client(host='http://localhost:11434')  # Default Ollama port

# def call_llm(prompt: str) -> str:
#     print(" LLaMA 3.2 is thinking... please wait...\n")
#     response = client.chat(model='llama3.2:latest', messages=[
#         {"role": "user", "content": prompt}
#     ])
#     return response['message']['content'].strip()



from ollama import Client

# Define the Ollama client
client = Client(host="http://localhost:11434")  # default port for Ollama

def call_llm(prompt: str) -> str:
    try:
        print("📡 LLaMA 3.2 is thinking...\nPrompt:\n", prompt)
        response = client.chat(
            model='llama3.2:latest',
            messages=[{"role": "user", "content": prompt}]
        )
        print("🧠 LLM Response:\n", response['message']['content'])
        return response['message']['content'].strip()
    except Exception as e:
        print("❌ LLM call failed:", e)
        return "Error: LLM call failed"
