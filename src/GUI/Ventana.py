import customtkinter
from customtkinter import CTk
from GUI.MenuFrame import Menu
from GUI.LateralFrame import Lateral

class Ventana(customtkinter.CTk):

    __manager = None

    __principal = None
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
        pass

    pass
