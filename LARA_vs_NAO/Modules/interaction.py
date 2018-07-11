# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:14:07 2017

@author: dtozadore
"""

import sys
from modules import vars
from modules import dialog as diag
from modules import motion as mt
from modules import vision as vs
from modules import disatention as d 

#obs o raw_input e o input to python3
from modules.vision_components import results as rs
import time

import cv2
#import time


def main():
    
    info("Starting program ")            
    
    info("Connecting with NAO")    
    
    try:
        vars.initializer();
    except:
        info("Exception:" + sys.exc_info()[0])
    
    
    
    info("Starting vision system")
    
    #'''
    a = d.Th(1)	# thread de execucao
    a.start()

    str1  = 'rodando'
    while(str1 != 'sair'):
        
        str1 = raw_input()
        
        if(str1=='termina'):
            b = d.Th(2)	# thread de finalizacao
            b.start()
            diag.say("Terminando a thread")
            
            
            foo=vs.getImg(0)
            cv2.imshow("",foo)
            
            
            if not vars.attention:
                diag.say("Foi detectado um desvio alto.")
                #do something
                vars.attention = True
            
            #time.sleep(1)
            a = d.Th(1)	# thread de execucao
            a.start()
                
        

    b = d.Th(2)
    b.start()
    #'''
       
    #cv2.imshow("Saw",vs.getImg(0))
    #cv2.waitKey(0)


    info("Task finished!")     


















def class_vis():


    info("Starting program ")            
    
    info("Connecting with NAO")    
    
    try:
        vars.initializer();
    except:
        info("Exception:" + sys.exc_info()[0])
    
    
    
    info("Starting vision system")
    
   
    vs.initializate(vars. training_path, vars.classifierType)
    counter = 0

   # mt.run("Right_hand_up")       
    rs.initializate('teste_com_ruidos_pesados_'+ str(time.ctime()) +'.csv')
    while True:
        
        time.sleep(1)
        c = raw_input("( " + str(counter) + " ) label:") 
        counter += 1
        if c == "x":
            break
        
        im=vs.see()    
        
       # cv2.imshow("top-camera-320x240", im)
      #  cv2.waitKey(0)
        name = "newimg/" + c + "_" + str(time.ctime()) + ".jpg"

        cv2.imwrite(name,im)
        print("Image saved." + name)
     #   cv2.destroyAllWindows()
        

        
        
        ret = vs.classify(im, vars.classifierType)   
        ret['csv']['class'] = c
        rs.write_row(ret['csv'])
        
        vs.print_proba(ret, full=True, classifier=vars.classifierType)
        
    #diag.say("")    
    
    #vars.posture.goToPosture("Crouch", 1.0)
    
    
    #vars.finisher()
    
    
    #vars.motors.rest()

    
    
    
    
    
def info(stringToPrint):   
    
    
    if vars.debug:
            print("[INFO ] "+ stringToPrint)            

















    
if __name__ == "__main__":
    main()  
