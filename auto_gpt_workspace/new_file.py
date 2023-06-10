import openai

openai.api_key = 'YOUR_SECRET_API_KEY'

def generate_text(prompt):
    completions = openai.Completion.create(
        engine='davinci',
        prompt=prompt[:2048], # reducing the length of the prompt to be within the maximum context length of the model
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message