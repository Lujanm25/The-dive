from tablero import crear_tablero,mostrar_tablero
from personajes import colocar_personajes
from movimientos import mover_aleatorio_raton,mover_gato
from minimax import minimax,evaluar,mover_raton_minimax,mover_gato_minimax

#con un bucle pregunto al usuario si quiere representar al gato o al raton y valido
while True:
    personaje = int(input("Ingresa que personaje queres representar\n 1-Raton 🐁\n 2-Gato 🐈 \n "))
    if personaje in (1,2):
        break
    else:
        print("Opcion invalida. Elija la opcion 1 o 2!")

#creo la funcion principal para mi juego
def iniciar_juego():
    #genero un nuevo tablero
    tablero = crear_tablero()

    #coloco a los elementos de mi tablero en sus posiciones inicales
    pos_raton, pos_gato, pos_queso, pos_trampa = colocar_personajes(tablero)

    turnos = 20
    turnos_jugados_raton = 0 

    while turnos > 0:
        mostrar_tablero(tablero)
        print(f"Te quedan {turnos} restantes")

        print("\n Turno del Raton 🐁. Presione Enter para mover...  ")
        input()
        
        if turnos_jugados_raton <= 4:
         nueva_pos_raton = mover_aleatorio_raton(tablero,pos_raton,pos_gato,pos_queso,pos_trampa)
        else:
            nueva_pos_raton = mover_raton_minimax(tablero,pos_raton,pos_gato,pos_queso,pos_trampa,profundidad=5)

        pos_raton = nueva_pos_raton
        turnos_jugados_raton += 1
        turnos -= 1 # se resta un turno

        if pos_raton in pos_queso: #si el raton esta sobre el queso se elimina el queso
            pos_queso.remove(pos_raton)
        
        #actualizo el tablero con las nuevas posiciones
        tablero=crear_tablero()
        tablero[pos_raton[0]][pos_raton[1]] = "🐁"
        tablero[pos_gato[0]][pos_gato[1]]= "🐈"
        for queso in pos_queso:
            tablero[queso[0]][queso[1]]= "🧀"
        for trampa in pos_trampa:
            tablero[trampa[0]][trampa[1]]="🧱"


        if len(pos_queso) == 0:
            mostrar_tablero(tablero)

            if personaje == 1:
                print("El raton 🐁 comio todos el queso🧀🎉 GANASTE!! ")

            else:
                print("El raton logro comer todos el queso🧀 .PERDISTE!!😿")
            return 
            
        if pos_gato == pos_raton:
            mostrar_tablero(tablero)

            if personaje == 2:
                print("El gato 🐈 atrapo al raton!! GANASTE 😼!")
                      
            else:
                print("El gato atrapo al raton 🐁, PERDISTE!!")
            return 


        

        if turnos == 0:
             mostrar_tablero(tablero)
             print("\n Empate! El raton logro escapar,pero, no comio el queso!🧀")
             return 

        mostrar_tablero(tablero)
        print(f"Turnos restantes {turnos}")
        print("\n Turno del Gato 🐈 . Presione Enter para mover...")
        input()

        pos_gato = mover_gato_minimax(tablero,pos_raton,pos_gato,pos_queso,pos_trampa,profundidad=5)

        

while True:
       iniciar_juego()
       respuesta= input("Queres jugar otra vez? (s/n):").strip().lower()
       if respuesta != "s":
        print("Gracias por jugar!")
        break
       

