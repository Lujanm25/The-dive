#importo decopy para poder copiar el estado del juego sin modificar el original
from copy import deepcopy
from tablero import crear_tablero,mostrar_tablero
from movimientos import mover_aleatorio_raton, posibles_movimientos_raton,mover_gato

#empiezo a implementar la logica del minimax
#defino la funcion con todos los parametros necesarios
def minimax(tablero,pos_raton,pos_gato,pos_queso,pos_trampa,profundidad,turno_gato,alfa=float("-inf"), beta=float("inf")):

    # si la profundidad llega a 0 o el gato esta en la misma posicion que el raton o ya no hay quesos
    if profundidad == 0 or pos_raton == pos_gato or len(pos_queso) == 0:

        #devuelvo la evaluacion del estado y ningun movimiento 
        return evaluar(tablero,pos_raton,pos_gato,pos_queso), None
    
    #al gato es el max, va buscar maximizar su puntuacion
    if turno_gato:
        mejor_valor = float("-inf")  # ← el gato es max, así que inicia con -infinito
        mejor_movimiento = None

        #obtengo los posibles movimientos del gato
        movimientos=mover_gato(tablero,pos_gato,pos_trampa,pos_queso)
        
        for movimiento in movimientos:
            nueva_pos_gato = movimiento #simulo mover al gato en esa posicion

            #llamo recursivamente a minimax para el siguiente movimiento(turno del raton)
            valor, _ = minimax(deepcopy(tablero),pos_raton,nueva_pos_gato,    #a partir de este false es turno del raton
                               deepcopy(pos_queso), pos_trampa, profundidad-1,False,alfa,beta)
            
            #actualizo el valor y movimiento si encontre uno mejor
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = nueva_pos_gato
                alfa = max(beta,valor) #actualizo beta
                if beta <= alfa:
                    break # realizo la poda porque ya no vale la pena seguir evaluando

        return mejor_valor, mejor_movimiento
    
    #turno del raton(min)
    else:
        mejor_valor = float("inf")
        mejor_movimiento = None
        movimientos = posibles_movimientos_raton(tablero,pos_raton,pos_gato,pos_queso,pos_trampa)
        for movimiento in movimientos:
            nueva_pos_raton = movimiento
            nuevos_quesos = deepcopy(pos_queso) #copio la posicion de los quesos

            #sacamos el queso si esta en la posicion nueva del raton
            if nueva_pos_raton in nuevos_quesos:
                nuevos_quesos.remove(nueva_pos_raton)

                return -1000, nueva_pos_raton

            valor, _ = minimax(deepcopy(tablero),nueva_pos_raton,
                    pos_gato,nuevos_quesos,pos_trampa,
                    profundidad -1, True,alfa,beta)
                
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = nueva_pos_raton
            beta=min(alfa,valor) #actualizo alfa
            if beta <= alfa:
                break #poda
        return mejor_valor,mejor_movimiento

#funcion para evaluar 
def evaluar(tablero,pos_raton,pos_gato,pos_queso):
    if pos_raton == pos_gato:
        return 1000 #gano el gato
    
    if pos_raton in pos_queso:
        return -1000 #compensa al raton por comerse un queso
    
    if len(pos_queso) == 0:
        return -900 #todos los quesos fueron comidos
    
    #calculo la distancia minima entre el raton y queso mas cercano usando la distancia eucladiana(por las diagonales)
    queso= pos_queso[0]
    distancia_queso = ((pos_raton[0] - queso[0])**2  + (pos_raton[1]- queso[1])**2) **0.5

    #calculo la distancia del gato al raton usando la distancia manhattan(en cruz o linea recta)
    distancia_gato =abs(pos_raton[0] - pos_gato[0]) + abs(pos_raton[1] - pos_gato[1])

    #penalizo si el gato esta cerca
    peligro = max(0,3 - distancia_gato) * 50 #mientras mas cerca este el gato,peor

    return distancia_queso * 5 + peligro #premia acercarse al queso y penaliza acercarse al gato  

#funcion para mover al raton con minimax
def mover_raton_minimax(tablero,pos_raton,pos_gato,pos_queso,pos_trampa,profundidad):
    _, mejor_movimiento= minimax(tablero,pos_raton,pos_gato,pos_queso,pos_trampa,profundidad, False) #turno del raton
    return mejor_movimiento if mejor_movimiento else pos_raton # devuelve el mejor movimiento o se queda en su lugar

def mover_gato_minimax(tablero,pos_raton,pos_gato,pos_queso,pos_trampa,profundidad):
    _, mejor_movimiento= minimax(tablero,pos_raton,pos_gato,pos_queso,pos_trampa,profundidad,True)
    return mejor_movimiento if mejor_movimiento else pos_gato

