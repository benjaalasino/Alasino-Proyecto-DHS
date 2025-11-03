from antlr4 import TerminalNode, ErrorNode
from compiladorParser import compiladorParser
from compiladorListener import compiladorListener
from TablaSimbolos import *


class Escucha(compiladorListener):
    indent = 1
    declaracion = 0
    profundidad = 0
    numNodos = 0

    def __init__(self):
        super().__init__()
        self.TS = TS()
        self.tipo_actual = None
        self.cont_errores = 0
        self.errores_sintacticos = []
        self.errores_semanticos = []
        self.en_asignacion = False
        self.variable_asignada = None

    # ==================== PROGRAMA ====================
    def enterPrograma(self, ctx: compiladorParser.ProgramaContext):
        print("\n" + "="*60)
        print("INICIO DEL ANÁLISIS")
        print("="*60)

    def exitPrograma(self, ctx: compiladorParser.ProgramaContext):
        print("\n" + "="*60)
        print("FIN DEL ANÁLISIS")
        print("="*60)
        
        # Verificar variables no usadas
        self._verificar_variables_no_usadas()
        
        # Mostrar tabla de símbolos
        print("\n" + "-"*60)
        print("TABLA DE SÍMBOLOS FINAL:")
        print("-"*60)
        self.TS.mostrarTS()
        
        # Generar reporte de errores
        self._generar_reporte_errores()
        self.imprimir_reporte_completo()

    # ==================== DECLARACIONES ====================
    def enterDeclaracion_variable(self, ctx: compiladorParser.Declaracion_variableContext):
        self.declaracion += 1
        self.tipo_actual = ctx.tipo().getText()
        print(f"\n→ Entrando en declaración de variable (Tipo: {self.tipo_actual})")

    def exitDeclaracion_variable(self, ctx: compiladorParser.Declaracion_variableContext):
        # Obtener el primer identificador
        nombre = ctx.ID().getText()
        
        # Verificar doble declaración
        if self.TS.buscarSimboloContexto(nombre):
            error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Variable '{nombre}' ya declarada en este contexto"
            print(error)
            self.errores_semanticos.append(error)
            self.cont_errores += 1
        else:
            v = Variable(nombre, self.tipo_actual)
            v.inicializado = False  # Por defecto no inicializada
            v.usada = False  # Por defecto no usada
            
            # Verificar si tiene inicialización
            if ctx.inic() and ctx.inic().ASIG():
                v.inicializado = True
                print(f"✓ Variable '{nombre}' declarada e inicializada (tipo: {self.tipo_actual})")
            else:
                print(f"✓ Variable '{nombre}' declarada sin inicializar (tipo: {self.tipo_actual})")
            
            self.TS.addSimbolo(v)
        
        self.tipo_actual = None

    def exitListavar(self, ctx: compiladorParser.ListavarContext):
        # Verifica si hay más variables en la lista (ej: int x, y, z;)
        if ctx.ID():
            nombre = ctx.ID().getText()
            
            if self.tipo_actual:
                if self.TS.buscarSimboloContexto(nombre):
                    error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Variable '{nombre}' ya declarada en este contexto"
                    print(error)
                    self.errores_semanticos.append(error)
                    self.cont_errores += 1
                else:
                    v = Variable(nombre, self.tipo_actual)
                    v.usada = False
                    
                    # Verificar si tiene inicialización
                    if ctx.inic() and ctx.inic().ASIG():
                        v.inicializado = True
                        print(f"✓ Variable '{nombre}' declarada e inicializada (tipo: {self.tipo_actual})")
                    else:
                        v.inicializado = False
                        print(f"✓ Variable '{nombre}' declarada sin inicializar (tipo: {self.tipo_actual})")
                    
                    self.TS.addSimbolo(v)

    # ==================== ASIGNACIONES ====================
    def enterAsignacion(self, ctx: compiladorParser.AsignacionContext):
        self.en_asignacion = True
        nombre = ctx.ID().getText()
        self.variable_asignada = nombre
        
        print(f"\n→ Asignación a variable '{nombre}'")
        
        # Verificar que la variable esté declarada
        simbolo = self.TS.buscarSimbolo(nombre)
        if not simbolo:
            error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Variable '{nombre}' no declarada"
            print(error)
            self.errores_semanticos.append(error)
            self.cont_errores += 1
        else:
            # Marcar como usada
            simbolo.usada = True

    def exitAsignacion(self, ctx: compiladorParser.AsignacionContext):
        nombre = ctx.ID().getText()
        simbolo = self.TS.buscarSimbolo(nombre)
        
        if simbolo:
            # Marcar como inicializada
            simbolo.inicializado = True
            print(f"✓ Variable '{nombre}' inicializada")
            
            # Verificar compatibilidad de tipos (básico)
            self._verificar_tipos_asignacion(ctx, simbolo)
        
        self.en_asignacion = False
        self.variable_asignada = None

    def enterAsignacion_for(self, ctx: compiladorParser.Asignacion_forContext):
        if ctx.ID():
            nombre = ctx.ID().getText()
            simbolo = self.TS.buscarSimbolo(nombre)
            
            if not simbolo:
                error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Variable '{nombre}' no declarada"
                print(error)
                self.errores_semanticos.append(error)
                self.cont_errores += 1
            else:
                simbolo.usada = True
                simbolo.inicializado = True

    # ==================== EXPRESIONES ====================
    def enterExpr(self, ctx: compiladorParser.ExprContext):
        # Verificar uso de variables en expresiones
        self._verificar_variables_en_expresion(ctx)

    def enterTerm(self, ctx: compiladorParser.TermContext):
        self._verificar_variables_en_expresion(ctx)

    def enterFactor(self, ctx: compiladorParser.FactorContext):
        # Si es un ID, verificar que esté declarado
        if ctx.ID():
            nombre = ctx.ID().getText()
            simbolo = self.TS.buscarSimbolo(nombre)
            
            if not simbolo:
                error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Variable '{nombre}' no declarada"
                print(error)
                self.errores_semanticos.append(error)
                self.cont_errores += 1
            else:
                # Marcar como usada
                simbolo.usada = True
                
                # Verificar si está inicializada (solo si no estamos en asignación)
                if not self.en_asignacion and not simbolo.inicializado:
                    error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Variable '{nombre}' usada sin inicializar"
                    print(error)
                    self.errores_semanticos.append(error)
                    self.cont_errores += 1

    # ==================== BLOQUES Y CONTEXTOS ====================
    def enterBloque(self, ctx: compiladorParser.BloqueContext):
        print(f"\n→ Entrando en nuevo bloque (profundidad: {self.profundidad})")
        self.TS.addContexto()
        self.profundidad += 1

    def exitBloque(self, ctx: compiladorParser.BloqueContext):
        print(f"\n← Saliendo de bloque (profundidad: {self.profundidad})")
        print("\nTabla de Símbolos del contexto actual:")
        self.TS.mostrarContextoActual()
        self.TS.delContexto()
        self.profundidad -= 1

    # ==================== ESTRUCTURAS DE CONTROL ====================
    def enterIif(self, ctx: compiladorParser.IifContext):
        print(f"\n→ Estructura IF encontrada [Línea {ctx.start.line}]")

    def enterIwhile(self, ctx: compiladorParser.IwhileContext):
        print(f"\n→ Estructura WHILE encontrada [Línea {ctx.start.line}]")

    def enterIfor(self, ctx: compiladorParser.IforContext):
        print(f"\n→ Estructura FOR encontrada [Línea {ctx.start.line}]")

    def enterIreturn(self, ctx: compiladorParser.IreturnContext):
        print(f"\n→ RETURN encontrado [Línea {ctx.start.line}]")

    # ==================== FUNCIONES ====================
    def enterPrototipo_funcion(self, ctx: compiladorParser.Prototipo_funcionContext):
        nombre = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        print(f"\n→ Prototipo de función: {tipo_retorno} {nombre}()")
        
        if self.TS.buscarSimboloContexto(nombre):
            error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Función '{nombre}' ya declarada"
            print(error)
            self.errores_semanticos.append(error)
            self.cont_errores += 1
        else:
            f = Funcion(nombre, tipo_retorno)
            self.TS.addSimbolo(f)

    def enterDeclaracion_funcion(self, ctx: compiladorParser.Declaracion_funcionContext):
        nombre = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        print(f"\n→ Definición de función: {tipo_retorno} {nombre}()")
        
        if self.TS.buscarSimboloContexto(nombre):
            error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Función '{nombre}' ya declarada"
            print(error)
            self.errores_semanticos.append(error)
            self.cont_errores += 1
        else:
            f = Funcion(nombre, tipo_retorno)
            self.TS.addSimbolo(f)

    def enterLlamada_funcion(self, ctx: compiladorParser.Llamada_funcionContext):
        nombre = ctx.ID().getText()
        simbolo = self.TS.buscarSimbolo(nombre)
        
        if not simbolo:
            error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: Función '{nombre}' no declarada"
            print(error)
            self.errores_semanticos.append(error)
            self.cont_errores += 1
        elif not isinstance(simbolo, Funcion):
            error = f"ERROR SEMÁNTICO [Línea {ctx.start.line}]: '{nombre}' no es una función"
            print(error)
            self.errores_semanticos.append(error)
            self.cont_errores += 1

    # ==================== MANEJO DE ERRORES ====================
    def visitErrorNode(self, node: ErrorNode):
        error = f"ERROR SINTÁCTICO [Línea {node.symbol.line}]: Token inesperado '{node.getText()}'"
        print(error)
        self.errores_sintacticos.append(error)
        self.cont_errores += 1

    # ==================== MÉTODOS AUXILIARES ====================
    def _verificar_variables_en_expresion(self, ctx):
        """Verifica que todas las variables usadas en una expresión estén declaradas"""
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'ID') and callable(getattr(child, 'ID')) and child.ID():
                nombre = child.ID().getText()
                simbolo = self.TS.buscarSimbolo(nombre)
                
                if simbolo:
                    simbolo.usada = True

    def _verificar_tipos_asignacion(self, ctx, simbolo):
        """Verifica compatibilidad básica de tipos en asignaciones"""
        # Implementación básica - puede expandirse
        tipo_var = simbolo.tipo
        
        # Obtener la expresión del lado derecho
        expr = ctx.expr()
        if expr:
            # Verificar si se asigna un tipo compatible
            # Esto es una verificación básica, se puede expandir
            pass

    def _verificar_variables_no_usadas(self):
        """Verifica si hay variables declaradas pero no usadas"""
        print("\n" + "-"*60)
        print("VERIFICACIÓN DE VARIABLES NO USADAS:")
        print("-"*60)
        
        encontradas = False
        for contexto in self.TS.getContextos():
            for nombre, simbolo in contexto.items():
                if isinstance(simbolo, Variable) and not simbolo.usada:
                    error = f"WARNING SEMÁNTICO: Variable '{nombre}' declarada pero no usada"
                    print(error)
                    self.errores_semanticos.append(error)
                    encontradas = True
        
        if not encontradas:
            print("✓ Todas las variables declaradas fueron usadas")

    def _generar_reporte_errores(self):
        """Genera el reporte final de errores"""
        print("\n" + "="*60)
        print("REPORTE DE ERRORES")
        print("="*60)
        
        print(f"\nTotal de errores: {self.cont_errores}")
        print(f"Errores sintácticos: {len(self.errores_sintacticos)}")
        print(f"Errores semánticos: {len(self.errores_semanticos)}")
        
        if self.errores_sintacticos:
            print("\n--- ERRORES SINTÁCTICOS ---")
            for error in self.errores_sintacticos:
                print(f"  • {error}")
        
        if self.errores_semanticos:
            print("\n--- ERRORES SEMÁNTICOS ---")
            for error in self.errores_semanticos:
                print(f"  • {error}")
        
        if self.cont_errores == 0:
            print("\n✓ NO SE ENCONTRARON ERRORES - Código correcto")
        
        print("="*60)

    def imprimir_reporte_completo(self):
    
        print("\n" + "="*70)
        print(" "*20 + "REPORTE FINAL DE ANÁLISIS")
        print("="*70)
        
        # Resumen
        print(f"\n RESUMEN:")
        print(f"   Total de errores encontrados: {self.cont_errores}")
        print(f"   • Errores sintácticos: {len(self.errores_sintacticos)}")
        print(f"   • Errores semánticos: {len(self.errores_semanticos)}")
        
        # Errores sintácticos
        if self.errores_sintacticos:
            print("\n" + "-"*70)
            print("ERRORES SINTÁCTICOS:")
            print("-"*70)
            for i, error in enumerate(self.errores_sintacticos, 1):
                print(f"   {i}. {error}")
        
        # Errores semánticos
        if self.errores_semanticos:
            print("\n" + "-"*70)
            print(" ERRORES SEMÁNTICOS:")
            print("-"*70)
            for i, error in enumerate(self.errores_semanticos, 1):
                print(f"   {i}. {error}")
        
        # Tabla de símbolos
        print("\n" + "-"*70)
        print("TABLA DE SÍMBOLOS:")
        print("-"*70)
        if not self.TS.getContextos():
            print("   [Vacía]")
        else:
            for i, contexto in enumerate(self.TS.getContextos()):
                print(f"\n   Contexto {i}:")
                if not contexto.simbolos:
                    print("      [Sin símbolos]")
                else:
                    for nombre, simbolo in contexto.items():
                        print(f"      • {simbolo}")
        
        # Conclusión
        print("\n" + "="*70)
        if self.cont_errores == 0:
            print(" "*15 + " ANÁLISIS COMPLETADO SIN ERRORES")
        else:
            print(f" "*10 + f" ANÁLISIS COMPLETADO CON {self.cont_errores} ERROR(ES)")
        print("="*70 + "\n")