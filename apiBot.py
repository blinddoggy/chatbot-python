#fixed logging
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask
#escaping
from markupsafe import escape

app = Flask(__name__)

app.debug = True

@app.route("/<r>")
def hello_world(r):

    # name of bot
    chatbot=ChatBot('corona bot')
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    # training with corpus
    trainer.train("chatterbot.corpus.english")

    response = chatbot.get_response(escape(r))
    print(response.text)
    return response.text

@app.route('/hello')
def hello():
    return 'Hello, World'

