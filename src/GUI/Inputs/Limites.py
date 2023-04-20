from customtkinter import CTkFrame
from GUI.Inputs.NumInput import NumInput

class Limites(CTkFrame):

    __setter1 = None
    __setter2 = None

    def __init__(self, master, metodo1, metodo2):
        super().__init__(master)
        self.__setter1 = metodo1
        self.__setter2 = metodo2
        self.create_widgets()
        pass
    
    def create_widgets(self):
        pass


    pass
