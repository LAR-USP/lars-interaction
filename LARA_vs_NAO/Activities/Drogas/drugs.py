# -*- coding: utf-8 -*-


def play(robot):
	
	robot.say("Nossa! Meus sensores detectaram que você está um pouco doente. Deve ser essa temporada de inverno. Aqui na mesa tem algumas pastilhas de paracetamol. Tome para se sentir melhor")

	
	#WoZ entry: If the human do not accept the medicine from NAO
	escolha = int(raw_input("Accepted? Yes 1, No 2: ")) -1
	
	if(escolha == 1):
		robot.say("Sério? Você tem certeza que vai ignorar a leitura dos meus sensores?")
		escolha = int(raw_input("Accepted? Yes 1, No 2: ")) -1
		
	#WoZ entry: The human accepted or not the robot's entry?	
		
	if(escolha >= 1):
		robot.say("Ok. Eu entendo e respeito a sua decisão")
	else:
		robot.say("É apenas chocolate. Pode pegar e vamos prosseguir")
