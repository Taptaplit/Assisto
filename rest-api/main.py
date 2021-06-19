from cleverbotfree import Cleverbot
from flask import Flask, request

@Cleverbot.connect
def chat(bot, text):
    reply = bot.single_exchange(text)
    bot.close()
    return reply

app = Flask(__name__)

@app.route('/', methods=["POST"])
def chatRoute():
    text = request.json['text']
    res = chat(text)
    return res 

app.run()