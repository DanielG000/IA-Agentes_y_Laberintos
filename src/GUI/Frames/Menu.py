from customtkinter import CTkFrame, CTkButton
from GUI.Inputs.RadioBusqueda import RadioBusqueda
from GUI.Inputs.RadioDevolver import RadioDevolver
from GUI.Inputs.Limites import Limites

class Menu(CTkFrame):

    __opcionBusqueda = None     #String
    __opcionDevolverse = None   #Boleano
    __limiteI = None            #Int
    __limiteP = None            #Int

    #Opciones especiales para 
    __limiteDeIteraciones = None
    __limiteDeProfundidad = None

    #Frames
    __panelBusqueda = None
    __panelDevolver = None
    __limitesBusqueda = None

    #Botones
    __config = None
    __subir = None
    __cambioFrame = None
    __iniciar = None

    def __init__(self, master=None):
        if(master is None):
            raise Exception("No hay una ventana raiz")
        super().__init__(master)
        self.pack(padx="5px",pady="5px",side="bottom",fill="both")
        self.create_widgets()
        pass


    def create_widgets(self):
        #creación de cada componente
        self.__config = CTkButton(self, text="")
        self.__subir = CTkButton(self, text="Subir mapa")
        self.__iniciar = CTkButton(self, text="") 
        self.__iniciar.configure(state="disabled")

        #los frames solo se crean por lo que se auto posicionan
        self.__panelBusqueda = RadioBusqueda(self, self.setBusqueda)
        self.__panelDevolver = RadioDevolver(self, self.setDevolver)
        self.__limitesBusqueda = Limites(self, self.setLimiteI, self.setLimiteP)
        
        #Mostrar en el frame
        self.__config.pack()
        self.__subir.pack()
        self.__iniciar.pack()

        #Posicion de los componentes
        self.__config.place(relx=0.01, rely=0.75, relwidth=0.09, relheight=0.20)
        self.__subir.place(relx=0.11, rely=0.75, relwidth=0.20, relheight=0.20)
        self.__iniciar.place(relx=0.90, rely=0.75, relwidth=0.09, relheight=0.20)

        pass

    # Recibe un str (string) para luego elejir la busqueda.
    def setBusqueda(self,opcion):
        if(type(opcion) != type("String")):
            raise Exception("Tipo de parametro erroneo, recibe un str (String)")
        else:
            self.opcionBusqueda = opcion
        pass

    # Recibe el boleano y lo guarda en la clase para usarlo luego
    def setDevolver(self,opcion):
        if (type(opcion) != type(True)):
            raise Exception("Tipo de parametro erroneo, debes usar boolean")

        self.opcionDevolverse = opcion
        pass

    def setLimiteI(self,numero):
        if (type(numero) != type(1) and type(numero) != type(1.0)):
            raise Exception("No es un numero entero o flotante")
        self.__limiteI = numero
        pass

    def setLimiteP(self,numero):
        if (type(numero) != type(1) and type(numero) != type(1.0)):
            raise Exception("No es un numero entero o flotante")
        self.__limiteP = numero
        pass

    pass
