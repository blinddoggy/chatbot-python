#fixed logging
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# name of bot
chatbot=ChatBot('corona bot')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
# training with corpus
trainer.train("chatterbot.corpus.english")
response = chatbot.get_response('Good Morning')
print(response)
response = chatbot.get_response('what is hisory')
print(response)
