#-*- coding: utf-8 -*-
from flask import Flask, render_template
import random
from hrserial import hrcapture
app = Flask(__name__)

# Configuração da porta serial do Arduino 

#SERIAL_PORT = '/dev/ttyACM0'  # ou 'COMX' no Windows
#BAUD_RATE = 9600

# Inicializa a comunicação serial com o Arduino
# arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Rota para exibir a página web com o valor da frequência cardíaca
@app.route('/')
def index():
 
    #heart_rate = hrcapture()
    heart_rate = random.randrange(1, 301)
    return render_template('index.html', heart_rate=heart_rate)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
