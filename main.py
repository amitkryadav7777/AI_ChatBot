from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from gtts import gTTS
import pyttsx3
from flask import Flask, render_template, request

app = Flask(__name__)


#pyyaml = 5.4.1
language = "en"

# bot = ChatBot("Optimus", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])
bot = ChatBot("Optimus", read_only=False, logic_adapters=[
        {
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"Sorry! I don't have an answer",
            "maximum_similarity_threshold" : 0.9
        }
    ])

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")


@app.route("/")
def main():
    return render_template("index.html")


# for using chatbot on console
# while True :
#     user_response = input("User : ")
#     girl = pyttsx3.init()
#     voices = girl.getProperty('voices')
#     girl.setProperty('voice',voices[1].id)
#     girl.setProperty('rate',150)
#     text = bot.get_response(user_response)
#     print("Optimus :", bot.get_response(user_response))
#     girl.say(text)
#     girl.runAndWait()

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    girl = pyttsx3.init()
    voices = girl.getProperty('voices')
    girl.setProperty('voice',voices[1].id)
    girl.setProperty('rate',150)
    text = bot.get_response(userText)
    girl.say(text)
    girl.runAndWait()
    return str(text)


if __name__ == "__main__" :
    app.run(debug=True)