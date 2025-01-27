# Buscaminas_Proyecto_Final
---
Avance del proyecto

## 1. Diagrama preliminar: 
¿Como poner la condicion para ganar? Solo se aclaro la manera en que finaliza el juego si se encuentra una mina, es decir si se pierde.

```mermaid

flowchart TD
  A([Inicio]) --> B[Solicitarle los datos al usuario: Filas, columnas y dificultad]
  B--> C[Se genera la matriz y las minas]
  C--> D[Solicitar coordenada]
  D--> E{¿Es la primera coordenada?}
  E--> |si|F{¿Es una mina?}
  F--> |si|G[Elimina la mina y ajusta la matriz]
  
  E--> |no|H{¿Poner bandera?}
  
  G--> D 
  F--> |no|D
  
  H--> |no|I[Revelar la casilla]
  H--> |si|J[Poner bandera]
  J--> D
  I--> L{¿Es una mina?} 
  L--> |si|O([Fin])
  L--> |no|D
```




