from customtkinter import CTkFrame, CTkButton, CTkEntry 

class NumInput(CTkFrame):

    __value = None
    __setter = None

    __inputBox = None
    __botonQuitar = None
    __botonAgregar = None


    def __init__(self, master, metodo, **kwargs):
        super().__init__(master, **kwargs)
        self.__setter = metodo
        self.create_widgets()
        pass

    def create_widgets(self):
        #Se crean los componentes con sus tamaños
        self.__botonQuitar = CTkButton(self, text="", command=self.quitar)
        self.__inputBox = CTkEntry(self, border_width=0)
        self.__botonAgregar = CTkButton(self, text="", command=self.agregar)

        #ahora se agregan al widget principal
        self.__botonQuitar.pack()
        self.__inputBox.pack()
        self.__botonAgregar.pack()

        #poscicionamiento relativo
        self.__botonQuitar.place(relx=0.13, rely=0.5, relwidth=0.22, relheight=0.9, anchor="center")
        self.__inputBox.place(relx=0.5, rely=0.5, relwidth=0.46, relheight=0.9, anchor="center")
        self.__botonAgregar.place(relx=0.87, rely=0.5, relwidth=0.22, relheight=0.9, anchor="center")

        #se le da valor inicial a la entrada de texto
        self.__inputBox.insert(0, "0")

        #se pone a escuchar el evento de la tecla Enter
        self.__inputBox.bind('<Return>', self.editar)

        pass

    def editar(self, evento):
        try:
            self.__value = int(self.__inputBox.get())
            if(self.__value < 0):
                self.__value = 0
            self.__inputBox.delete(0, "end")
            self.__inputBox.insert(0, self.__value)
            self.send()
        except ValueError:
            self.__inputBox.delete(0, "end")
            self.__inputBox.insert(0, "0")
        pass

    def quitar(self):
        try:
            self.__value = int(self.__inputBox.get()) - 1
            if(self.__value < 0):
                self.__value = 0
            self.__inputBox.delete(0, "end")
            self.__inputBox.insert(0, self.__value)
            self.send()
        except ValueError:
            self.__inputBox.delete(0, "end")
            self.__inputBox.insert(0, "0")
        pass

    def agregar(self):
        try:
            self.__value = int(self.__inputBox.get()) + 1
            self.__inputBox.delete(0, "end")
            self.__inputBox.insert(0, self.__value)
            self.send()
        except ValueError:
            self.__inputBox.delete(0, "end")
            self.__inputBox.insert(0, "0")
        pass


    def send(self):
        self.__setter(self.__value)
        pass

    pass
