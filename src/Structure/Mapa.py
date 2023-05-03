class Mapa:

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
            raise Exception("Error con el Formato, {texto}")

    def comprobarFormato(self, lineas):
        size = lineas[0].split()
        matriz = []

        if len(size) != 2:
            self.error("tamaño del mapa.")
        elif len(lineas) != size[0]+1:
            self.error("cantidad de las filas.")
        else:
            for nf in range(1, (size[0]+1) ):
                fila = lineas[nf]
                columnas = file.split()
                if len(columnas) != size[1]:
                    self.error("cantidad de columnas.")
                else:
                    for colum in columnas:
                        matriz.append(int(colum))

        return matriz


    def comprobarInicio(self):
        inicio = False
        for fila in self.__matriz:
            for columna in fila:
                if (columna == 1):
                    inicio = True
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

    pass
