from customtkinter import CTkTabview
from GUI.Frames.MapaG import MapaG

class Central(CTkTabview):

    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        pass

    def create_widgets(self):
        self.add("Arbol")
        self.add("Mapa")
        pass

    pass
