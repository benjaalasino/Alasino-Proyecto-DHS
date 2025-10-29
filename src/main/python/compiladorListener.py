# Generated from c:/Users/Usuario/OneDrive/Documents/GitHub/Proyecto Alasino DHS/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.
class compiladorListener(ParseTreeListener):

    # Enter a parse tree produced by compiladorParser#programa.
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladorParser#programa.
    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladorParser#elemento_programa.
    def enterElemento_programa(self, ctx:compiladorParser.Elemento_programaContext):
        pass

    # Exit a parse tree produced by compiladorParser#elemento_programa.
    def exitElemento_programa(self, ctx:compiladorParser.Elemento_programaContext):
        pass


    # Enter a parse tree produced by compiladorParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#instruccion.
    def enterInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#instruccion.
    def exitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladorParser#bloque.
    def enterBloque(self, ctx:compiladorParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladorParser#bloque.
    def exitBloque(self, ctx:compiladorParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladorParser#iwhile.
    def enterIwhile(self, ctx:compiladorParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladorParser#iwhile.
    def exitIwhile(self, ctx:compiladorParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladorParser#iif.
    def enterIif(self, ctx:compiladorParser.IifContext):
        pass

    # Exit a parse tree produced by compiladorParser#iif.
    def exitIif(self, ctx:compiladorParser.IifContext):
        pass


    # Enter a parse tree produced by compiladorParser#ielse.
    def enterIelse(self, ctx:compiladorParser.IelseContext):
        pass

    # Exit a parse tree produced by compiladorParser#ielse.
    def exitIelse(self, ctx:compiladorParser.IelseContext):
        pass


    # Enter a parse tree produced by compiladorParser#ifor.
    def enterIfor(self, ctx:compiladorParser.IforContext):
        pass

    # Exit a parse tree produced by compiladorParser#ifor.
    def exitIfor(self, ctx:compiladorParser.IforContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion_for.
    def enterDeclaracion_for(self, ctx:compiladorParser.Declaracion_forContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion_for.
    def exitDeclaracion_for(self, ctx:compiladorParser.Declaracion_forContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion_for.
    def enterAsignacion_for(self, ctx:compiladorParser.Asignacion_forContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion_for.
    def exitAsignacion_for(self, ctx:compiladorParser.Asignacion_forContext):
        pass


    # Enter a parse tree produced by compiladorParser#ireturn.
    def enterIreturn(self, ctx:compiladorParser.IreturnContext):
        pass

    # Exit a parse tree produced by compiladorParser#ireturn.
    def exitIreturn(self, ctx:compiladorParser.IreturnContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion_variable.
    def enterDeclaracion_variable(self, ctx:compiladorParser.Declaracion_variableContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion_variable.
    def exitDeclaracion_variable(self, ctx:compiladorParser.Declaracion_variableContext):
        pass


    # Enter a parse tree produced by compiladorParser#inic.
    def enterInic(self, ctx:compiladorParser.InicContext):
        pass

    # Exit a parse tree produced by compiladorParser#inic.
    def exitInic(self, ctx:compiladorParser.InicContext):
        pass


    # Enter a parse tree produced by compiladorParser#listavar.
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        pass

    # Exit a parse tree produced by compiladorParser#listavar.
    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        pass


    # Enter a parse tree produced by compiladorParser#prototipo_funcion.
    def enterPrototipo_funcion(self, ctx:compiladorParser.Prototipo_funcionContext):
        pass

    # Exit a parse tree produced by compiladorParser#prototipo_funcion.
    def exitPrototipo_funcion(self, ctx:compiladorParser.Prototipo_funcionContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:compiladorParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:compiladorParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by compiladorParser#parametros_formales.
    def enterParametros_formales(self, ctx:compiladorParser.Parametros_formalesContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametros_formales.
    def exitParametros_formales(self, ctx:compiladorParser.Parametros_formalesContext):
        pass


    # Enter a parse tree produced by compiladorParser#lista_parametros.
    def enterLista_parametros(self, ctx:compiladorParser.Lista_parametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#lista_parametros.
    def exitLista_parametros(self, ctx:compiladorParser.Lista_parametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#resto_parametros.
    def enterResto_parametros(self, ctx:compiladorParser.Resto_parametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#resto_parametros.
    def exitResto_parametros(self, ctx:compiladorParser.Resto_parametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:compiladorParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by compiladorParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:compiladorParser.Llamada_funcionContext):
        pass


    # Enter a parse tree produced by compiladorParser#parametros_reales.
    def enterParametros_reales(self, ctx:compiladorParser.Parametros_realesContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametros_reales.
    def exitParametros_reales(self, ctx:compiladorParser.Parametros_realesContext):
        pass


    # Enter a parse tree produced by compiladorParser#lista_expresiones.
    def enterLista_expresiones(self, ctx:compiladorParser.Lista_expresionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#lista_expresiones.
    def exitLista_expresiones(self, ctx:compiladorParser.Lista_expresionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#resto_expresiones.
    def enterResto_expresiones(self, ctx:compiladorParser.Resto_expresionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#resto_expresiones.
    def exitResto_expresiones(self, ctx:compiladorParser.Resto_expresionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo.
    def enterTipo(self, ctx:compiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo.
    def exitTipo(self, ctx:compiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr.
    def enterExpr(self, ctx:compiladorParser.ExprContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr.
    def exitExpr(self, ctx:compiladorParser.ExprContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr_rest.
    def enterExpr_rest(self, ctx:compiladorParser.Expr_restContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr_rest.
    def exitExpr_rest(self, ctx:compiladorParser.Expr_restContext):
        pass


    # Enter a parse tree produced by compiladorParser#term.
    def enterTerm(self, ctx:compiladorParser.TermContext):
        pass

    # Exit a parse tree produced by compiladorParser#term.
    def exitTerm(self, ctx:compiladorParser.TermContext):
        pass


    # Enter a parse tree produced by compiladorParser#term_rest.
    def enterTerm_rest(self, ctx:compiladorParser.Term_restContext):
        pass

    # Exit a parse tree produced by compiladorParser#term_rest.
    def exitTerm_rest(self, ctx:compiladorParser.Term_restContext):
        pass


    # Enter a parse tree produced by compiladorParser#factor.
    def enterFactor(self, ctx:compiladorParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladorParser#factor.
    def exitFactor(self, ctx:compiladorParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr_logica.
    def enterExpr_logica(self, ctx:compiladorParser.Expr_logicaContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr_logica.
    def exitExpr_logica(self, ctx:compiladorParser.Expr_logicaContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr_logica_rest.
    def enterExpr_logica_rest(self, ctx:compiladorParser.Expr_logica_restContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr_logica_rest.
    def exitExpr_logica_rest(self, ctx:compiladorParser.Expr_logica_restContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr_and.
    def enterExpr_and(self, ctx:compiladorParser.Expr_andContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr_and.
    def exitExpr_and(self, ctx:compiladorParser.Expr_andContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr_and_rest.
    def enterExpr_and_rest(self, ctx:compiladorParser.Expr_and_restContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr_and_rest.
    def exitExpr_and_rest(self, ctx:compiladorParser.Expr_and_restContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr_comp.
    def enterExpr_comp(self, ctx:compiladorParser.Expr_compContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr_comp.
    def exitExpr_comp(self, ctx:compiladorParser.Expr_compContext):
        pass


    # Enter a parse tree produced by compiladorParser#expr_comp_rest.
    def enterExpr_comp_rest(self, ctx:compiladorParser.Expr_comp_restContext):
        pass

    # Exit a parse tree produced by compiladorParser#expr_comp_rest.
    def exitExpr_comp_rest(self, ctx:compiladorParser.Expr_comp_restContext):
        pass



del compiladorParser