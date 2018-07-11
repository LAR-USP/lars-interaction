# -*- coding: utf-8 -*-
import time
#from Modules import vars as core
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

play_book = ["pedra","papel","tesoura"]

behaviors = ["PedraAberto","PedraFechado", "PapelAberto","PapelFechado", "TesouraAberto","TesouraFechado" ]

            
def jokenpo(primeira_jogada,segunda_jogada):

        
    ganhador = ''
    perdedor = ''
    result = ''

    if primeira_jogada == segunda_jogada:
        result = 0
        ganhador = primeira_jogada
        perdedor = primeira_jogada
    
    '''
    ganha_de = {
    'pedra': 'tesoura',
    'tesoura': 'papel',
    'papel': 'pedra',
    }

    if ganha_de[primeira_jogada] == segunda_jogada:
        ganhador = primeira_jogada
        perdedor = segunda_jogada
    else:
        ganhador = segunda_jogada
        perdedor = primeira_jogada
        

      
    '''
    
    if primeira_jogada == 'pedra' and segunda_jogada == 'tesoura':
        ganhador = 'pedra'
        perdedor = 'tesoura'
        result = 1
        
    if primeira_jogada == 'tesoura' and segunda_jogada == 'pedra':
        ganhador = 'pedra'
        perdedor = 'tesoura'
        result = -1
        
    if primeira_jogada == 'tesoura' and segunda_jogada == 'papel':
        ganhador = 'tesoura'
        perdedor = 'papel'
        result = 1
        
    if primeira_jogada == 'papel' and segunda_jogada == 'tesoura':
        ganhador = 'tesoura'
        perdedor = 'papel'
        result = -1
        
    if primeira_jogada == 'papel' and segunda_jogada == 'pedra':
        ganhador = 'papel'
        perdedor = 'pedra'
        result = 1
        
        
    if primeira_jogada == 'pedra' and segunda_jogada == 'papel':
        ganhador = 'papel'
        perdedor = 'pedra'
        result = -1
    
    return result, ganhador, perdedor       



def play(robot, ds,round_numbers=3):
    

    ##-------- Real Play

    robot.say('vamos jogar jo ken po')
    behaviors = np.arange(round_numbers)
    np.random.shuffle(behaviors)
    for turn in range(0,round_numbers):
        #time.sleep(15)
        #pass
        #print(core.emotions)
        robot.say("Rodada número " + str(turn+1))


        # behave = np.random.randint(0,3)
        behave = behaviors[turn]
    
        print "Behave", behave
    
        p1 = behave
        #p2 = np.random.randint(0,2)

        robot.say("Jó")
        time.sleep(0.2)

        robot.say("Ken")
        time.sleep(0.2)

        robot.say("Pô!")

        robot_move = play_book[p1]
        #-- Generic function to execute jokenpo play
        robot.activity('jokenpo', behave)
 
        p2 = int(raw_input("Player play (1-3): ")) -1

        print "p1: " , play_book[p1]
        print "p2: ", play_book[p2]
        print "behave", behave
    
      
        
        #ds.say("Eu escolho " +  play_book[p1])
        
        play,w,l = jokenpo(play_book[p1],play_book[p2])
    
        
        robot.say(" eu escolhi " +  play_book[p1] + " e voce escolheu " + play_book[p2])
    
        print "result: ", play

        if play > 0:
            robot.say("Eu ganhei porque " +  w + " ganha de " + l)
            #print "Robô ganhou porque ", w ," ganha de ", l    

        elif play < 0:  
            robot.say("Voce ganhou porque " +  w + " ganha de " + l)
            #print "Player ganhou porque ", w ," ganha de ", l
    
        else:
            robot.say("Empatou porque escolhemos a mesma coisa")
            #print "empate porque ", w ," e ", l, "são iguais"

def info(stringToPrint):   
    if core.debug:
            core.info(stringToPrint)            

    
def war(stringToPrint):   
    if core.debug:
            core.war(stringToPrint)            

    
def error(stringToPrint):   
    if core.debug:
            core.error(stringToPrint)            




