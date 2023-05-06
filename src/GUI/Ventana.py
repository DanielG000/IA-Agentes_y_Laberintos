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
        self.__lateral = Lateral(self, width=150, height=1000)
        self.__central = Central(self)
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

    def setResultado(self, resultado):
        if type(resultado) is str:
            self.__lateral.setResultado(resultado)
        elif type(resultado) is []:
            self.__lateral.setResultado(resultado)
            self.__central.setResultado(resultado)

    pass
