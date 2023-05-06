import numpy as np   #Utilizamos la libreria numpy para la lectura archivos.
import heapq


class nodo: #Creamos la clase nodo.
    def __init__(self, costo,pos, recorridos, camino):
      self.costo = costo
      self.recorridos = recorridos
      self.camino = camino
      self.pos = pos
    def __lt__(self, otro_nodo):
     return self.costo < otro_nodo.costo
    
class posicion:#creamos la clase posicion
    def __init__(self, posx, posy):
      self.posx = posx
      self.posy = posy

def costonodo(nodo):#Creamos la funcion costonodo que nos devuelve el costo que hay en un nodo
    return nodo.costo

def costof(matriz,x,y):
  valor = matriz[x][y]
  if valor == 0 or valor == 1 or valor == 2:#Creamos la funcion buscar elemento para ver si se encuentra en la lista el elemento.
   return 1
  elif valor == 3:
   return 2
  elif valor == 4:
   return 3
  elif valor == 5:
    return 4
  elif valor == None:
   return 5


def buscarElemento(lista, elemento): #Creamos la funcion buscar elemento para ver si se encuentra en la lista el elemento.
    for i in lista:
      if i.posx == elemento.posx and i.posy == elemento.posy:
        return True

    else: 
      return False
    
 
def busquedaCosto(matriz,x,y):  #Creamos la primera busqueda por costo ---amplitud.
    
    nodoc= 0 
    inicio = nodo(0,posicion(x,y),[],[posicion(x,y)])
    juego = matriz #Declaramos a como el archivo.
    cola = []
    cola.append(inicio)    #Declaramos desde donde inicia la cola.
    lista = []

    while(True):

      if len(cola) == 0:
         #Si el tamaño de la cola llega a 0 no lo encontro.
        return False


      heapq.heapify(cola)#ponemos la cola por prioridad siendo el primer dato costo ordenandolo por este
      nodoActual = heapq.heappop(cola)#sacamos el nodo mas bajo de la cola y sus respectivas posiciones x,y
      posX = nodoActual.pos.posx
      posY = nodoActual.pos.posy

      
      
      if juego[posX][posY] == 2: #Declaramos el valor neseciario para encontrar al objetivo.
        lista = []
        costot = nodoActual.costo
        for i in nodoActual.camino:
         lista.append((i.posx,i.posy))  
        return (lista,costot,nodoc)
      
      if not(juego[posX][posY] == 5 ): #Declaramos los sitios por los que no puede pasar el robot.


        #Arriba
        if(nodoActual.pos.posy>0):#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx,nodoActual.pos.posy-1)
          recorridoA = nodoActual.recorridos.copy()
          caminoA = nodoActual.camino.copy()
          nodoc = nodoc + 1
        #Verifica si se puede ir a la siguiente posicion, y si es asi se va hacia la direccion indicada creando una copia en el proceso
          #para asi recorrer todas las posiciones mediante copias temporales.
        
       
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:          
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx,nodoActual.pos.posy-1)
            recorridoA.append(nodoActual.pos)
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(costoa,posicionNueva,recorridoA,caminoA)
            cola.append(nuevoNodo)
            
          
        #Abajo
        if(nodoActual.pos.posy<len(juego)-1):#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx,nodoActual.pos.posy+1)
          recorridoA = nodoActual.recorridos.copy()

          caminoA = nodoActual.camino.copy()
          nodoc = nodoc + 1
        #Verifica si se puede ir a la siguiente posicion, y si es asi se va hacia la direccion indicada creando una copia en el proceso
          #para asi recorrer todas las posiciones mediante copias temporales.
        
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:          
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx,nodoActual.pos.posy+1)
            recorridoA.append(nodoActual.pos)
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(costoa,posicionNueva,recorridoA,caminoA)
            cola.append(nuevoNodo)            

        #Derecha
        if nodoActual.pos.posx<len(juego)-1:#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx+1,nodoActual.pos.posy)
          recorridoA = nodoActual.recorridos.copy()
          caminoA = nodoActual.camino.copy()

        #Verifica si se puede ir a la siguiente posicion, y si es asi se va hacia la direccion indicada creando una copia en el proceso
          #para asi recorrer todas las posiciones mediante copias temporales.
        
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:
            recorridoA.append(nodoActual.pos)          
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx+1,nodoActual.pos.posy)
            caminoA.append(posicionNueva)
            nodoc = nodoc + 1
            nuevoNodo = nodo(costoa,posicionNueva,recorridoA,caminoA)
            cola.append(nuevoNodo)

        #Izquierda
        if(nodoActual.pos.posx>0):#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx-1,nodoActual.pos.posy)
          recorridoA = nodoActual.recorridos.copy()
          caminoA = nodoActual.camino.copy()

          
        #Verifica si se puede ir a la siguiente posicion, y si es asi se va hacia la direccion indicada creando una copia en el proceso
          #para asi recorrer todas las posiciones mediante copias temporales.
                
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:          
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx-1,nodoActual.pos.posy)
            recorridoA.append(nodoActual.pos)
            caminoA.append(posicionNueva)
            nuevoNodo = nodo(costoa,posicionNueva,recorridoA,caminoA)
            cola.append(nuevoNodo)
            nodoc = nodoc + 1
            

      



