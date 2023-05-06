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

def costof(matriz,x,y):#Creamos la funcion buscar elemento para ver si se encuentra en la lista el elemento.
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
    


def busquedaProfundida(matriz,x,y,piso,nodos):
    juego = matriz #Declaramos a como el archivo.
    pila = []
    inicio = nodo(posicion(x,y),[],[posicion(x,y)],0)
    nodoc = nodos
    pila.append(inicio)#Utilizamos la posicion inicial del robot.
    

    
    #Busqueda amplitud
    while(True):
     
     #paro si no encontré a gepetto
      if len(pila) == 0:
        lista = []
        costot = nodoActual.costo
        for i in nodoActual.camino:
         lista.append((i.posx,i.posy))  
        return (1,lista,costot,nodoc)
      
      nodoActual = pila.pop(-1)#sacamos el nodo mas profundo de la cola y sus respectivas posiciones x,y
      posX = nodoActual.pos.posx
      posY = nodoActual.pos.posy

      #paro si encontré a gepetto
      if juego[posX][posY] == 2:
        lista = []
        costot = nodoActual.costo
        for i in nodoActual.camino:
         lista.append((i.posx,i.posy)) 
        return (2,lista,costot,nodoc)


      if not(juego[posX][posY] == 5):

        #Arriba
        if(nodoActual.pos.posy>0):#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx,nodoActual.pos.posy-1)
          recorridoA = nodoActual.recorridos.copy()
          caminoA = nodoActual.camino.copy()
          nodoc = nodoc + 1

        #primero declaramos una copia de las funciones si cumple que no se a hecho antes modifca los datos
        #y se agregan los caminos,ademas de sumar a la cola
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:
            recorridoA.append(nodoActual.pos)
            caminoA.append(posicionNueva)
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx,nodoActual.pos.posy-1)
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
            pila.append(nuevoNodo)

        #Abajo
        if(nodoActual.pos.posy<len(juego)-1):#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx,nodoActual.pos.posy+1)
          recorridoA = nodoActual.recorridos.copy()
          caminoA = nodoActual.camino.copy()
          nodoc = nodoc + 1

#primero declaramos una copia de las funciones si cumple que no se a hecho antes modifca los datos
        #y se agregan los caminos,ademas de sumar a la cola
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:
            recorridoA.append(nodoActual.pos)
            caminoA.append(posicionNueva)
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx,nodoActual.pos.posy+1)
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
            pila.append(nuevoNodo)

        #Derecha
        if nodoActual.pos.posx<len(juego)-1:#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx+1,nodoActual.pos.posy)
          recorridoA = nodoActual.recorridos.copy()
          caminoA = nodoActual.camino.copy()
          nodoc = nodoc + 1

#primero declaramos una copia de las funciones si cumple que no se a hecho antes modifca los datos
        #y se agregan los caminos,ademas de sumar a la cola
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:
            recorridoA.append(nodoActual.pos)
            caminoA.append(posicionNueva)
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx+1,nodoActual.pos.posy)
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
            pila.append(nuevoNodo)

        #Izquierda
        if(nodoActual.pos.posx>0):#verificamos que no se salga de los limites de la matriz
          posicionNueva = posicion(nodoActual.pos.posx-1,nodoActual.pos.posy)
          recorridoA = nodoActual.recorridos.copy()
          caminoA = nodoActual.camino.copy()
          nodoc = nodoc + 1
          
          #primero declaramos una copia de las funciones si cumple que no se a hecho antes modifca los datos
        #y se agregan los caminos,ademas de sumar a la cola
          if buscarElemento(nodoActual.recorridos,posicionNueva)==False and juego[posicionNueva.posx
          ][posicionNueva.posy]!=1:
            recorridoA.append(nodoActual.pos)
            caminoA.append(posicionNueva)
            costoa = nodoActual.costo + costof(juego,nodoActual.pos.posx-1,nodoActual.pos.posy)
            nuevoNodo = nodo(posicionNueva,recorridoA,caminoA,costoa)
            pila.append(nuevoNodo)

      lista = []
      for i in nodoActual.camino: #verificamos que no se pase del piso limite
        lista.append((i.posx,i.posy)) #en caso contrario para
      if len(lista) > piso:
        return (False,lista,nodoc)
      



def profundidadi(matriz,x,y):
 piso = 0 
 nodos = 0
 while (True):
   resultado= [] 
   resultado= busquedaProfundida(matriz,x,y,piso,nodos)
   nodos = resultado[2]
                              #declaramos resultado para que le de un tope a busqueda profundida
   if resultado[0] == False:  #y si no encuentra la solucion siga bsucando con un piso mayor
    piso = piso + 1
   
   elif resultado[0] == 1: #encontre a gepetto
    return False
   
   elif resultado[0] == 2: #no encontre a gepetto
    return resultado[1]

        

      

   
   

