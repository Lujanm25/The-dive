#  Generador y Solucionador de Laberintos
## Descripción
En este proyecto creé un programa en C++ que genera laberintos aleatorios y luego los resuelve automáticamente. La idea era construir laberintos que siempre tengan un camino posible desde la entrada hasta la salida.

## Cómo funciona
- Generación del laberinto: El laberinto se genera como una matriz donde cada celda puede ser muro o espacio vacío,  con un 40% de probabilidad de que sea espacio. La entrada está fija en la esquina superior izquierda y la   salida en la esquina inferior derecha.

- Backtracking: Usé backtracking para explorar el laberinto y asegurarme de que haya al menos un camino desde    la  entrada a la salida.

- BFS (Breadth First Search): Después aplico BFS para encontrar la ruta más corta entre entrada y salida. Mientras BFS encuentra el camino, el programa muestra la búsqueda de forma animada en la consola.

- Visualización: El laberinto y la solución se muestran en la consola usando caracteres ASCII.

## Lo que aprendí
- Cómo combinar generación aleatoria con validación para crear laberintos solucionables.

- La diferencia práctica entre backtracking (exploración) y BFS (búsqueda óptima).

- La importancia de estructuras de datos como colas y matrices dinámicas.

- Uso  de punteros: En vez de vectores, manejé memoria dinámica con punteros para crear las matrices del laberinto y controlar todo con más detalle. Esto me ayudó a entender mejor cómo funciona la memoria en C++ y a manejar recursos manualmente.

- Que mostrar el progreso con animaciones ayuda a entender mejor cómo funciona el algoritmo.

## Cómo ejecutar el programa
Compilá el archivo .cpp con un compilador de C++ (por ejemplo, usando g++):

Copiar
Editar
g++ -o laberinto laberinto.cpp
Ejecutá el programa generado:

bash
Copiar
Editar
./laberinto
El programa te va a pedir ingresar la cantidad de filas y columnas para el laberinto. Ingresás los números y ahí se genera y resuelve el laberinto mostrando todo en consola.

## Posibles mejoras
- Mejorar la heurística para la generación, para que los laberintos sean más variados y desafiantes.

- Implementar otros algoritmos de búsqueda como A* para comparar eficiencia.

- Optimizar la visualización para que sea más rápida y clara.