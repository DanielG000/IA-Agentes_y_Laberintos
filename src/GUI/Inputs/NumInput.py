from customtkinter import CTkFrame, CTkButton 

class NumInput(CTkFrame):

    __setter = None
    __inputBox = None
    __quitar = None
    __agregar = None
    __value = None

    def __init__(self, master, command):
        super().__init__(master)
        self.__setter = command
        pass

    def create_widgets(self):
        pass

    def quitar(self):
        pass

    def agregar(self):
        pass


    def send(self):
        self.setter(self.__value)
        pass

    pass
