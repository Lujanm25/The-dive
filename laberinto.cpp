#include <iostream>
#include <cstdlib>
#include <ctime> //incluyo todas las librerias que necesito
#include <queue>
#include <utility>
#include <windows.h> 

using namespace std;

void pausa(int ms = 100) {
    Sleep(ms); } // una mini pausa para mostrar el laberinto


void pausaBFS() { // otra pausa para ver de forma "animada" como actua el BFS
    Sleep(400);
}

void mostrarLaberintoAnimado(char** matrizLaberinto, int filas, int columnas) {
    system("cls"); //limpio la pantalla
    for (int i = 0; i < filas; i++) { //recorro toda la matriz
        for (int j = 0; j < columnas; j++) {
            char c = matrizLaberinto[i][j]; //dependiendo del valor de mi variable temporal elijo que caracter mostrar
            if (c == 'S') cout << "S ";
            else if (c == 'E') cout << "E ";
            else if (c == '+') cout << "+ ";
            else if (c == '.') cout << ". ";
            else if (c == '#') cout << "# ";
            else cout << "  ";
        }
        cout << endl;
    }
    pausaBFS(); //aca pauso para ver la animacion
}

// es lo mismo pero sin la pausa BFS porque es para mostrar el laberinto final
void mostrarLaberintoFinal(char** matrizLaberinto, int filas, int columnas) { 
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            char c = matrizLaberinto[i][j];
            if (c == 'S') cout << "S ";
            else if (c == 'E') cout << "E ";
            else if (c == '+') cout << "+ ";
            else if (c == '.') cout << ". ";
            else if (c == '#') cout << "# ";
            else cout << "  ";
        }
        cout << endl;
    }
} 

void explorarBacktracking(char** matrizLaberinto, bool** casillasVisitadas, int x, int y, int filas, int columnas) {
    if (x < 0 || y < 0 || x >= filas || y >= columnas) return; // si x o y estan fuera de la matriz, salimos de la fucion
    if (matrizLaberinto[x][y] == '#' || casillasVisitadas[x][y]) return; // o si hay un muro o ya visite esa casilla no sigo por ahi

    casillasVisitadas[x][y] = true; //marco la casilla como visitada para no volver a pasar por ahi
 
    if (matrizLaberinto[x][y] != 'S' && matrizLaberinto[x][y] != 'E') {
        matrizLaberinto[x][y] = '.'; // si la casilla no es E ni S pongo un . 
    }
//uso la recursividad para moverme en cada direccion posible
    explorarBacktracking(matrizLaberinto, casillasVisitadas, x + 1, y, filas, columnas);
    explorarBacktracking(matrizLaberinto, casillasVisitadas, x - 1, y, filas, columnas);
    explorarBacktracking(matrizLaberinto, casillasVisitadas, x, y + 1, filas, columnas);
    explorarBacktracking(matrizLaberinto, casillasVisitadas, x, y - 1, filas, columnas);
}

void generarLaberinto(char** matrizLaberinto, int filas, int columnas) {
    for (int i = 0; i < filas; i++)
        for (int j = 0; j < columnas; j++)
            matrizLaberinto[i][j] = '#';   //recorro toda la matriz

    for (int i = 1; i < filas - 1; i++) {
        for (int j = 1; j < columnas - 1; j++) {
            if (rand() % 100 < 40 ) { // con rand() genero un numero aleatorio con un 40% de probabilidad
                matrizLaberinto[i][j] = ' ';  //si el if anterior es verdadero, la celda se va convertir en un espacio vacio
            }
        }
    }

    matrizLaberinto[0][1] = 'S';   //posiciono la entrada y la salida
    matrizLaberinto[filas - 1][columnas - 2] = 'E';
}

void reiniciarVisitados(bool** casillasVisitadas, int filas, int columnas) {
    for (int i = 0; i < filas; i++)
        for (int j = 0; j < columnas; j++)//para reiniciar las casillas visitdas las marco como false
            casillasVisitadas[i][j] = false;
}

