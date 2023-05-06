from customtkinter import CTkScrollableFrame, CTkLabel

class Lateral(CTkScrollableFrame):

    def __init__(self,master, **kwargs):
        if master is None:
            raise Exception("No hay una ventana raiz")
        super().__init__(master, **kwargs)
        self.pack(padx="5px", pady="5px", side="right", fill="both")
        self.create_widgets()
        pass

    def create_widgets(self):
        pass

    def setResultado(self, resultado):
        if type(resultado) is str:
            self.label = CTkLabel(self, text=resultado)
            self.label.pack()
        elif type(resultado) is [1,2]:
            texto = ""
            for a in resultado:
                texto += str(a)+"\n"
            self.label = CTkLabel(self, text=texto)
            self.label.pack()

        pass

    pass
