"""Version de python 3.11.4"""
#Librerias#
from automata import Agente , MODELO, REGLAS
import re
import time

#Función para imprimir la validación de una entrada
def val( estado, accion, tiempo):
    time.sleep(tiempo)
    print(estado)
    time.sleep(tiempo)
    print(estado)
    time.sleep(tiempo)
    print(estado)
    print(accion)

"""Validar una cadena de acuerdo con un patron"""
def regex(cadena, patron):
    #Hacer match con el valor que se pasa de la cadena
    resultado = re.match(patron, cadena)
    #Retorna True si coincide, de lo contrario retorna false
    return resultado is not None
#Regex para las variables c* = c[1-3]$

#Funcion del agente#
def agente():
    #Inicialización del agente
    expendedora = Agente(MODELO, REGLAS, 'sin-dinero','pedir-dinero', c1 = 17, c2 = 20, c3 = 19)
    #Copio los valores de los codigos a una lista y se la asigno a precios
    precios = list(expendedora.codigos.values())
    saldo = 0
    percepcion = 'pedir-dinero'
    #Flujo del Agente
    while percepcion:
        accion = expendedora.actuar(percepcion)
        if(accion == 'pedir-dinero'): #En caso de que solicite no haya insertado la 'dinero' lo solicita
            print("-- Máquina Expendedora --")
            print("Saldo: $",saldo)
            dinero = input( "\tInserte dinero\nVálido dinero de 1, 2, 5 y 10\nBilletes de 20, 50 y 100\n|: ")
            #Convertir el valor a entero
            dinero = int(dinero)
            if(dinero == 1 or dinero == 2 or dinero == 5 or dinero == 10 or 
                dinero == 20 or dinero == 50 or dinero == 100):
                saldo = dinero + saldo
                percepcion = 'dinero'
            else:
                print("No válido")
                percepcion = 'pedir-dinero'
        elif(accion == 'pedir-codigo'): #Cuando solicite pedir codigo imprimira las opciones disponibles
            print("Saldo: $",saldo)
            
            print("Ingrese el código")
            print("Gansito   => c1 $17")
            print("Coca-Cola => c2 $20")
            print("Pingüinos => c3 $19")

            decision = input("|: ")

            retorno = regex(decision, "c[1-3]$")
            if(retorno):
                if(decision == 'c1' and saldo >= precios[0]):
                    print("Cambio a regresar: $",saldo-precios[0])
                    percepcion = decision
                    saldo = 0
                elif(decision == 'c2' and saldo >= precios[1]):
                    print("Cambio a regresar: $",saldo-precios[1])
                    percepcion = decision
                    saldo = 0
                elif(decision == 'c3' and saldo >= precios[2]):
                    print("Cambio a regresar: $",saldo-precios[2])
                    percepcion = decision
                    saldo = 0
                else:
                    print("Dinero insuficiente")
                    percepcion = 'pedir-dinero'
            else:#Regresar dinero en caso de error
                print("Codigo insertado no válido")
                percepcion = 'pedir-dinero'
        elif(accion == 'esperar'): #Tiempo de espera de la maquina en la entrega del producto
            val("Entregando", "Entregado", 1)
            percepcion = 'servida'

#Llamado del agente
agente()

##Diccionario##
#Accion = percepcion actual del automata
#Percepcion  = Valor siguiente que va a recibir el automata
#Dinero = valor que recibe la "maquina"
#Saldo = saldo que contiene la maquina