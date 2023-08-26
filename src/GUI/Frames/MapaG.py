from customtkinter import CTkFrame,CTkScrollableFrame,CTkButton,CTkImage
from PIL import Image, ImageTk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from io import BytesIO
import time

class MapaG(CTkFrame):

    __manager = None
    
    def __init__(self, master, manager):
        super().__init__(master)
        self.__manager = manager
        self.animando = False
        self.colaAnimacion = []
        self.botones = None
        self.pack(side="top",expand=True,fill="both")
        pass


    def ctkimgSVG(self, w, h, ruta):
        # Modificacion de la solucion de SVG encontrada en linea
        width = int(w)
        height = int(h)

        svgFile = svg2rlg(ruta)
        bytesPNG = BytesIO()
        renderPM.drawToFile(svgFile, bytesPNG, fmt="PNG")

        img = Image.open(bytesPNG)
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.image = img

        ctkimg = CTkImage(light_image=img, dark_image=img,size=(height,height)) 
        return ctkimg


    def animar(self,camino,x,y):
        x1 = self.getRelX(y)
        y1 = self.getRelY(x)
        
        agente = self.botones[x][y]
        agente.pack_forget()
        agente.destroy()
        imagen = self.ctkimgSVG(self.width, self.height, self.image_dict[1])
        agente = CTkButton(self, text="", fg_color="transparent", image=imagen, width=self.width, height=self.height, state="disabled" )
        agente.configure(bg_color="transparent")
        self.botones[x][y] = agente
        

        for posicion in camino :
            row = posicion[0]
            col = posicion[1]
            
            x2 = self.getRelX(col)
            y2 = self.getRelY(row)
            self.colaAnimacion.insert(0,[agente,x1,y1,x2,y2])
            x1 = self.getRelX(col)
            y1 = self.getRelY(row)

        self.__manager.ejecutar(self.animacion)
        pass
    
    
    def animacion(self):
        while(len(self.colaAnimacion) >= 1):
            if (not self.animando):
                agente,x1,y1, x2,y2 = self.colaAnimacion.pop() 
                self.mover(agente, x1,y1,x2,y2)
            else:
                None
        pass


    def mover(self,agente,x1,y1,x_destino,y_destino):
        self.animando = True
        x1 =  round(x1, 3)
        y1 =  round(y1, 3)
        x_destino =  round(x_destino, 3)
        y_destino =  round(y_destino, 3)

        if x1 < (x_destino - 0.01):
            x1 += 0.01
            agente.place(relx=x1, rely=y1)
            self.after(10, self.mover, agente, x1,y1, x_destino,y_destino)
        elif x1 > (x_destino + 0.01):
            x1 -= 0.01
            agente.place(relx=x1, rely=y1)
            self.after(10, self.mover, agente, x1,y1, x_destino,y_destino)
        elif y1 < (y_destino - 0.01):
            y1 += 0.01
            agente.place(relx=x1, rely=y1)
            self.after(10, self.mover, agente, x1,y1, x_destino,y_destino)
        elif y1 > (y_destino + 0.01):
            y1 -= 0.01
            agente.place(relx=x1, rely=y1)
            self.after(10, self.mover, agente, x1,y1, x_destino,y_destino)
        else:
            self.animando = False

        pass

    def limpiarMapa(self):
        for y in self.botones:
            for x in y:
                if (not x is None):
                    x.pack_forget()
                    x.destroy()

        self.botones = None
        self.create_widgets()
        pass

    def cargarMapa(self, matriz):
        self.matriz = matriz
        self.X = len(self.matriz[0])
        self.Y = len(self.matriz)
        self.load_images()
        if (not self.botones is None):
            self.limpiarMapa()
        self.create_widgets()
        pass

    def getRelX(self, index):
        escala = (1/self.X)
        relx = index * escala
        return relx

    def getRelY(self, index):
        escala = (1/self.Y)
        rely = index * escala
        return rely

    def load_images(self):
        self.image_dict = {5 : 'GUI/Frames/Imagenes/Bloque.svg',
                           1 : 'GUI/Frames/Imagenes/Agente.svg',
                           4 : 'GUI/Frames/Imagenes/Obstaculo-2.svg',
                           2 : 'GUI/Frames/Imagenes/Meta-1.svg',
                           3 : 'GUI/Frames/Imagenes/Obstaculo-1.svg'
                }

        pass


    def create_widgets(self):

        relWidth = (1/self.X)
        relHeight = (1/self.Y)
        self.width = self.winfo_width() * relWidth
        self.height = self.winfo_height() * relHeight
        # Crea los botones que conforman elementos en el mapa tipo matriz
        self.botones = []
        for row in range(self.Y):
            self.botones.append([])
            for col in range(self.X):
                self.botones[row].append(None)
                imagen = None
                numero = self.matriz[row][col]
                if numero != 0:
                    imagen = self.ctkimgSVG(self.width, self.height, self.image_dict[numero])
                    self.botones[row][col] = CTkButton(self, text="",fg_color="transparent" , image=imagen, width=self.width, height=self.height , state="disabled" )
                    self.botones[row][col].configure(bg_color="transparent")
                    self.botones[row][col].pack()
                    self.botones[row][col].place(relx=self.getRelX(col), rely=self.getRelY(row))
        pass

    pass
