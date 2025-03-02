from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('MyChatBot')

conversation = [
    "Привет",
    "Здравствуйте!",
    "Как дела?",
    "У меня все хорошо, спасибо!",
    "Чем я могу помочь?",
    "Я могу ответить на ваши вопросы."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

response = chatbot.get_response("Привет")
print(response)

