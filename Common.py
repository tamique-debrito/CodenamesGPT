from openai import OpenAI

API_KEY="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"

client = OpenAI(api_key=API_KEY)

def test():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say this is a test"}],
    )
    print(completion)