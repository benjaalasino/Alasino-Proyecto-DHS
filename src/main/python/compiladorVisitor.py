# Generated from c:/Users/Usuario/OneDrive/Documents/GitHub/Proyecto Alasino DHS/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete generic visitor for a parse tree produced by compiladorParser.

class compiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladorParser#programa.
    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#elemento_programa.
    def visitElemento_programa(self, ctx:compiladorParser.Elemento_programaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instruccion.
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#bloque.
    def visitBloque(self, ctx:compiladorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iwhile.
    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iif.
    def visitIif(self, ctx:compiladorParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ielse.
    def visitIelse(self, ctx:compiladorParser.IelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ifor.
    def visitIfor(self, ctx:compiladorParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion_for.
    def visitDeclaracion_for(self, ctx:compiladorParser.Declaracion_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion_for.
    def visitAsignacion_for(self, ctx:compiladorParser.Asignacion_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ireturn.
    def visitIreturn(self, ctx:compiladorParser.IreturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion_variable.
    def visitDeclaracion_variable(self, ctx:compiladorParser.Declaracion_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#inic.
    def visitInic(self, ctx:compiladorParser.InicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listavar.
    def visitListavar(self, ctx:compiladorParser.ListavarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#prototipo_funcion.
    def visitPrototipo_funcion(self, ctx:compiladorParser.Prototipo_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion_funcion.
    def visitDeclaracion_funcion(self, ctx:compiladorParser.Declaracion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametros_formales.
    def visitParametros_formales(self, ctx:compiladorParser.Parametros_formalesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#lista_parametros.
    def visitLista_parametros(self, ctx:compiladorParser.Lista_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#resto_parametros.
    def visitResto_parametros(self, ctx:compiladorParser.Resto_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:compiladorParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametros_reales.
    def visitParametros_reales(self, ctx:compiladorParser.Parametros_realesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#lista_expresiones.
    def visitLista_expresiones(self, ctx:compiladorParser.Lista_expresionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#resto_expresiones.
    def visitResto_expresiones(self, ctx:compiladorParser.Resto_expresionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo.
    def visitTipo(self, ctx:compiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr.
    def visitExpr(self, ctx:compiladorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr_rest.
    def visitExpr_rest(self, ctx:compiladorParser.Expr_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#term.
    def visitTerm(self, ctx:compiladorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#term_rest.
    def visitTerm_rest(self, ctx:compiladorParser.Term_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#factor.
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr_logica.
    def visitExpr_logica(self, ctx:compiladorParser.Expr_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr_logica_rest.
    def visitExpr_logica_rest(self, ctx:compiladorParser.Expr_logica_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr_and.
    def visitExpr_and(self, ctx:compiladorParser.Expr_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr_and_rest.
    def visitExpr_and_rest(self, ctx:compiladorParser.Expr_and_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr_comp.
    def visitExpr_comp(self, ctx:compiladorParser.Expr_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expr_comp_rest.
    def visitExpr_comp_rest(self, ctx:compiladorParser.Expr_comp_restContext):
        return self.visitChildren(ctx)



del compiladorParser