bool resolverBFS(char** matrizLaberinto, bool** casillasVisitadas, pair<int,int>** padreCasilla, int sx, int sy, int filas, int columnas) {
    queue<pair<int, int>> cola; //creo una cola
    cola.push({sx, sy}); //agrego a la cola la posicion actual de donde empieza a buscar
    casillasVisitadas[sx][sy] = true; //marco como visitada la casilla inicial

    int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, 1, -1}; //son  mis movimientos posibles dentro de las 4 direcciones

    while (!cola.empty()) { //mientras que la cola no este vacia
        int x = cola.front().first; //agarro la casilla que esta enfrente de la cola
        int y = cola.front().second;
        cola.pop(); //elimino la casilla actual de la cola porque ya estoy procesando

        if (matrizLaberinto[x][y] == 'E') { //si la casilla esta en el punto de salida 
            pair<int, int> p = padreCasilla[x][y]; //gurado esa casilla en una vt p para volver a retroceder
            while (matrizLaberinto[p.first][p.second] != 'S') { // en el camino y volver al inicio
                matrizLaberinto[p.first][p.second] = '+'; // marco el camino correcto y cambio el . por +
                mostrarLaberintoAnimado(matrizLaberinto, filas, columnas); //llamo a la funcion  el mostrarlaberintoAnimado
                p = padreCasilla[p.first][p.second]; // actualizo mi vt con el padre de la casilla actual y asi hasta
                // regresar al inicio
            }
            return true; // retorno true si se reconstruyo un camino al inicio, o sea que si se encontro solucion
        }

        for (int i = 0; i < 4; i++) { //recorro las 4 direcciones posibles a la que puede moverse el algortimo
            int nx = x + dx[i];
            int ny = y + dy[i]; //calculo la nueva posicion


            /* me aseguro que las nuevas posiciones esten dentro del rango, reviso si la casilla ya fue visitada o no
          acepto moverme si es un espacio libre, le meta o si ya esta marcada como transitable temporalmente */
            if (nx >= 0 && nx < filas && ny >= 0 && ny < columnas &&
                !casillasVisitadas[nx][ny] &&
                (matrizLaberinto[nx][ny] == ' ' || matrizLaberinto[nx][ny] == 'E' || matrizLaberinto[nx][ny] == '.')) {
                cola.push({nx, ny}); //si la condicion se cumple agrego esa casilla a la cola para procesarla dp
                casillasVisitadas[nx][ny] = true; // marco la casilla como visitada para evitar incovenientes
                padreCasilla[nx][ny] = {x, y}; //gaurdo de donde llego en pC para poder reconstruir el camino despues
            }
        }
    }
    return false; //retorno false en caso de que no haya encontrado ninguna solucion
}

int main() {
    srand(time(nullptr)); //inicializo la semilla del generador aleatorio con la hora actual

    int filas, columnas;
    cout << "Ingrese la cantidad de filas: ";
    cin >> filas; //pido que se ingresen las cantidas de filas y columnas
    cout << "Ingrese la cantidad de columnas: ";
    cin >> columnas;




    
    // creo mi matriz dinamica primero creando las filas
    char** matrizLaberinto = new char*[filas];
    bool** casillasVisitadas = new bool*[filas];
    pair<int,int>** padreCasilla = new pair<int,int>*[filas];

    for (int i = 0; i < filas; i++) { // a cada fila le asigno un arreglo de columnas para tener mi matriz completa
        matrizLaberinto[i] = new char[columnas];
        casillasVisitadas[i] = new bool[columnas];
        padreCasilla[i] = new pair<int,int>[columnas]; //guardo de donde viene en cada paso(coordenadas)
    }

    bool resuelto = false; //retorno falso porque el laberinto aun no esta correcto

    //mientars el laberinto no se resuelva, sigo generando otro
        while (!resuelto) {
        generarLaberinto(matrizLaberinto, filas, columnas); //creo el laberinto nuevo
        reiniciarVisitados(casillasVisitadas, filas, columnas);//pongo todos los visitados en falso otra vez
        explorarBacktracking(matrizLaberinto, casillasVisitadas, 0, 1, filas, columnas);//me aseguro q se pueda llegar haciendo backtracking
        reiniciarVisitados(casillasVisitadas, filas, columnas);// vuelvo a reiniciar para usar el BFS
        resuelto = resolverBFS(matrizLaberinto, casillasVisitadas, padreCasilla, 0, 1, filas, columnas);//intento resolver con bfs, si sale bien corto el bucle
    }
  
     //muestro el laberinto terminado y ya resuelto
    cout << "\nLaberinto generado y resuelto:\n";
    mostrarLaberintoFinal(matrizLaberinto, filas, columnas);

    //cuento cuantos pasos tiene el camino marcado con '+'
    int pasos = 0;
    for (int i = 0; i < filas; i++)
        for (int j = 0; j < columnas; j++)
            if (matrizLaberinto[i][j] == '+')
                pasos++;
    
                //muestro cuantos pasos hay en el camino correcto 
    cout << "\nPasos del camino correcto: " << pasos << "\n";

    // 
    for (int i = 0; i < filas; i++) {
        delete[] matrizLaberinto[i];
        delete[] casillasVisitadas[i];
        delete[] padreCasilla[i];
    }
    delete[] matrizLaberinto;
    delete[] casillasVisitadas;
    delete[] padreCasilla;

    return 0; 
}
