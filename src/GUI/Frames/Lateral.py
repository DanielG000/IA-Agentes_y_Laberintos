from customtkinter import CTkScrollableFrame, CTkLabel

class Lateral(CTkScrollableFrame):

    __manager = None

    def __init__(self,master, manager, **kwargs):
        if master is None:
            raise Exception("No hay una ventana raiz")
        super().__init__(master, fg_color=master.cget("fg_color"), **kwargs)
        self.__manager = manager
        self.pack(padx="1px", pady="1px", side="right", fill="both")
        self.place(relx=0.9,rely=0,relwidth=0.1, relheight=0.75)
        self.create_widgets()
        pass

    def create_widgets(self):
        pass

    def setResultado(self, resultado,x,y):
        if type(resultado) is type(""):
            self.label = CTkLabel(self, text=resultado)
            self.label.pack()
        elif type(resultado) == type([1,2]):
            texto = ""
            for a in resultado:
                texto += str(a)+"\n"
            self.label = CTkLabel(self, text=texto)
            self.label.pack()

        pass

    pass
