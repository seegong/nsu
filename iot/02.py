import RPi.GPIO as cc
import time

led = 4

cc.setwarnings(False) 
cc.setmode(cc.BCM) 

for k in range(3):
    cc.output(led,cc,1)    
    time.sleep(2)
    cc.output(led,cc,0)
    time.sleep(2)

cc.cleanup()
