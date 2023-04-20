from GUI.Ventana import Ventana
#from Structure-Hilos import Hilos
#from Structure.
#from Structure.Arbol import Hilos

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
        self.__ventana = Ventana(self)
        self.startGUI()
        pass

    def startGUI(self):
        self.__ventana.mainloop()
        pass

    pass

main()
