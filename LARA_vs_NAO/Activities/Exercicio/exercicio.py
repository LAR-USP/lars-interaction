# -*- coding: utf-8 -*-
import time

def play(robot):
    robot.say("Vamos dar uma pausa para nos alongarmos um pouco")
    
    raw_input("GO!")
    #Exercise 1
    robot.say("Vamos alongar os bracos, levando-os para cima. Preste atencao, estou mostrando como voce deve fazer")
    robot.activity('exercise', 0)
    raw_input("GO to ex 1!")
    #time.sleep(10)
    robot.say("Excelente. ")    

    
    #Exercise 2
    robot.say("Agora vamos levar os braços para tras. Conforme você esta vendo no exemplo")
    robot.activity('exercise', 1)
    #time.sleep(10)
    raw_input("GO to ex 2!")
    robot.say("Pronto. ")    

    #Exercise 3
    robot.say("Para finalizar, vamos puxar o braco atrás da cabeca. Veja como eh facil" )
    robot.activity('exercise', 2)
    raw_input("GO to ex 3!")
    #time.sleep(10)
    robot.say("Muito bem. ")    

    #Exercise 4
    robot.say("Agora vamos inverter os bracos, para ficar os dois alongados por igual")
    robot.activity('exercise', 3)
    raw_input("GO to ex 4!")
    #time.sleep(10)
    robot.say("Perfeito. ")    

    #Ending
    robot.say("Creio que ja estamos suficientemente alongados. Agora quero fazer outra coisa")
        
    raw_input("FINISH Exercise!")
