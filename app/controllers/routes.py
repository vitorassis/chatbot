from app import app
from flask import Flask, jsonify, render_template, request
from chatterbot import ChatBot

bot = ChatBot('botinho')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response')
def get_response():
    text = request.args.get('text')

    return jsonify(result=str(bot.get_response(text)))
