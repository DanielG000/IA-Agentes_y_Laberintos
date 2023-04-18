from customtkinter import CTkFrame,CTkLabel,CTkRadioButton
from tkinter import IntVar

class OpcionBusqueda(CTkFrame):

    variable = None

    #texto
    __etiqueta = None

    #Opciones
    __amplitud = None
    __costo = None
    __profundidadI = None

    def __init__(self, master=None):
        if (master is None):
            raise Exception("La referencia raiz es None")
        super().__init__(master)
        self.pack()
        self.place(relx=0.01, rely=0.05, relwidth=0.38,relheight=0.60)
        self.create_widgets()
        pass

    def create_widgets(self):
        self.variable = IntVar()
        #creación de elementos
        self.__etiqueta = CTkLabel(self, text="Busquedas Desinformadas")
        self.__amplitud = CTkRadioButton(self, text="Amplitud", command=self.sendOption, variable=self.variable, value=1)
        self.__costo = CTkRadioButton(self, text="Costo", command=self.sendOption, variable=self.variable, value=2)
        self.__profundidadI = CTkRadioButton(self, text="Profundidad\nIterativa", command=self.sendOption, variable=self.variable, value=3)

        #agregar al frame
        self.__etiqueta.pack()
        self.__amplitud.pack()
        self.__costo.pack()
        self.__profundidadI.pack()

        #Posicion de los elementos
        self.__etiqueta.place(relx=0.5, rely=0.15, relwidth=1,relheight=0.3, anchor="center")
        self.__amplitud.place(relx=0.25, rely=0.65, anchor="center")
        self.__costo.place(relx=0.50, rely=0.65, anchor="center")
        self.__profundidadI.place(relx=0.75, rely=0.65, anchor="center")

        pass

    def sendOption(self):
        opcion = None
        match self.variable.get():
            case 1:
                opcion="Amplitud"
            case 2:
                opcion="Costo"
            case 3:
                opcion="Profundidad iterativa"

        self.master.setBusqueda(opcion)
        pass

    pass
