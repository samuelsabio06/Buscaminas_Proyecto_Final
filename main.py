'''
Módulo con la funcion principal del juego
'''
import threading
from funciones import crear_tablero, mostrar_tablero, crear_minas, calcular_fondo, jugar
from extras import timer_thread

def main():
    '''
    Función principal del juego.
    Solicita al usuario las dimensiones, dificultad y duración, inicia la cuenta regresiva y arranca la partida.
    '''
    global tiempo_finalizado
    try:
        filas = int(input("Introduce el número de filas: "))
        columnas = int(input("Introduce el número de columnas: "))
        dificultad = float(input("Ingrese la dificultad del juego \n1. Fácil \n2. Heroica \n3. Legendaria\n"))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    tablero = crear_tablero(filas, columnas)
    mostrar_tablero(tablero)

    duracion = len(tablero)*len(tablero[0])*8  # Duración en segundos basada en el tamaño del tablero
    print(f"La duración de la partida será de {duracion} segundos.")
    # Iniciar el hilo del timer (daemon para que se detenga al finalizar el programa)
    timer = threading.Thread(target=timer_thread, args=(duracion,), daemon=True)
    timer.start()

    minas = crear_minas(filas, columnas, dificultad)
    fondo = calcular_fondo(minas)
    jugar(tablero, fondo, minas, dificultad)

if __name__ == "__main__":
    main()
