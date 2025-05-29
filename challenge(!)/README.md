
## Juego del Gato y el Ratón 🐁🧀🐈
Este es un juego de persecución entre un gato y un ratón, implementado en Python.
El usuario puede elegir representar al gato o al ratón. Como se trata de una competencia entre máquina y máquina, se implementa el algoritmo Minimax para que el gato (jugador MAX) persiga al ratón, y el ratón (jugador MIN) huya e intente comer el queso.

## Objetivos del juego
-Que el ratón escape y/o coma todos los quesos.
-Que el gato atrape al ratón.

## Características
- El tablero tiene obstáculos y quesos (en posiciones fijas).
- El ratón empieza moviéndose de forma aleatoria (utilizando random, también puede moverse en diagonales).
- Después de 4 turnos, el ratón empieza a usar Minimax.
- El gato usa Minimax desde el principio (y puede saltar los obstáculos).
- El juego termina si:
- El gato atrapa al ratón.
- El ratón se come todos los quesos.
- Se alcanza un empate por cantidad máxima de movimientos.
- Sistema de turnos limitados.
- Código estructurado en módulos para mayor claridad y escalabilidad.

## Cosas que salieron bien
-La creación del tablero y hacerlo atractivo visualmente.
-El posicionamiento de los elementos dentro del tablero y las condiciones para validar los movimientos.

## Mayores desafíos
- La implementación correcta del algoritmo Minimax, ya que me costó pasar de la teoría a la práctica.
- Conectar todo correctamente al modularizar sin romper funcionalidades.

## Mejores partes
- Incorporación de emojis para mejorar el aspecto visual.
- Retroalimentación de conocimientos adquiridos previamente.
-Entendimiento del algoritmo Minimax.

