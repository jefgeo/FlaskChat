import chat_api
import os
from dotenv import load_dotenv
import chat_api

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

chatter = chat_api.ChatAPI(api_key)

models = chatter.get_model_names()

content = None

while not content:
    content = input("enter query: ")
response, stats = chatter.get_chat_response(content)
print(response)
print(stats)

