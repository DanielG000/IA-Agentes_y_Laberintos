from GUI.Ventana import Ventana

class main:

    #Objectos GUI
    __ventana = None

    #Manejador de hilos
    __hilos = None

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
