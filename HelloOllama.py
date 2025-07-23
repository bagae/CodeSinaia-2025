import ollama

# Specify the model name
model_name = "gemma3:1b"

# Define the prompt
prompt=input('Ask?')

# Send the prompt to the model and get the response
response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])

# Print the response
print(type(response))
print(response['message']['content'])