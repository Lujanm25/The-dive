#funcion para crear tablero
def crear_tablero():
    return[["⬜" for _ in range(8)] for _ in range(8)]

#funcion para mostrar el tablero 
def mostrar_tablero(tablero):
    for fila in tablero:
        print("".join(fila))
    print()

tablero = crear_tablero()





