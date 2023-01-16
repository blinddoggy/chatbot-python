#fixed logging
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

from chatterbot.conversation import Statement
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# name of bot
chatbot=ChatBot('corona bot')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
# training with corpus
trainer.train("chatterbot.corpus.spanish")

while True:
	query = input(">>>")
	print(chatbot.get_response(Statement(text=query, search_text=query)))
