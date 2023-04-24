class Mapa:

    __matriz = None

    def __init__(self):
        pass

    def leerMapa(self, ruta):
        file = open(ruta, 'r')
        lineas = file.readlines()
        file.close()
        size = lineas[0].split()

        if len(size) != 2:
            self.errorFormato()
        else:
            self.__matriz = []

            if len(lineas) != size[0]+1:
                self.errorFormato()
            else:
                for nf in range(1, (size[0]+1) ):
                    fila = lineas[nf]
                    columnas = file.split()

                    if len(columnas) != size[1]:
                        self.errorFormato()
                    else:
                        self.__matriz.append(columnas)

        pass

    def errorFormato(self):
        raise Exception("Error con el Formato del contenido del archivo")
        pass 

    def getMapa(self):
        return self.__matriz

    pass
