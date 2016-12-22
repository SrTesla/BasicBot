#coding: utf-8

import telepot, time

TOKEN = "265190984:AAF43FB_YYXCVE2ZnC6lrEv7v4uiiikZg5Q"# Token
bot = telepot.Bot(TOKEN)
print ('Conectado')

def handle(msg):
	tipomsg, tchat, chat_id = telepot.glance(msg)
	print(tipomsg, tchat, chat_id)

	try:
		nick = msg['from']['username']#username, @username
	except:
		nick = ""

	uid = str(msg['from']['id'])#id
	pnome = msg['from']['first_name']#Primeiro nome
	try:
		nomegp = msg['chat']['title']#Nome do grupo
	except:
		pass
	try:
		adicionado = msg['new_chat_member']['first_name']#nome de um membro adicionado
	except:
		pass

	msgid = msg['message_id']#id da msg
	gid = msg['chat']['id']#id do grupo

	try:
		rpnome = rid = msg['reply_to_message']['from']['first_name']#mostra o primeiro nome de um reply
	except:
		pass
	try:
		rid = str(msg['reply_to_message']['from']['id'])#mostra o id de um reply
	except:
		pass

	if tipomsg == 'new_chat_member':
		m = "*{}*, ao *{}*".format(adicionado, nomegp)
		time.sleep(1)
		bot.sendMessage(chat_id, "Bem-vindo(a) "+m, parse_mode='Markdown')

	try:
		mn = (msg['text']).lower().split(' ')
	except:
		pass

	if mn[0] == '/afk':
		frase = mn[1:]
		nfrase = ''.join(frase)
		if nfrase == "":
			nfrase = "Não especificado."
		m = "Usuário *{}* está AFK. \n*Motivo:* {}".format(nick, nfrase)
		bot.sendMessage(chat_id, m, reply_to_message_id=msgid, parse_mode='Markdown')

	elif mn[0] == "/back":
		frase = mn[1:]
		nfrase = ' '.join(frase)
		m = "{}, *{}* Voltou. ".format(pnome, nick)

		try:
			bot.sendMessage(chat_id, m, reply_to_message_id=msgid, parse_mode='Markdown')
		except:
			bot.sendMessage(chat_id, "_Algo errado não está certo e.e_", reply_to_message_id=msgid, parse_mode='Markdown')

	elif mn[0] == "/id":
		m = "*{}* seu ID: *{}*".format(pnome, uid)
		bot.sendMessage(chat_id, m, reply_to_message_id=msgid, parse_mode='Markdown')

	elif mn[0] == "/mid":
		m = "*{}* \nID: *{}*".format(rpnome, rid)
		bot.sendMessage(chat_id, m, reply_to_message_id=msgid, parse_mode='Markdown')

bot.message_loop(handle)

while 1:
    time.sleep(10)
