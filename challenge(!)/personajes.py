from tablero import crear_tablero,mostrar_tablero
#funcion para posicionar y mostrar todos los personajes y elemementos
# en mi tablero(empiezan en posiciones fijas)
def colocar_personajes(tablero):
    pos_raton = (0,0)
    pos_gato = (7,7)
    pos_queso = [(2,2),(5,6)]
    pos_trampa = [(2,1), (4,3), (5,3),(2,6),(2,7)]

    tablero[pos_raton[0]][pos_raton[1]] = "🐁"
    tablero[pos_gato[0]][pos_gato[1]] = "🐈"
    for pos in pos_queso:
     fila, columna = pos
     tablero[fila][columna] = "🧀"
    for pos in pos_trampa:
     fila, columna = pos
     tablero[fila][columna] = "🧱"

    
    

    return pos_raton, pos_gato, pos_queso, pos_trampa

