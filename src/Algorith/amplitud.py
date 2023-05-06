import numpy as np   #Utilizamos la libreria numpy para la lectura archivos.


class nodo: #Creamos la clase nodo.
    def __init__(self, pos, recorridos, camino, costo):
      self.pos = pos
      self.recorridos = recorridos
      self.camino = camino
      self.costo = costo
    
class posicion:#creamos la clase posicion
    def __init__(self, posx, posy):
      self.posx = posx
      self.posy = posy
    
def costof(matriz,x,y): #creamos la funcion costo que nos devuelve el valor de ponerse en una casilla
  valor = matriz[x][y]
  if valor == 0 or valor == 1 or valor == 2:
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
    
  
def busquedaAmplitud(matriz,x,y):  #Creamos la primera busqueda por amplitud.
    
    nodoc= 0 
    inicio = nodo(posicion(x,y),[],[posicion(x,y)],0)
    juego = matriz #Declaramos a como el archivo.
    cola = []
    cola.append(inicio)    #Declaramos desde donde inicia la cola.
    lista = []
    nodoanterior = 1
    while(True):

      if len(cola) == 0: #Si el tamaño de la cola llega a 0 no lo encontro.
        return False
      
      nodoActual = cola[0] #en este punto revisamos el nodo actual
      contador = ((len(nodoActual.camino)% 2)) +1 #sacamos modulo saldra entre 1 y 2
      if contador == 1 and nodoanterior == 2:#si es 1 y cambio volteamos la cola
       cola = cola[::-1]                     #si fuera iquierda a derecha se voltea y viceversa
       nodoanterior = 1
      elif contador == 2 and nodoanterior == 1:#si es 2 y cambio volteamos la cola
       cola = cola[::-1]
       nodoanterior = 2

      nodoActual = cola.pop(0) #sacamos el primer nodo de la cola y sus respectivas posiciones x,y
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
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
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
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
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
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
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
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
            cola.append(nuevoNodo)
            nodoc = nodoc + 1
            
