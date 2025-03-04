'''
Módulo de logica del buscaminas.

Contiene las funciones necesarias para implementar la lógica del juego
'''

import random
from extras import calcular_puntuación, limpiar_consola, timer_thread

tiempo_finalizado = False

def crear_tablero(filas, columnas):
    '''
    Crea un tablero de juego con las dimensiones especificadas.

    Args:
    filas (int): Número de filas del tablero.
    columnas (int): Numero de columnas del tablero.

    Retorno:
    tablero (list): Matriz que representa el tablero de buscaminas
    '''
    tablero = [['*' for _ in range(columnas)] for _ in range(filas)]
    return tablero


def mostrar_tablero(tablero):
    '''
    Muestra el tablero de juego en la consola.

    Args:
    tablero (list): El tablero de juego con las celdas reveladas.

    Retorno:
    None
    '''
    filas, columnas = len(tablero), len(tablero[0])
    espacio = 3  # Ancho de cada celda
    print("   ", end="")  # Encabezado de columnas
    for u in range(columnas):
        print(f"{u:>{espacio}}", end="")
    print()
    for i in range(filas):
        print(f"{i:>{2}}", end=" ")  # Índice de fila
        for j in range(columnas):
            print(f"{tablero[i][j]:>{espacio}}", end="")
        print()


def crear_minas(filas, columnas, dificultad):
    '''
    Crea el tablero de minas según la dificultad especificada.

    Args:
    filas (int): Número de filas del tablero.
    columnas (int): Numero de columnas del tablero.
    difucltad (float): Dificultad que determina el numero de minas.

    Retorno:
    minas (list): Matriz que representa el tablero con las minas

    '''
    match dificultad:
        case 1.0:
            dificultad = 0.10
        case 2.0:
            dificultad = 0.15
        case 3.0:
            dificultad = 0.25

    minas = [[1 if random.random() < dificultad else 0 
          for _ in range(columnas)] 
         for _ in range(filas)]
    return minas


def calcular_fondo(minas):
    '''
    Calcula el fondo del tablero según la posición y número de minas adyacentes.

    Args:
    minas (list): Matriz que representa el tablero con las minas

    Retorno:
    fondo (list): El tablero con las posiciones de las minas y numeros.
    '''
    filas, columnas = len(minas), len(minas[0])
    fondo = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            if minas[i][j] == 1:
                fondo[i][j] = 'X'
            else:
                for k in range(max(0, i-1), min(filas, i+2)):
                    for l in range(max(0, j-1), min(columnas, j+2)):
                        fondo[i][j] += minas[k][l]
    return fondo


def revelar_ceros(tablero, fondo, fila, columna, visitados=None):
    """
    Revela todas las celdas conectadas que tengan 0 y, además, las adyacentes
    con números. Se utiliza recursividad para recorrer las celdas adyacentes.

    Args:
    tablero (list): El tablero de juego con las celdas reveladas.
    fondo (list): El tablero con las posiciones de las minas y numeros.
    fila (int): La fila de la celda que se seleccionó.
    columna(int): La columa de la celda que s eselccionó.

    Retorno:
    None
    """
    if visitados is None:
        visitados = []
    if fila < 0 or fila >= len(fondo) or columna < 0 or columna >= len(fondo[0]):
        return
    if (fila, columna) in visitados:
        return
    visitados.append((fila, columna))
    tablero[fila][columna] = str(fondo[fila][columna])
    if fondo[fila][columna] == 0:
        for i in range(max(0, fila-1), min(len(fondo), fila+2)):
            for j in range(max(0, columna-1), min(len(fondo[0]), columna+2)):
                if (i, j) not in visitados:
                    revelar_ceros(tablero, fondo, i, j, visitados)


def jugar(tablero, fondo, minas, dificultad):
    '''
    Función principal para jugar al buscaminas.
    Verifica si el jugador pisa una mina o revela una celda vacía. 
    Determina si el tiempo de juego se agota o el jugador gana el juego.

    Args:
    tablero (list): El tablero de juego con las celdas reveladas.
    fondo (list): El tablero con las posiciones de las minas y numeros.
    minas (list): Coordenadas de las minas en el tablero.
    dificultad (str): Dificultad del juego actual

    Retorno:
    None
    '''
    global tiempo_finalizado
    primera_vez = True
    while True:
        # Si el tiempo se agotó, se finaliza el juego
        if tiempo_finalizado:
            print("\n¡Tiempo agotado! Fin del juego.")
            puntuacion = calcular_puntuación(tablero, dificultad)
            print("Puntuación obtenida en esta partida:", int(puntuacion))
            break

        try:
            fila = int(input("Introduce la fila:\n"))
            columna = int(input("Introduce la columna:\n"))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero[0]):
            print("Coordenadas fuera de los límites del tablero.")
            continue

        respuesta = input("¿Colocar una bandera en esta coordenada? (sí/no):\n"
            ).strip().lower()
        if respuesta in ('sí', 'si'):
            limpiar_consola()
            tablero[fila][columna] = '?'
            mostrar_tablero(tablero)
            print("Se ha colocado una bandera. Continúa jugando.")
            continue

        if fondo[fila][columna] == 'X' and not primera_vez:
            print("¡HAS ENCONTRADO UNA MINA! Fin del juego.")
            tablero[fila][columna] = 'X'
            mostrar_tablero(tablero)
            puntuacion = calcular_puntuación(tablero, dificultad)
            print("Puntuación obtenida en esta partida:", int(puntuacion))
            break
        elif fondo[fila][columna] == 'X' and primera_vez:
            limpiar_consola()
            # Primera jugada: se evita que el jugador pierda si escoge una mina
            for k in range(max(0, fila-1), min(len(minas), fila+2)):
                for l in range(max(0, columna-1), min(len(minas[0]), columna+2)):
                    if fondo[k][l] != 'X':
                        fondo[k][l] -= 1
            fondo[fila][columna] = 0  # Se elimina la mina de la celda inicial
            revelar_ceros(tablero, fondo, fila, columna)
            mostrar_tablero(tablero)
            primera_vez = False
            print("Sigue jugando.")
        else:
            limpiar_consola()
            if fondo[fila][columna] == 0:
                revelar_ceros(tablero, fondo, fila, columna)
            else:
                tablero[fila][columna] = str(fondo[fila][columna])
            mostrar_tablero(tablero)
            print("Sigue jugando.")

        # Verificar si el jugador ha ganado
        celdas_descubiertas = sum(1 for row in tablero 
            for cell in row if cell not in ('*', 'X', '?'))
        celdas_no_minas = sum(1 for row in fondo for cell in row if cell != 'X')
        if celdas_descubiertas == celdas_no_minas:
            print("¡Has ganado el juego!")
            puntuacion = calcular_puntuación(tablero, dificultad)
            print("Puntuación obtenida en esta partida:", int(puntuacion))
            break

        primera_vez = False


