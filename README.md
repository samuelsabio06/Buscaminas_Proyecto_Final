# Buscaminas: Proyecto Final
Demo del juego buscaminas en terminal usando python.
[![asciicast](https://asciinema.org/a/706504.svg)](https://asciinema.org/a/706504)

## Tabla de contenidos
  - [Introducción](#introducción)
  - [Abordaje del problema](#abordaje-del-problema)
  - [Solución del problema](#solución-del-problema)
  - [Función foco](#función-foco)
  - [Instalacion del programa](#instalación-del-programa)
  - [Conclusiones](#conclusiones)

## Introducción
El **buscaminas** ha sido una fuente de entretenimiento que ha marcado varias generaciones. En este repositorio se dará a conocer el proceso y desarrollo de una versión funcional que sea fiel a las reglas basicas del buscaminas original. El funcionamiento del codigo esta sustentado en algoritmos que permiten funcionalidades como la creacion de un tablero, distribución de minas, o gestión de interacciones del jugador.
## Abordaje del problema
El problema consiste en crear un código que emule un **buscaminas**, y que además cumpla con las siguientes condiciones:
  - Código original
  - Aborde temas aprendidos en clase
  - Tenga 3 niveles de dificultad
  - Se dibuje la matriz en la consola
  - Se interactue por medio de coordenadas
    
Adicionalmente se nos permitia que el proyecto llevara ciertos **extras**, como la cuenta regresiva y el conteo de puntos.
## Solución del problema
A grandes rasgos, el código se realizo de manera que se pueda jugar el clásico buscaminas por medio de la consola. En primer lugar, se usaron librerias como ```random```  que hizo posible generar numeros aleatorios para llenar el campo de juego. Por otro lado fue indispensable el uso de ciclos ```for``` para la creación de funciones dedicadas diferentes aspectos del juego, como crear el tablero, crear minas y o revelar las fronteras; y una funcion principal para iniciar el juego.

- Funcionamiento general del código:
  ```mermaid
  flowchart TD


  id1([Inicio]) ==> B[Solicitar datos: Número de filas, columnas y dificultad]
  B==> C[Solicitar coordenada]
  C ==> D{¿Poner bandera?}
  D ==>|si|f[Colocar bandera] ==>C 
  D ==> |no|E[Revelar casilla]
  E ==> G{¿Es una mina?}
  G ==> |si|H([Fin])
  G ==> |no|I{¿Quedan casillas sin minar?}
  I ==> |no|H
  I ==> |si|C
  
  style id1 stroke:#0F0,stroke-width:4px
  style H stroke:#0F0,stroke-width:4px
  style D stroke:#00f,stroke-width:4px
  style G stroke:#00f,stroke-width:4px
  style I stroke:#00f,stroke-width:4px

  ```

## Función foco

Una de las funciones principales de este código es la función que se encarga de revelar las fronteras del tablero, es decir, al revelar una casilla con un cero (no tiene minas alrededor), automaticamente se van a seguir liberando las casillas que también contengan un cero.



## Instalación del programa
Requires Python 3.x or later.

```sh
git clone https://github.com/samuelsabio06/Buscaminas_Proyecto_Final.git
cd Buscaminas_Proyecto_Final
python main.py
```

## Proximos pasos (Mejoras)
  - Agregar una interfaz
  - Agregar animaciones de bandera y bomba
  - Dejar de usar la consola para pedir coordenadas y cambiar a un sistema donde se use el mouse por medio de la interfaz
  - Revelar un area grande en el primer movimiento






