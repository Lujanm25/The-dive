import random #importo ramdon para poder darle movimientos aleatorios a mi raton

def mover_aleatorio_raton(tablero,pos_raton,pos_trampa,pos_gato,pos_queso):
    movimientos = []
    direcciones = [
        (-1,0), #arriba
        (1,0), # abajo
        (0,1), #derecha
        (0, -1), #izquierda
        (-1,1), #arriba derecha
        (-1,-1), #arriba izquierda
        (1,1), # abajo derecha
        (1,-1) #abajo izquierda
    ]

    for m in direcciones: #por cada movimiento posible dentro de mis direcciones
        fila_nueva = pos_raton[0] + m[0] #suma el movimineto a la fila actual para saber donde va ir el 🐁
        columna_nueva = pos_raton[1] + m[1] #lo mismo pero con las columnas

        #veridico que la nueva posicion este dentro de mi tablero 
        if 0 <= fila_nueva < len(tablero) and 0 <= columna_nueva < len(tablero[0]):

            #verifico que no haya trampas en esa posicion
            if (fila_nueva,columna_nueva) not in pos_trampa:

                #si es valido y no hay trampas lo agrego a la lista
                movimientos.append((fila_nueva,columna_nueva))

    if movimientos:
        return random.choice(movimientos)  # Elijo solo un movimiento al azar
    return pos_raton


def posibles_movimientos_raton(tablero, pos_raton, pos_trampa,pos_gato,pos_queso):
    movimientos = []
    direcciones = [
        (-1,0), # arriba
        (1,0),  # abajo
        (0,1),  # derecha
        (0,-1), # izquierda
        (-1,1), # arriba derecha
        (-1,-1),# arriba izquierda
        (1,1),  # abajo derecha
        (1,-1)  # abajo izquierda
    ]

    for m in direcciones:
        fila_nueva = pos_raton[0] + m[0]
        columna_nueva = pos_raton[1] + m[1]

        # verifico que la nueva posición esté dentro del tablero
        if 0 <= fila_nueva < len(tablero) and 0 <= columna_nueva < len(tablero[0]):
            # verifico que no haya trampas en esa posición
            if (fila_nueva, columna_nueva) not in pos_trampa:
                movimientos.append((fila_nueva, columna_nueva))
    return movimientos



def mover_gato(tablero,pos_gato,pos_trampa,pos_queso):
    movimientos = []
    direcciones= [
        (-1,0), #arriba
        (1,0), #abajo
        (0,1), #derecha
        (0,-1) #izquierda
    ]

    for m in direcciones:
        fila_nueva = pos_gato[0] + m[0]
        columna_nueva = pos_gato[1] + m[1]

        if 0 <= fila_nueva < len(tablero) and 0 <= columna_nueva < len(tablero[0]):
            movimientos.append((fila_nueva,columna_nueva))
          
    return movimientos
