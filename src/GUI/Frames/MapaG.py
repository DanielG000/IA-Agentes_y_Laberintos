from customtkinter import CTkScrollableFrame,CTkButton
from PIL import Image, ImageTk
import time

class MapaG(CTkScrollableFrame):
    
    def __init__(self, master):
        super().__init__(master)
        #Dimenciones del tablero
        self.BOARD_WIDTH = 5
        self.BORAD_HEIGHT = 5
        #Dimenciones de las imagenes
        self.IMAGE_WIDTH = 100
        self.IMAGE_HEIGHT = 100
        self.pack(padx="5px",pady="5px",side="top",expand=True,fill="both")
        pass

    def cargarMapa(self,matriz):
        self.matriz = matriz
        print(matriz)
        self.load_images()
        self.create_widgets()
        pass

    def animar(self,camino,x,y):
        for posicion in camino:
            row = posicion[0]
            col = posicion[1]

            self.mbotones[row][col].configure(image=self.images[x][y])
        pass


    def load_images(self):
        self.image_dict = {0 : 'GUI/Frames/Imagenes/Vacio.jpg',
                           5 : 'GUI/Frames/Imagenes/Bloque.jpg',
                           1 : 'GUI/Frames/Imagenes/Pinocho.jpg',
                           4 : 'GUI/Frames/Imagenes/Zorro.jpg',
                           2 : 'GUI/Frames/Imagenes/Geppetto.jpg',
                           3 : 'GUI/Frames/Imagenes/Cigarrillo.jpg'
                }
        
        self.images = []
        for row in self.matriz:
            row_images = []
            for col in row:
                try:
                    image_path = self.image_dict[col]
                    image = Image.open(image_path).resize(
                        (self.IMAGE_WIDTH, self.IMAGE_HEIGHT), Image.LANCZOS
                        )
                except:
                    image = Image.new('RGB',
                                      (self.IMAGE_WIDTH, self.IMAGE_HEIGHT),
                                      color=(255,255,255)
                                      )
                row_images.append(ImageTk.PhotoImage(image))

            self.images.append(row_images)
        pass

    def create_widgets(self):
        # Crea un boton para cada celda de la matriz
        self.mbotones = []
        for row in range(len(self.matriz)):
            self.mbotones.append([])
            for col in range(len(self.matriz[0])):
                self.mbotones[row].append(None)
                self.mbotones[row][col] = CTkButton(self, text="", image=self.images[row][col], width=self.winfo_width()*(1/len(self.matriz[0])), height=self.winfo_height()*(1/(len(self.matriz) * 2)))
                self.mbotones[row][col].grid(row=row, column=col) 
        pass

    pass
