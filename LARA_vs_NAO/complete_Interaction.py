# -*- coding: utf-8 -*-

import time
#import numpy as np


#from Modules import dialog
from Modules import vars as core
from Modules import disattention
#from Modules import vision
#import os
#import sys
#ip = "169.254.178.70"
#port = 9559

# ----- System imports -----

import sys
import time
import cv2
import csv
import os
import pickle
import random
from pprint import pprint
import numpy as np
import json
import socket
import time

# ---------- Activities Imports -------
from Activities.Jokenpo import jokenpo_main as jkp
from Activities.Atores import atores as emo
from Modules.Memory import fileHelper
from Activities.Exercicio import exercicio
from Activities.Drogas import drugs
from Activities.Prateleira  import shelf

class SocketInterface():
    def __init__(self):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect(('localhost', 8108))
    
    def say(self, txt):
        msg = {'text': txt, 'task': 'speak'}
        s_msg = json.dumps(msg)
        self.socket_send(s_msg)
        while self.clientsocket.recv(2) != 'ok':
            time.sleep(0.01)
    
    def move(self, lin_x=0.0, lin_y=0.0, lin_z=0.0, ang_x=0.0, ang_y=0.0, ang_z=0.0):
        msg = {'linear_x': lin_x, 'linear_y': lin_y, 'linear_z': lin_z,
               'angular_x': ang_x, 'angular_y': ang_y, 'angular_z': ang_z}
        msg['task'] = 'move'
        s_msg = json.dumps(msg)
        self.socket_send(s_msg)
        while self.clientsocket.recv(2) != 'ok':
            time.sleep(0.01)

    def activity(self, name, idx=None):
        msg = {'idx': idx, 'task': name}
        s_msg = json.dumps(msg)
        self.socket_send(s_msg)
        while self.clientsocket.recv(2) != 'ok':
            time.sleep(0.01)

    def socket_send(self, msg):
        self.clientsocket.send(msg)



def playActor():
    soI.say('Agora vou te mostrar minhas habilidades como ator. Primeiro, mostre cada uma das emoções contidas no papel que te entregagram, na ordem em que preferir. Doga OK robô quando estiver pronto.')
    raw_input('Press enter to start emotion recognition')
    soI.activity(name='actor')

    emojis = [':)', ':(',  '>:', ':&', ':!', ':o', ':O', '.']

    soI.say("Agora é a sua vez de descobrir. Tente dizer qual expressão eu estou mostrando")
    soI.say("Está pronto?")
    soI.say("Anote qual emoção você acha que é e me diga quando estiver pronto para a próxima.")


    for i,emoji in enumerate(emojis):
        #display_emotion(robot, max(core.emotions, key=core.emotions.get))
        soI.say("Emoção número " + str(i+1))
        soI.say(emoji)
        soI.say("Pronto?")
        raw_input("GO!")




def main():
    soI = SocketInterface()
    
    playActor()
    exit()

    #----- move stuff    
    soI.move(ang_z=1.0)
    time.sleep(1.5)
    soI.move()
    soI.move(ang_z=-1.0)
    time.sleep(3.0)
    soI.move()
    soI.move(ang_z=1.0)
    time.sleep(1.5)
    soI.move()

    prefferences = False

    userModel = fileHelper.fileHelper()
    soI.say(u'Boa tarde, humano! Meu nome é Lara. E o você, qual é seu nome?')
    nome = raw_input()
    soI.say("Que nome top!")
    
    if prefferences:    
        soI.say(u'Qual é a sua idade?')
        answer = raw_input()
        userModel.addPreference(nome, answer, 'idade')
       
        print(u'Qual é o seu esporte favorito?')
        soI.say("Qual seu esporte favorito?")
        answer = raw_input()
        userModel.addSearchQueue([answer], nome, 'esporte favorito')
        
        print(u'Qual é a sua comida favorita?')
        soI.say("Qual sua comida favorita?")
        answer = raw_input()
        userModel.addSearchQueue([answer], nome, 'comida favorita')

        print(u'Qual é a sua musica favorita?')
        soI.say("Qual sua banda preferida?")
        answer = raw_input()
        userModel.addSearchQueue([answer], nome, 'musica favorita')
        
        print('Getting preferences...')
        preferences = userModel.getPreferences(nome)
        print('Got preferences!')
        userModel.join()
        print('Joint threads!')

    soI.say(" Vamos fazer uma série de atividades agora! Está preparado? Vamos lá")
    
   
    # Change Activities Orders: 
    drugs.play(soI)
    
    userModel.join()
    userModel.close()

    try:
        esporte = u'Sobre seu esporte preferido: \n{}'.format(
            userModel.searchFile([preferences['esporte favorito'].encode('utf-8')])).encode('utf-8')
        comida = u'\nSobre sua comida preferida: \n{}'.format(
            userModel.searchFile([preferences['comida favorita'].encode('utf-8')])).encode('utf-8')
        musica = u'\nSobre sua música preferida: \n{}'.format(
            userModel.searchFile([preferences['musica favorita'].encode('utf-8')])).encode('utf-8')
    
    except Exception as e:
        print(e)

    #soI.say( esporte )
    
    #shelf.play(soI)
    if prefferences:
        soI.say( comida )
    
    #exercicio.play(soI) 
    jkp.play( soI, None, 3 )


    soI.say("Agora vou te mostrar minhas habilidades como ator. Primeiro mostre cada uma das emocoes contidas no papel que te entregaram, na ordem que preferir. Diga Ok robo quanto estiver pronto")
    raw_input("Press enter to start emotion recognition")

    attention = disattention.Th(1)
    attention.start()

    soI.emotions()
    #emo.play(soI, attention)
    attention._end_classification()

    if prefferences:
        soI.say( musica )



    soI.say("Então é isso. Foi um prazer interagir com você, "+ nome +" . Espero te ver em breve. Até mais.")
    

if __name__=="__main__":
    main()
    
    
    
    


    
