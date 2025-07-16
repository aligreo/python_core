
from openai import OpenAI
from helpers import settings

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=settings.OPEN_ROUTER_API_KEY,
)

def get_sentiment(text: str):
    """
    Function to get sentiment analysis of a given text.
    """
    response = client.chat.completions.create(
        model=settings.OPEN_ROUTER_MODEL_ID,
        messages=[
            {
                "role": "system",
                "content": "You are a sentiment analysis model that classifies text in one word as positive, negative, or neutral."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content
