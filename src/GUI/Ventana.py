import customtkinter
from customtkinter import CTk
from GUI.Frames.Menu import Menu
from GUI.Frames.Lateral import Lateral
from GUI.Frames.Central import Central

class Ventana(customtkinter.CTk):

    __manager = None

    __central = None
    __lateral = None
    __menu = None

    def __init__(self, main):
        super().__init__()
        self.__manager = main
        self.title("IA Agentes y Laberintos")
        self.geometry("900x600")
        self.create_widgets()
        pass

    def create_widgets(self):
        #loc componentes se crean y agregan a la interfas de forma automatica
        self.__menu = Menu(self)
        self.__lateral = Lateral(self, manager=self.__manager)
        self.__central = Central(self, manager=self.__manager)
        pass

    def usarHilo(self, funcion, **parametros):
        self.__manager.ejecutar(funcion, **parametros)
        pass

    def rutaMapa(self, ruta):
        self.__manager.mapaNuevo(ruta)
        pass

    def setMapa(self, matriz):
        self.__central.setMapa(matriz)
        pass

    def solucionar(self, opcion):
        self.__manager.solucionar(opcion)
        pass

    def setResultado(self, resultado,x,y):
        if type(resultado) is type(""):
            self.__lateral.setResultado(resultado,x,y)
        elif type(resultado) == type([]):
            self.__lateral.setResultado(resultado,x,y)
            self.__central.setResultado(resultado,x,y)

    pass
