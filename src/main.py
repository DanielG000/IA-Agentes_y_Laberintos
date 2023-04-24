from GUI.Ventana import Ventana
from Structure.Hilos import Hilos
from Structure.Mapa import Mapa
#from Structure. import 

class main:

    #Objectos GUI
    __ventana = None

    #Manejador de hilos
    __managerHilos = None

    #Objetos funcionales
    __pinocho = None
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


    def ejecutar(self, funcion, **parametros):
        self.__managerHilos.usarHilo(funcion, **parametros)
        pass
    
    def startGUI(self):
        self.ejecutar(self.__ventana.mainloop())
        pass
    
    def mapaNuevo(self,ruta):
        self.ejecutar(self.__mapa.leerMapa(ruta))
        pass

    pass

main()
