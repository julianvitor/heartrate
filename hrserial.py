#-*- coding: utf-8 -*-
import serial

#porta serial do Arduino 

#SERIAL_PORT = '/dev/ttyACM0'  # ou 'COMX' no Windows
#BAUD_RATE = 9600

def hrcapture(SERIAL_PORT = '/dev/ttyACM0', BAUD_RATE = 9600):
    heart_rate = int(arduino.readline().decode().strip())    # Lê o valor da frequência cardíaca do Arduino
    return heart_rate
