from GUI.Ventana import Ventana
from Structure.Hilos import Hilos
from Structure.Mapa import Mapa
from Algorith.amplitud import *
from Algorith.costo import *
from Algorith.profundidad import *

class main:

    #Objectos GUI
    __ventana = None

    #Manejador de hilos
    __managerHilos = None

    #Objetos funcionales
    __arbol = None
    __mapa = None

    #Constructor
    def __init__(self):
        #3 hilos maximo (1 GUI, 2 Procesos, 3 actualización recurrente de frames)
        self.__mapa = Mapa()
        self.__managerHilos = Hilos(3)
        self.__ventana = Ventana(self)
        self.startGUI()
        pass

    def solucionar(self, opcion):
        camino = None
        matriz = self.__mapa.getMapa()
        inicio = self.__mapa.getInicio()
        if opcion == "Amplitud":
            camino = busquedaAmplitud(matriz,inicio[0],inicio[1])
        elif opcion == "Costo":
            camino = busquedaCosto(matriz, inicio[0], inicio[1])
        elif opcion == "Profundidad iterativa":
            camino = profundidadi(matriz, inicio[0], inicio[1])

        if camino is False or camino is None:
            self.__ventana.setResultado("No se encontro solución",inicio[0],inicio[1])
        elif type(camino[0]) == type([]):
            print(camino[0])
            print(camino[1])
            print(camino[2])

            self.__ventana.setResultado(camino[0],inicio[0],inicio[1])
        else:
            self.__ventana.setResultado(camino,inicio[0],inicio[1])


        pass

    def ejecutar(self, funcion, **parametros):
        self.__managerHilos.usarHilo(funcion, **parametros)
        pass
    
    def startGUI(self):
        self.ejecutar(self.__ventana.mainloop())
        pass
    
    def mapaNuevo(self,ruta):
        self.__mapa.leerMapa(ruta)
        matriz = self.__mapa.getMapa()
        self.__ventana.setMapa(matriz)
        pass

    pass

main()
