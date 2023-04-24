from concurrent.futures import ThreadPoolExecutor

class Hilos(ThreadPoolExecutor):

    #Limita cuantos hilos se crearan como maximo
    def __init__(self, max_hilos):
        super().__init__(max_hilos)
        pass

    #recibe la funcion seguido de los parametros que necesite
    def usarHilo(self, funcion, **parametros):
        self.submit(funcion, **parametros)
        pass

    pass
