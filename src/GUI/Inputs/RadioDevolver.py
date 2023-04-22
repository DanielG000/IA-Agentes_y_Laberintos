from customtkinter import CTkFrame,CTkLabel,CTkRadioButton
from tkinter import IntVar

class RadioDevolver(CTkFrame):

    __setter = None
    variable = None

    #texto
    __etiqueta = None

    #Opciones
    __si = None
    __no = None


    def __init__(self, master, metodo):
        if (master is None):
            raise Exception("La referencia raiz es None")
        elif (metodo is None):
            raise Exception("No recibio el metodo para devolver el valor")
        super().__init__(master)
        self.__setter = metodo
        self.pack()
        self.place(relx=0.4, rely=0.05, relwidth=0.2,relheight=0.60)
        self.create_widgets()
        pass

    def create_widgets(self):
        self.variable = IntVar()
        #creación de elementos
        self.__etiqueta = CTkLabel(self, text="¿Devolverse?")
        self.__si = CTkRadioButton(self, text="Si", command=self.sendOption, variable=self.variable, value=1)
        self.__no = CTkRadioButton(self, text="No", command=self.sendOption, variable=self.variable, value=2)

        #agregar al frame
        self.__etiqueta.pack()
        self.__si.pack()
        self.__no.pack()

        #Posicion de los elementos
        self.__etiqueta.place(relx=0.5, rely=0.15,relwidth=1,relheight=0.3, anchor="center")
        self.__si.place(relx=0.33, rely=0.65, relwidth=0.3, anchor="center")
        self.__no.place(relx=0.66, rely=0.65, relwidth=0.3, anchor="center")

        pass

    def sendOption(self):
        opcion = None
        match self.variable.get():
            case 1:
                opcion = True
            case 2:
                opcion = False

        self.__setter(opcion)
        pass

    pass
