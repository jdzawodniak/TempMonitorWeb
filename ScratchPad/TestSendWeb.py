# Imports
import requests
import os
import sys
import lcddriver
import time
import datetime
import RPi.GPIO as GPIO
import dht11

thingspeak_key = 'ZHAO5MQEKA0B93P7'
temperature = 23
humidity = 35




	# Send the data to Thingspeak
r = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'field1':temperature, 'field2':humidity})