from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random

bot = ChatBot('Botinho')

talk = [
	'Oi',
	'Olá'
]

talk2 = [
	'Boa noite!',
	'Boa noite'
]

talk3 = [
	'Tudo bem?',
	'Estou bem, eai?'
]

talk4 = [
	'Boa tarde!',
	'Boa tarde'
]

talk5 = [
	'Como vai?',
	'Vou bem, e você?',
	'Que bom! Estou bem também'
]

talk6 = [
	'Bom dia!',
	'Bom dia'
]

talk7 = [
	'Que a Força esteja com você!',
	'Com você também!'
]

talk8 = [
	'Como foi seu dia?',
	'Foi bom, e o seu?',
	'O meu foi bom também!'
]

talk9 = [
	'Tchau',
	'Até mais'
]

talk10 = [
	'Seu nome',
	'VAI, Vitor Artificial Intelligence'
]

talk11 = [
	'Boa noite',
	'Palmeiras não tem mundial!'
]

trainer = ListTrainer(bot)
trainer.train(talk)
trainer.train(talk2)
trainer.train(talk3)
trainer.train(talk4)
trainer.train(talk5)
trainer.train(talk6)
trainer.train(talk7)
trainer.train(talk8)
trainer.train(talk9)
trainer.train(talk10)
trainer.train(talk11)

#rand = list(set().union(talk, talk2, talk3, talk4, talk5, talk6, talk7, talk8))
#trainer.train(random.shuffle(rand))

