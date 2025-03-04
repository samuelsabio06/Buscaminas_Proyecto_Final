'''
Módulo con extras para el juego

Este módulo contiene funciones que mejoran la experiencia 
y jugabilidad del buscaminas
'''

import os
import time
import threading

def calcular_puntuación(tablero, dificultad):
    '''
    Define la puntuación del juego basado en el tablero y dificultad.

    Args:
    tablero (list): El tablero de juego con las celdas reveladas.
    dificultad (str): Dificultad del juego actual

    Retorno:
    puntuacion (int): Puntuación obtenida

    '''

    filas, columnas = len(tablero), len(tablero[0])
    puntuacion = 0
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] not in ('*', 'X'):
                puntuacion += 1
            if tablero[i][j] == 'X':
                puntuacion -= 5
    puntuacion *= dificultad
    return puntuacion

def limpiar_consola():
    '''
    Limpia el contenido que se imprime en la consola, 
    para una mejor visualización del juego

    Args:
    None
    '''
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y otros sistemas operativos
        os.system('clear')

def timer_thread(duracion):
    '''
    Función que muestra la cuenta regresiva del tiempo restante.
    
    Args:
        duracion (int): Tiempo total de la partida en segundos.
    '''
    global tiempo_finalizado
    for i in range(duracion, 0, -5):
        if i == duracion:
            time.sleep(1)
            print(f"{'Tiempo restante: ':>35}{duracion} segundos", end="\r")
        else:
            print(f"{'Tiempo restante: ':>35}{i} segundos", end="\r")
            time.sleep(5)
    tiempo_finalizado = True
    print(f"{'Tiempo restante: ':>35} 0 segundos")
