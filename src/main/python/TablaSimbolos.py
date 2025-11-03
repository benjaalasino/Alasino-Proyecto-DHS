# TablaSimbolos.py

# Clase base abstracta
class ID:
    def __init__(self, nombre: str, tipoDato: str):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.tipo = tipoDato  # Alias para compatibilidad
        self.inicializado = False
        self.usado = False
        self.usada = False  # Alias para compatibilidad

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
        self.usada = True

    def getUsado(self):
        return self.usado
    
    def __str__(self):
        estado = []
        if self.inicializado:
            estado.append("inicializado")
        if self.usado:
            estado.append("usado")
        estado_str = ", ".join(estado) if estado else "sin inicializar, no usado"
        return f"{self.__class__.__name__} '{self.nombre}' (tipo: {self.tipoDato}, {estado_str})"


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
    
    def items(self):
        """Permite iterar sobre los símbolos del contexto"""
        return self.simbolos.items()
    
    def __len__(self):
        return len(self.simbolos)


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
    
    def mostrarTS(self):
        """Muestra toda la tabla de símbolos de todos los contextos"""
        if not self.contextos:
            print("  [Tabla vacía]")
            return
        
        for i, contexto in enumerate(self.contextos):
            print(f"\n  Contexto {i}:")
            if not contexto.simbolos:
                print("    [Vacío]")
            else:
                for nombre, simbolo in contexto.simbolos.items():
                    print(f"    • {simbolo}")
    
    def mostrarContextoActual(self):
        """Muestra solo el contexto actual (el último)"""
        if not self.contextos:
            print("  [Sin contextos]")
            return
        
        contexto = self.contextos[-1]
        if not contexto.simbolos:
            print("  [Contexto vacío]")
        else:
            for nombre, simbolo in contexto.simbolos.items():
                print(f"  • {simbolo}")

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
    
    def getContextos(self):
        """Retorna la lista de contextos para iterar"""
        return self.contextos
    
    def cantidadContextos(self):
        """Retorna la cantidad de contextos activos"""
        return len(self.contextos)