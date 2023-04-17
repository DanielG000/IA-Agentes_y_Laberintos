from customtkinter import CTkFrame, CTkButton

class Menu(CTkFrame):

    #Frames
    __panelAlboritmo = None
    __evitar = None
    __configBusqueda = None

    #Botones
    __config = None
    __subir = None
    __cambioFrame = None
    __iniciar = None

    def __init__(self, master=None):
        if(master is None):
            raise Exception("No hay una ventana raiz")
        super().__init__(master)
        self.pack(side="bottom",fill="both")
        self.create_widgets()
        pass

    def create_widgets(self):
        #creación de cada componente
        self.__config = CTkButton(self, text="")
        self.__subir = CTkButton(self, text="Subir mapa")
        self.__iniciar = CTkButton(self, text="") 
        
        #Mostrar en el frame
        self.__config.pack()
        self.__subir.pack()
        self.__iniciar.pack()

        #Posicion de los componentes
        self.__config.place(relx=0.01, rely=0.75, relwidth=0.09, relheight=0.20)
        self.__subir.place(relx=0.11, rely=0.75, relwidth=0.20, relheight=0.20)
        self.__iniciar.place(relx=0.90, rely=0.75, relwidth=0.09, relheight=0.20)

        pass

    pass
