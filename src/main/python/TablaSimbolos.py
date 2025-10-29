# TablaSimbolos.py

# Clase base abstracta
class ID:
    def __init__(self, nombre: str, tipoDato: str):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = False
        self.usado = False

    def getNombre(self):
        return self.nombre

    def getTipoDato(self):
        return self.tipoDato

    def setInicializado(self):
        self.inicializado = True

    def getInicializado(self):
        return self.inicializado

    def setUsado(self):
        self.usado = True

    def getUsado(self):
        return self.usado


# Variable hereda de ID
class Variable(ID):
    def __init__(self, nombre: str, tipoDato: str):
        super().__init__(nombre, tipoDato)
        self.valor = None  # atributo adicional opcional


# Funcion hereda de ID
class Funcion(ID):
    def __init__(self, nombre: str, tipoDato: str):
        super().__init__(nombre, tipoDato)
        self.args = []

    def getListaArgs(self):
        return self.args


# Contexto que contiene símbolos
class Contexto:
    def __init__(self):
        self.simbolos = {}  # dict: nombre -> ID

    def addSimbolo(self, id_obj: ID):
        self.simbolos[id_obj.getNombre()] = id_obj

    def buscarSimbolo(self, nombre: str):
        return self.simbolos.get(nombre, None)


# Tabla de símbolos (singleton)
class TS:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TS, cls).__new__(cls)
            cls._instance.contextos = []
        return cls._instance

    def getTablaSimbolo(self):
        return self
    
    def MostrarTabla(self):
        if not self.TS.contexto:
            print("VACIA")

        for i, contexto in enumerate(self.TS.contextos):
            if contexto.simbolos:
                for nombre, simbolos in contexto.simbolos.items():
                    print(simbolos)
    def addContexto(self):
        self.contextos.append(Contexto())

    def delContexto(self):
        if self.contextos:
            self.contextos.pop()

    def addSimbolo(self, id_obj: ID):
        if self.contextos:
            self.contextos[-1].addSimbolo(id_obj)
        else:
            # Si no hay contexto, creamos uno global
            self.addContexto()
            self.contextos[-1].addSimbolo(id_obj)

    def buscarSimbolo(self, nombre: str):
        # Busca desde el contexto actual hasta el global
        for ctx in reversed(self.contextos):
            simbolo = ctx.buscarSimbolo(nombre)
            if simbolo:
                return simbolo
        return None

    def buscarSimboloContexto(self, nombre: str):
        if self.contextos:
            return self.contextos[-1].buscarSimbolo(nombre)
        return None
