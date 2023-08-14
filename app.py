#-*- coding: utf-8 -*-
from flask import Flask, render_template
import random
from hr_calc import tensao_para_hr

app = Flask(__name__)

# Rota para exibir a página web com o valor da frequência cardíaca
@app.route('/')
def index():
 
    heart_rate = tensao_para_hr()
    
    #heart_rate = random.randrange(40, 220)
    
    return render_template('index.html', heart_rate=heart_rate)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
