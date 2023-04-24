from customtkinter import CTkFrame

class ArbolG(CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx="5px",pady="5px",side="top",expand=True,fill="both")
        self.create_widgets()
        pass

    def create_widgets(self):
        pass

    pass
