#-*- coding: utf-8 -*-
from serial_input import serialinput
import time

def tensao_para_hr(ponto_alto = 4500, ponto_baixo = 2500, max_leituras = 100):
    picos = 0
    ciclos_completos = 0
    tempo_inicial = time.time()  # Registra o tempo inicial

    for leituras in range(max_leituras):
        tensao_atual = serialinput()  # Supõe que a função serialinput() fornece o valor de tensão atual

        if tensao_atual >= ponto_alto:
            picos += 1
        elif tensao_atual <= ponto_baixo and picos > 0:
            ciclos_completos += 1
            picos = 0
        time.sleep(0.05)#sleep considerando frequencia maxima de 220 bpm (picos e vales a cada 136 milisegundos tempo de hardware a considerar)

    tempo_final = time.time()  # Registra o tempo final
    tempo_total_segundos = tempo_final - tempo_inicial  # Calcula o tempo total em segundos

    # Calcula a frequência cardíaca em bpm
    batidas = (ciclos_completos/2)
    tempo_total_minutos = (tempo_total_segundos / 60)
    frequencia_cardiaca = (batidas / tempo_total_minutos)   # Converte para bpm
    if frequencia_cardiaca < 40:
        return "ERRO: MEDIDA INFERIOR AO MINIMO"
    elif frequencia_cardiaca > 220:
        return "ERRO: MEDIDA SUPERIOR AO MAXIMO"
    else:
        return frequencia_cardiaca


# Exemplo de uso:
# picos e vales são a sistólica e didiastólica 

# ponto_alto = 4300  # Valor pré-estabelecido para ponto alto ()
# ponto_baixo = 3000  # Valor pré-estabelecido para ponto baixo ()
# max_leituras = 50  # Número máximo de leituras da tensão


# frequencia_cardiaca = tensao_para_hr(ponto_alto, ponto_baixo, max_leituras)
# print("Frequência cardíaca:", frequencia_cardiaca, "bpm", )