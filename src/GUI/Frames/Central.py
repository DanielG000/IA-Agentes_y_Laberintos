from customtkinter import CTkTabview
from GUI.Frames.MapaG import MapaG
from GUI.Frames.ArbolG import ArbolG

class Central(CTkTabview):

    __mapaG = None
    __arbolG = None

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx="5px", pady="5px", side="left",expand=True,fill="both")
        self.create_widgets()
        pass

    def create_widgets(self):
        self.add("Mapa")
        self.add("Arbol")
        
        self.__mapaG = MapaG(self.tab("Mapa"))
        self.__arbolG= ArbolG(self.tab("Arbol"))

        pass

    pass
