# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import cv2
# ROS
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import subprocess
import disattention
from Modules import vars as core

# SOCKET
import socket
import random
import numpy as np
import time
import json
#QT
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtCore

#from threading import Thread
import thread

class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = 'LARa'
        self.left = 1100
        self.top = 10
        self.width = 900
        self.height = 1000
        self.initUI()
        self.pub = rospy.Publisher('robot_face/text_out', String, queue_size=1)


        self.velocity_pub = rospy.Publisher('/pioneer/cmd_vel', Twist, queue_size=1)
        self.say_pub = rospy.Publisher('/speak', String, queue_size=1)
        rospy.init_node('LARa', anonymous=True)

        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(('localhost', 8108))
        self.serversocket.listen(1)
    
        self.standby_gif = QMovie('imgs/default.gif')
        self.standByLabel.setMovie(self.standby_gif)
        self.standByLabel.resize(900,1000)
        self.standby_gif.start()

    def get_socket_msg(self):
        msg = self.a.recv()
        return msg

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create widget
        self.standByLabel = QLabel(self)
        self.imgLabel = QLabel(self)
        self.showStandby()

    def route_msg(self, msg):
        task = msg['task']

#        if task == 'pills':
#            self.initPills()
#        elif task == 'shelf':
#            self.initShelf()
        if task == 'exercise':
            self.initExercise(msg['idx'])
        elif task == 'actor':
            self.initEmotion()
        elif task == 'jokenpo':
            self.initJoKenPo(msg['idx'])
        elif task == 'speak':
            self.speak(msg['text'].encode('utf-8'))
        elif task == 'move':
            self.move(msg)

    def initExercise(self, idx):
        if idx == 0:
            img = 'imgs/exercicio/stretch1.png'
        elif idx == 1:
            img = 'imgs/exercicio/stretch2.png'
        elif idx == 2:
            img = 'imgs/exercicio/stretch2.png'
        else:
            img = 'imgs/exercicio/stretch3.png'
        self.showimage(img)

    def initJoKenPo(self, idx):
        if idx == 0:
            img = 'imgs/jokenpo/rock.png'
        elif idx == 1:
            img = 'imgs/jokenpo/paper.png'
        elif idx == 2:
            img = 'imgs/jokenpo/scizor.png'
        self.showimage(img)
        time.sleep(3)
        self.showStandby()

    def speak(self, text):
        #self.say_pub.publish(text)
        #time.sleep(3)
        print( 'speak callback function' )
        if len(text) <=2 and (':' in text or text == '.'):
            self.pub.publish(text) 
            return 1

        text = text.replace('=','')
        self.pub.publish( text )
        #time.sleep(0.5)
        print( 'published sentece' )
        subprocess.call( [ 'lianetts', '-s',  '1.0', text ] ) # blocking
        print( 'sentence spoken!' )


    def move(self, msg):
        vel_msg = Twist()

        vel_msg.linear.x = msg.get('linear_x', 0)
        vel_msg.linear.y = msg.get('linear_y', 0)
        vel_msg.linear.z = msg.get('linear_z', 0)
        vel_msg.angular.x = msg.get('angular_x', 0)
        vel_msg.angular.y = msg.get('angular_y', 0)
        vel_msg.angular.z = msg.get('angular_z', 0)

        self.velocity_pub.publish(vel_msg)

    def initEmotion(self):
        att = disattention.Th(1)
        att.start()

        emotions_list = ['Alegria', 'Triste', 'Raiva', 'Nojo',
        'Surpresa', 'Medo', 'Neutral']
        
        rand_emo = random.randint(0,6)
            
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
           emo_result = core.translated_emotions[max(core.emotions, key=core.emotions.get)]
                
           print( "Traduzida", emo_result)
     #      robot.say("A expressão que eu detectei foi, " + emo_result)
            
           if(i < 5):
               self.speak("Agora me mostre outra emoção")
           else:
               self.speak("Perfeito, estou aprendendo as emoções")
           
           print core.emotions
           core.clear_emo_variables()

           print "Emo:", emotions_list[i]
           print core.emotions

        att._end_classification()

    def showStandby(self):
    #    self.imgLabel.hide()
        self.standByLabel.show()
        self.show()
        self.standByLabel.raise_()

    def showimage(self, img_path):
        #self.standby_gif.stop()
        pixmap = QPixmap(img_path)
        pixmap.scaledToHeight(1000)
        pixmap.scaledToWidth(1000)
        self.imgLabel.setPixmap(pixmap)
        self.imgLabel.resize(900,1000)

        #self.standByLabel.hide()
        self.imgLabel.show()
        self.show()
        self.imgLabel.raise_()
       
def listen(ex):
    connection, address = ex.serversocket.accept()
    while True:
        buf = connection.recv(2048)
        if len(buf) > 0 and buf.startswith('{'):
            print(buf)
            try:
                msg = json.loads(buf)
                ex.route_msg(msg)
                connection.send('ok')
            except Exception as e:
                print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    thread.start_new_thread(listen, (ex,))
    app.exec_()
    sys.exit()
