from antlr4 import TerminalNode
from antlr4 import ErrorNode
from compiladorParser import compiladorParser
from compiladorListener import compiladorListener
from TablaSimbolos import *



class Escucha (compiladorListener) :
    indent = 1
    declaracion = 0
    profundidad = 0
    numNodos = 0

    def __init__(self):
        super().__init__()
        self.TS = TS()
        self.tipo_actual=None
        self.cont_errores=0
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        print("Comienza el parsing")

    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        print("Fin del parsing")

    def enterDeclaracion_variable(self, ctx:compiladorParser.Declaracion_variableContext):
        self.declaracion+=1
        self.tipo_actual=ctx.tipo().getText()
    
    def exitDeclaracion_variable(self, ctx:compiladorParser.Declaracion_variableContext):
        tipo=ctx.ID.tipo().getText()
        nombre=ctx.ID().getText()
        
        if self.TS.buscarSimboloContexto(nombre):
            print("ERROR: La variable "+nombre+" ya fue declarada en este contexto")
            self.cont_errores+=1
        else:
            v = Variable(nombre,tipo)
            self.TS.addSimbolo(v)
            print("Se declaro la variable "+ nombre)
        self.tipo_actual=None

    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        self.profundidad-=1
        if ctx.getChildCount() >= 2:
            nombre=ctx.getChild(1).getText()
        
        if self.tipo_actual:
            if self.TS.buscarSimboloContexto(nombre):
                print("ERROR: La variable "+nombre+" ya fue declarada en este contexto")
                self.cont_errores+=1
            else:
                v = Variable(nombre,self.tipo_actual)
                self.TS.addSimbolo(v)
                print("Se declaro la variable "+ nombre)
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

        

    