#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: 'f4stB4nd1t'
#GitHub: 'f4stB4nd1t'

import argparse
import random
import time
from colorama import Fore, init

def luhn_algorithm(card):
    if type(card) is not int:
        exit()
        
    cont = 1
    reversed_digits = list()
    normal_digits = list()
    for digit in reversed(str(card)):
        if cont % 2 == 0:
            reversed_digits.append(int(digit))
            cont = 1
        else:
            cont = 2
            normal_digits.append(int(digit))
            
    cont_reversed = 0
    for number in reversed_digits:
        number = number * 2
        if len(str(number)) == 2:
            num1 = str(number)[0]
            num2 = str(number)[1]
            number = int(num1) + int(num2)
            cont_reversed += number
        else:
            cont_reversed += number

    cont_normal = 0
    for number in normal_digits:
        cont_normal += number
    luhn = int(cont_normal) + int(cont_reversed)
    if luhn % 10 == 0:
        return str(card)
    
    else:
        return int(card)

def Generador(bin_base):
    nums = [1,2,3,4,5,6,7,8,9,0]
    digits = len(str(bin_base))
    for _ in range(digits, 16):
        bin_base = str(bin_base) + str(random.choice(nums))
    
    return int(bin_base)

def Guardar_Tarjetas_Codigos_Fechas(cantidad):
    tarjetas = list()
    tarjetas_no_validas = list()
    signal = True
    while signal:
        tarjeta = luhn_algorithm(Generador(args.bin))
        if type(tarjeta) is str:
            tarjetas.append(tarjeta)
            if len(tarjetas) == cantidad:
                signal = False
        else:
            tarjetas_no_validas.append(tarjeta)
            
    Generador_Codigo(tarjetas)
    
    for card, code in zip(tarjetas, codigos):
        fecha = Generar_Fecha()
        print(f'[+] Tarjeta: {card} - Codigo: {code} - Fecha: {fecha}')
    
def Generador_Codigo(tarjetas=list):
    global codigos; codigos = list()
    for tarjeta in tarjetas:
        code = tarjeta[4] + tarjeta[9] + tarjeta[14]
        codigos.append(code)
        
def Generar_Fecha():
    years = ['2022', '2023', '2024', '2025']
    months = ['01', '02', '03', '04', '05', '06' , '07', '08', '09', '10', '11', '12']
    fecha = '{}/{}'.format(random.choice(months), random.choice(years))
    
    return fecha
    
        
def Setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('bin', metavar='bin', help='Bin base para generar tarjetas', type=int)
    parser.add_argument('cantidad', metavar='cantidad', help='Cantidad de tarjetas', type=int)
    global args; args = parser.parse_args()
    
    bins_no_validos = ['1', '2', '6', '7', '8', '9', '0']
    if str(args.bin)[0] in bins_no_validos:
        time.sleep(1)
        print(f'{Fore.RED}[-] Introduce un bin valido')
        exit()

if __name__ == '__main__':
    try:
        init()
        Setup()
        Guardar_Tarjetas_Codigos_Fechas(args.cantidad)
    
    except KeyboardInterrupt:
        print('[-] Programa finalizado')
        exit()