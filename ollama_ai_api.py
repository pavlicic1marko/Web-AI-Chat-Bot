import ollama

model = "llama3.1"

def ask_ollama(prompt):
    response = ollama.chat(model=model, messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])

    return response['message']['content']
