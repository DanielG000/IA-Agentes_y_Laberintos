from customtkinter import CTkScrollableFrame

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

    pass
