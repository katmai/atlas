# Import the OpenAI API key and GPT-3.5 API wrapper
import openai_secret_manager
import openai

# Load the API key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# Authenticate with the API
openai.api_key = secrets['api_key']

# Define the prompt for the story
prompt = "Once upon a time, there was a [noun]. The [noun] was [adjective] and [adjective]."

# Generate the story using the GPT-3.5 API
story = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated story
print(story.choices[0].text)