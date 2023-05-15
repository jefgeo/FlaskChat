from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import chat_api
from waitress import serve

app = Flask(__name__)

# must create .env with ChatGPT key (not included in git repo)
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

chatter = chat_api.ChatAPI(api_key)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        content = request.form['question']
        response, stats = chatter.get_chat_response(content)
        # print(response, stats)
        return render_template('index.html', answer=response, stats=stats)


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5001)
else:
    serve(app, host="0.0.0.0", port=5000)

