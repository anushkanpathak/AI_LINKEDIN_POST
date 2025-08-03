from ollama import Client

client = Client()

response = client.chat(
    model='llama3.2:latest',
    messages=[
        {"role": "user", "content": "What is leadership?"}
    ]
)

print(response['message']['content'])
