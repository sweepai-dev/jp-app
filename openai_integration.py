import openai

def generate_jp_phrases(api_key, num_phrases=10, prompt="Generate 10 Japanese phrases for learning"):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100,
        n=num_phrases,
        stop=None,
        temperature=0.7,
    )

    phrases = [choice.choices[0].text.strip() for choice in response.choices]
    return phrases