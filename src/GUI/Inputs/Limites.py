from customtkinter import CTkFrame, CTkLabel
from GUI.Inputs.NumInput import NumInput

class Limites(CTkFrame):

    __setter1 = None
    __setter2 = None

    __etiqueta1 = None
    __etiqueta2 = None
    __etiqueta3 = None

    __inputIter = None
    __inputProf = None


    def __init__(self, master, metodo1, metodo2):
        super().__init__(master)
        self.__setter1 = metodo1
        self.__setter2 = metodo2
        self.pack()
        self.place(relx=0.61, rely=0.05, relwidth=0.38, relheight=0.60)
        self.create_widgets()
        pass
    
    def create_widgets(self):
        #creacion de componentes
        self.__etiqueta1 = CTkLabel(self, text="Limites de Busqueda")
        self.__etiqueta2 = CTkLabel(self, text="Iteraciones")
        self.__etiqueta3 = CTkLabel(self, text="Profundidad")
        self.__inputIter = NumInput(self, metodo=self.__setter1)
        self.__inputProf = NumInput(self, metodo=self.__setter2)

        #agregar al frame
        self.__etiqueta1.pack()
        self.__etiqueta2.pack()
        self.__etiqueta3.pack()
        self.__inputIter.pack()
        self.__inputProf.pack()

        #posicionamiento
        self.__etiqueta1.place(relx=0.5,rely=0.15,relwidth=1, relheight=0.3, anchor="center")
        self.__etiqueta2.place(relx=0.25,rely=0.35,relwidth=0.5, relheight=0.1, anchor="center")
        self.__etiqueta3.place(relx=0.75,rely=0.35,relwidth=0.5, relheight=0.1, anchor="center")
        self.__inputIter.place(relx=0.25,rely=0.65,relwidth=0.3, relheight=0.3, anchor="center")
        self.__inputProf.place(relx=0.75,rely=0.65,relwidth=0.3, relheight=0.3, anchor="center")

        pass


    pass
