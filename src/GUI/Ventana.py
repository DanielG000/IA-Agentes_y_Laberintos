import customtkinter
from customtkinter import CTk
from GUI.MenuFrame import Menu

class Ventana(customtkinter.CTk):

    __manager = None

    __principal = None
    __lateral = None
    __menu = None

    def __init__(self, main):
        super().__init__()
        self.__manager = main
        self.title("IA Agentes y Laberintos")
        self.geometry("500x400")
        self.create_widgets()
        pass

    def create_widgets(self):
        self.__menu = Menu(self)
        pass

    pass
