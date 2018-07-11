# -*- coding: utf-8 -*-
import time
from Modules import vars as core

# ----- System imports -----

import sys
import time
import cv2
import csv
import os
import random
import numpy as np


def play(robot, att):
    
    emotions_list = ['Alegria', 'Triste', 'Raiva', 'Nojo',
    'Surpresa', 'Medo', 'Neutral']
    
    rand_emo = random.randint(0,6)

    robot.say("Agora vou te mostrar minhas habilidades como ator. Primeiro mostre cada uma das emocoes contidas no papel que te entregaram, na ordem que preferir. Diga Ok robo quanto estiver pronto")
    raw_input("Press enter to start emotion recognition")
            
    for i in range(0,6):
       print('ESTOU AQUIIIII') 
       att._continue()
       print(core.emotions)
       #print "Faça para mim a expressão facial de" , emotions_list[i]
       #print "Agora vou te mostrar minhas habilidades como ator. Mostre uma expressão entre Alegria, Tristeza, Raiva, Nojo, Surpresa ou Medo que eu vou imitar"
       #Reconhecimento de emoções
       # Intervalo de tempo I, escolhe a emoção amis detectada 
       time.sleep(4)
       att._halt()


       core.emotions['neutral']=0
            
       print "Mais detectada",  max(core.emotions, key=core.emotions.get)
            
       #robot.say("A expressão que eu detectei foi, " + max(core.emotions, key=core.emotions.get))
       emo_result = core.translated_emotions[max(core.emotions, key=core.emotions.get)]
            
       print( "Traduzida", emo_result)
       robot.say("A expressão que eu detectei foi, " + emo_result)
        
        
       if(i < 5):
           robot.say("Agora me mostre outra emoção")
       else:
           robot.say("Perfeito, estou aprendendo as emoções")
       
       print core.emotions
    
        
       core.clear_emo_variables()

       print "Emo:", emotions_list[i]
       print core.emotions

    #pessoa adivinha emoções do nao
    #robot.say("Agora e a sua vez de descobrir. Tente dizer qual expressao eu estou mostrando")

    emojis = [':)', ':(',  '>:', ':&', ':!', ':o', ':O', '.']


    robot.say("Agora é a sua vez de descobrir. Tente dizer qual expressão eu estou mostrando")
    robot.say("Está pronto?")
    robot.say("Anote qual emoção você acha que é e me diga quando estiver pronto para a próxima.")

    

    for i,emoji in enumerate(emojis):
        
        #display_emotion(robot, max(core.emotions, key=core.emotions.get))

        robot.say("Emoção número " + str(i+1))
        robot.say(emoji)
        robot.say("Pronto?")
        raw_input("GO!")
        

    
    #return 1       
    



















