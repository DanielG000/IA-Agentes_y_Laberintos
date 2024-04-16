from customtkinter import CTkFrame, CTkButton, filedialog
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
        super().__init__(master, fg_color=master.cget("fg_color"))
        self.__limiteI = 0
        self.__limiteP = 0
        self.pack(padx="1px",pady="1px",side="bottom",fill="both")
        self.place(relx=0, rely=0.75 , relwidth=1 ,relheight=0.25)
        self.create_widgets()
        pass


    def create_widgets(self):
        #creación de cada componente
        #self.__config = CTkButton(self, text="")
        self.__subir = CTkButton(self, text="Subir mapa", command=self.subirMapa)
        self.__iniciar = CTkButton(self, text="", command=self.iniciar) 
        self.__iniciar.configure(state="disabled")

        #los frames solo se crean por lo que se auto posicionan
        self.__panelBusqueda = RadioBusqueda(self, self.setBusqueda)
        #self.__panelDevolver = RadioDevolver(self, self.setDevolver)
        #self.__limitesBusqueda = Limites(self, self.setLimiteI, self.setLimiteP)
        
        #Mostrar en el frame
        #self.__config.pack()
        self.__subir.pack()
        self.__iniciar.pack()

        #Posicion de los componentes
        #self.__config.place(relx=0.01, rely=0.75, relwidth=0.09, relheight=0.20)
        self.__subir.place(relx=0.11, rely=0.75, relwidth=0.20, relheight=0.20)
        self.__iniciar.place(relx=0.90, rely=0.75, relwidth=0.09, relheight=0.20)

        pass

    #

    # recibe la opcion en String (str) de la busqueda
    def setBusqueda(self,opcion):
        if(type(opcion) != type("String")):
            raise Exception("Tipo de parametro erroneo, recibe un str (String)")
        else:
            self.__opcionBusqueda = opcion
            self.inicioHabilitable()
        pass

    # Recibe el boleano y lo guarda en la clase para usarlo luego
    def setDevolver(self,opcion):
        if (type(opcion) != type(True)):
            raise Exception("Tipo de parametro erroneo, debes usar boolean")
        else:
            self.__opcionDevolverse = opcion
            self.inicioHabilitable()
        pass

    def setLimiteI(self,numero):
        if (type(numero) != type(1)):
            raise Exception("No es un numero entero o flotante")
        else:
            self.__limiteI = numero
            self.inicioHabilitable()
        pass

    def setLimiteP(self,numero):
        if (type(numero) != type(1) and type(numero) != type(1.0)):
            raise Exception("No es un numero entero o flotante")
        else:
            self.__limiteP = numero
            self.inicioHabilitable()
        pass


    #mira si tiene lo necesario para habilitar el boton para iniciar el agente
    def inicioHabilitable(self):
        habilitar = True
        if(self.__opcionBusqueda is None):
            habilitar = False
        #elif(self.__opcionDevolverse is None):
        #   habilitar = False
        #elif(self.__limiteI is None or self.__limiteI <= 0) and (self.__opcionBusqueda == "Profundidad iterativa"):
        #    habilitar = False

        if habilitar:
            self.__iniciar.configure(state="normal")
        else:
            self.__iniciar.configure(state="disabled")

        pass


    def config(self):
        pass

    def subirMapa(self):
        ruta = filedialog.askopenfilename(title='Mapa Laberinto',initialdir='./Mapas')
        self.master.rutaMapa(ruta)
        pass

    def iniciar(self):
        self.master.solucionar(self.__opcionBusqueda)
        pass

    pass
