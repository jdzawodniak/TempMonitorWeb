 #Import necessary libraries for communication and display use
import requests
import os
import sys
import lcddriver
import time
import datetime
import RPi.GPIO as GPIO
import dht11

################# Default Constants #################
# These can be changed if required

thingspeak_key = 'ZHAO5MQEKA0B93P7'
#####################################################

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()


# read data using pin 17
instance = dht11.DHT11(pin=17)

# Main body of code
try:
    while True:
        result = instance.read()
        if result.is_valid():
            temperatureC = result.temperature
            temperatureF=(result.temperature * 9/5)+32
            humidity = result.humidity
            
            
            F=(result.temperature * 9/5)+32
            C=result.temperature
            H=result.humidity
            unit1="F"
            unit2="C"


            print("Writing to display")
           
            
            L1= "Temp %d %s / %d %s ." % (F, unit1, C, unit2)
            L2= "Humidity is %d %%." %(H)
            print (F)
            print (C)
            print(L1)
            print(L2)
           
            display.lcd_display_string(L1, 1) # Write just first line to the display
            display.lcd_display_string(L2, 2) # Write second line o the display
            #display.lcd_display_string(str(C), 2) 
            time.sleep(600)  
            display.lcd_clear()  


            #time.sleep(2) # puts code to sleep between cycles
            
            ##################
            #Send data to web

            r = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'field1':temperatureC, 'field2':temperatureF, 'field3':humidity})
            
            #################






except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
