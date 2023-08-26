from customtkinter import CTkTabview
from GUI.Frames.MapaG import MapaG
from GUI.Frames.ArbolG import ArbolG

class Central(CTkTabview):

    __manager = None

    __mapaG = None
    __arbolG = None

    def __init__(self, master, manager):
        super().__init__(master)
        self.__manager = manager
        self.pack(padx="1px", pady="1px", side="left",expand=True,fill="both")
        self.place(relx=0.01, rely=0, relwidth=0.89, relheight=0.75)
        self.create_widgets()
        pass

    def create_widgets(self):
        self.add("Mapa")
        #self.add("Arbol")
        
        self.__mapaG = MapaG(self.tab("Mapa"), manager=self.__manager)
        #self.__arbolG= ArbolG(self.tab("Arbol"))

        pass

    def setResultado(self, resultado,x,y):
        self.__mapaG.animar(resultado,x,y)
        pass

    def setMapa(self,matriz):
        self.__mapaG.cargarMapa(matriz)
        pass

    pass
