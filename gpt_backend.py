import openai
import os

# Replace this with your real OpenAI API key



client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(question):
    # ❌ Do not redefine client inside the function
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
