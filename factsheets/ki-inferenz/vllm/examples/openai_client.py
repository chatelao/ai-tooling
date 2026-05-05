from openai import OpenAI

# vLLM is API-compatible with OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="token-is-ignored-by-vllm",
)

completion = client.chat.completions.create(
  model="facebook/opt-125m",
  messages=[
    {"role": "user", "content": "Explain quantum computing in one sentence."}
  ]
)

print(completion.choices[0].message.content)
