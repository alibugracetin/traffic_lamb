import RPi.GPIO as GPIO
from time import sleep
import buzzer_folder

GPIO.setmode(GPIO.BCM)
led_red = GPIO.setup(26,GPIO.OUT)
led_yellow = GPIO.setup(20,GPIO.OUT)
led_green = GPIO.setup(12,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
buzzer_pin=17
i=0
for i in range(10):

    GPIO.output(26,True)  
    buzzer_folder.buzzer(buzzer_pin)
    i+=1
       
GPIO.output(20,True) 
buzzer_folder.buzzer(buzzer_pin)
sleep(.1200)

GPIO.output(26,False)
GPIO.output(20,False)

GPIO.output(12,True) 
sleep(10)
GPIO.output(12,False)
GPIO.cleanup()       
