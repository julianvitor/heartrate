#-*- coding: utf-8 -*-
import serial

#porta serial do Arduino 
#SERIAL_PORT = '/dev/ttyACM0'  # ou 'COMX' no Windows
#BAUD_RATE = 9600

#def serialinput(SERIAL_PORT = '/dev/ttyACM0', BAUD_RATE = 9600):
#    serialvoltage = int(arduino.readline().decode().strip())    # Lê o valor da frequência cardíaca do Arduino
#    return tensao_atual


# Função para simular a obtenção de dados de tensão do Arduino (substitua por sua função real)
def serialinput():
    # Suponhamos que você tem uma variável chamada "tensao_atual" que contém o valor de tensão
    # Substitua este trecho pela leitura real da porta serial do Arduino
    import random
    tensao_atual = random.randrange(2000, 5000)  # Supondo valores entre 0 e 5 volts
    return tensao_atual