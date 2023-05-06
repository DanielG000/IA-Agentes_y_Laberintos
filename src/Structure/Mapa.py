class Mapa:

    __inicio = None
    __matriz = None

    def leerMapa(self, ruta):
        file = open(ruta, 'r')
        lineas = file.readlines()
        file.close()
        self.__matriz = self.comprobarFormato(lineas)
        inicio = self.comprobarInicio()
        final = self.comprobarMeta()
        if not inicio:
            self.__matriz = []
            self.error("falta el agente/pinocho")
        elif not final:
            self.__matriz = []
            self.error("falta la meta/gepetto")
        pass

    def error(self, texto):
            raise Exception("Error con el Formato, {}".format(texto))

    def comprobarFormato(self, lineas):
        size = lineas[0].split()
        size[0] = int(size[0])
        size[1] = int(size[1])
        matriz = []

        if len(size) != 2:
            self.error("tamaño del mapa.")
        elif len(lineas) != size[0]+1:
            self.error("cantidad de las filas.")
        else:
            for nf in range(1, (size[0]+1) ):
                fila = lineas[nf]
                columnas = fila.split()
                if len(columnas) != size[1]:
                    self.error("cantidad de columnas.")
                else:
                    cols = []
                    for colum in columnas:
                        cols.append(int(colum))
                    matriz.append(cols)

        return matriz


    def comprobarInicio(self):
        inicio = False
        for fila in self.__matriz:
            for columna in fila:
                if (columna == 1):
                    inicio = True
                    self.__inicio = [fila,columna]
                    break
            if inicio:
                break
        return inicio


    def comprobarMeta(self):
        meta = False
        for fila in self.__matriz:
            for columna in fila:
                if (columna == 2):
                    meta = True
                    break
            if meta:
                break
        return meta

    def getMapa(self):
        return self.__matriz

    def getInicio(self):
        return self.__inicio

    pass
