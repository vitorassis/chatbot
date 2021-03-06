from app import app
from flask import Flask, jsonify, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os.path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response')
def get_response():
    bot = ChatBot('botinho')
    text = request.args.get('text')

    return jsonify(result=str(bot.get_response(text)))

@app.route('/train')
def train():
    return render_template('train.html')

@app.route('/train_talk')
def train_talk():
    bot = ChatBot('botinho')
    trainer_corpus = ChatterBotCorpusTrainer(bot)
    trainer_corpus.train("chatterbot.corpus.portuguese")
    if request.args.get('talk') != None:
        talk = request.args.get('talk').split("\n")
    else:
        talk = []
    trainer = ListTrainer(bot)
    if not os.path.isfile('db.sqlite3'):
        os.mknod('db.sqlite3')
    trainer.train(talk)
    return jsonify(result='Bot treinado com sucesso')

@app.route('/exclude')
def exclude():
    psswd = request.args.get('psswd')
    if not os.path.isfile('db.sqlite3'):
        ret = 'Bot já sem memória'
    if psswd == 'zerar':
        os.remove('db.sqlite3')
        train_talk()
        ret = 'Memória excluída'

    else:
        ret = 'Senha incorreta!'
    return jsonify(result=ret)
