# -*- coding: utf-8 -*-

import os



"""
Created on Thu May  4 16:06:04 2017

@author: dtozadore
"""




class ReadValues:
    """
     Class to hold read values
    
    """
    def __init__(self, deviations=0, emotionCount=0,
                 numberWord=0, time2ans=0, sucRate=0):
        self.deviations = deviations 
        self.emotionCount = emotionCount  
        self.numberWord =  numberWord
        self.time2ans = time2ans
        self.sucRate = sucRate
    
    def set(self, deviations=0, emotionCount=0,
                 numberWord=0, time2ans=0, sucRate=0):
        self.deviations = deviations 
        self.emotionCount = emotionCount  
        self.numberWord =  numberWord
        self.time2ans = time2ans
        self.sucRate = sucRate
        


userPar = ReadValues()

     

#variable to check if the robot is conected
naoConeted= True

# System Variables
debug = True
Ykey = 'y'
classifierType = "all"
training_path = "modules/vision_components/classifiers/DBIM/alldb"

emotions = {'happy': 0, 'sad': 0, 'angry': 0, 'disgust': 0,
 	'surprise': 0, 'fear': 0, 'neutral': 0}

#emotions = {'felicidade': 0, 'tristeza': 0, 'raiva': 0, 'nojo': 0,
 	#'surpresa': 0, 'fear': 0, 'neutra': 0}




deviation_times = []



def getBadEmotions():
	
	emo =  emotions['sad'] + emotions['angry'] +  emotions['disgust'] + emotions['fear']     
	print "Number of bad emotions", emo

	return emo


def clear_emo_variables():

	global emotions
	for i in emotions.keys():
		emotions[i] = 0
	
	#print "DEVIATION", deviation_times
	global deviation_times
	del deviation_times[:]
	

# Default Language
defaultLanguage = 'Brazilian'

ESC = 1048603 #27
ENTER = 1048586 #13

attention=False

current_path= os.getcwd()

#emotion vars
labels_dict = {
    0: 'happy', 1: 'neutral', 2: 'surprise',
    3: 'fear', 4: 'disgust', 5: 'angry', 6: 'sad'}


translated_emotions = {
    'happy': 'Feliz', 'neutral': 'neutro', 'surprise': 'surpresa',
    'fear': 'medo', 'disgust': 'nojo', 'angry': 'raiva', 'sad': 'tristeza'}



input_shape = (224,224,3)


'''
if(naoConeted):
    tts = ALProxy("ALTextToSpeech", robotIp, port)
    behavior = ALProxy("ALBehaviorManager", robotIp, port)
    motors =  ALProxy("ALMotion", robotIp, port)
    posture = ALProxy("ALRobotPosture", robotIp, port)
    camera = ALProxy("ALVideoDevice", robotIp, port)

def initializer():
	
	#vars.shapes = load_classes('shapes.csv')
    
	#if(naoConeted):
        #tts = ALProxy("ALTextToSpeech", robotIp, 9559)
#        tts = ALProxy("ALTextToSpeech", robotIp, 9559)
#        behavior = ALProxy("ALBehaviorManager", robotIp, 9559)
#        motors =  ALProxy("ALMotion", robotIp, 9559)
#        posture = ALProxy("ALRobotPosture", robotIp, 9559)

		
		#motors.wakeUp()

def finisher():
    
    
    if(naoConeted):
        motors.rest()

'''        





class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

   
   
def info(stringToPrint):   
    
    if debug:
            print bcolors.OKBLUE + "[I] " + stringToPrint + bcolors.ENDC

def war(stringToPrint):   
    
    if debug:
            print bcolors.WARNING + "[W] " + stringToPrint + bcolors.ENDC

def error(stringToPrint):   
    
    if debug:
            print bcolors.FAIL + "[E] " + stringToPrint + bcolors.ENDC

def nao_say(stringToPrint):   
    
    if debug:
            print bcolors.OKGREEN + "[Saying] " + stringToPrint + bcolors.ENDC


   
        
