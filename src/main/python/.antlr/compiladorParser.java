// Generated from c:/Users/Usuario/OneDrive/Documents/DHS2025/src/main/python/compilador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class compiladorParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PA=1, PC=2, LLA=3, LLC=4, PYC=5, ASIG=6, COMA=7, SUMA=8, RESTA=9, MULT=10, 
		DIV=11, MOD=12, NUMERO=13, INT=14, DOUBLE=15, IF=16, ELSE=17, FOR=18, 
		WHILE=19, ID=20, WS=21, OTRO=22;
	public static final int
		RULE_programa = 0, RULE_instrucciones = 1, RULE_instruccion = 2, RULE_bloque = 3, 
		RULE_iwhile = 4, RULE_iif = 5, RULE_ielse = 6, RULE_ifor = 7, RULE_declaracion = 8, 
		RULE_listavar = 9, RULE_inic = 10, RULE_tipo = 11, RULE_asignacion = 12, 
		RULE_opal = 13, RULE_exp = 14, RULE_e = 15, RULE_term = 16, RULE_t = 17, 
		RULE_factor = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "instrucciones", "instruccion", "bloque", "iwhile", "iif", 
			"ielse", "ifor", "declaracion", "listavar", "inic", "tipo", "asignacion", 
			"opal", "exp", "e", "term", "t", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "';'", "'='", "','", "'+'", "'-'", 
			"'*'", "'/'", "'%'", null, "'int'", "'double'", "'if'", "'else'", "'for'", 
			"'while'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PA", "PC", "LLA", "LLC", "PYC", "ASIG", "COMA", "SUMA", "RESTA", 
			"MULT", "DIV", "MOD", "NUMERO", "INT", "DOUBLE", "IF", "ELSE", "FOR", 
			"WHILE", "ID", "WS", "OTRO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "compilador.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public compiladorParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode EOF() { return getToken(compiladorParser.EOF, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			instrucciones();
			setState(39);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionesContext extends ParserRuleContext {
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public InstruccionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instrucciones; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterInstrucciones(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitInstrucciones(this);
		}
	}

	public final InstruccionesContext instrucciones() throws RecognitionException {
		InstruccionesContext _localctx = new InstruccionesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instrucciones);
		try {
			setState(45);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LLA:
			case INT:
			case DOUBLE:
			case IF:
			case WHILE:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(41);
				instruccion();
				setState(42);
				instrucciones();
				}
				break;
			case EOF:
			case LLC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public IifContext iif() {
			return getRuleContext(IifContext.class,0);
		}
		public IwhileContext iwhile() {
			return getRuleContext(IwhileContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterInstruccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitInstruccion(this);
		}
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_instruccion);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(47);
				asignacion();
				}
				break;
			case INT:
			case DOUBLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				declaracion();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(49);
				iif();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(50);
				iwhile();
				}
				break;
			case LLA:
				enterOuterAlt(_localctx, 5);
				{
				setState(51);
				bloque();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LLA() { return getToken(compiladorParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladorParser.LLC, 0); }
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterBloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitBloque(this);
		}
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_bloque);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(LLA);
			setState(55);
			instrucciones();
			setState(56);
			match(LLC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IwhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(compiladorParser.WHILE, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IwhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iwhile; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIwhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIwhile(this);
		}
	}

	public final IwhileContext iwhile() throws RecognitionException {
		IwhileContext _localctx = new IwhileContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_iwhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(WHILE);
			setState(59);
			match(PA);
			setState(60);
			opal();
			setState(61);
			match(PC);
			setState(62);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IifContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(compiladorParser.IF, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IelseContext ielse() {
			return getRuleContext(IelseContext.class,0);
		}
		public IifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iif; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIif(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIif(this);
		}
	}

	public final IifContext iif() throws RecognitionException {
		IifContext _localctx = new IifContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_iif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(IF);
			setState(65);
			match(PA);
			setState(66);
			opal();
			setState(67);
			match(PC);
			setState(68);
			instruccion();
			setState(69);
			ielse();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IelseContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(compiladorParser.ELSE, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IelseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ielse; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIelse(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIelse(this);
		}
	}

	public final IelseContext ielse() throws RecognitionException {
		IelseContext _localctx = new IelseContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ielse);
		try {
			setState(74);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				match(ELSE);
				setState(72);
				instruccion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IforContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(compiladorParser.FOR, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public List<TerminalNode> PYC() { return getTokens(compiladorParser.PYC); }
		public TerminalNode PYC(int i) {
			return getToken(compiladorParser.PYC, i);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IforContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIfor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIfor(this);
		}
	}

	public final IforContext ifor() throws RecognitionException {
		IforContext _localctx = new IforContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ifor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(FOR);
			setState(77);
			match(PA);
			setState(78);
			match(PYC);
			setState(79);
			match(PYC);
			setState(80);
			match(PC);
			setState(81);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public InicContext inic() {
			return getRuleContext(InicContext.class,0);
		}
		public ListavarContext listavar() {
			return getRuleContext(ListavarContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladorParser.PYC, 0); }
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterDeclaracion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitDeclaracion(this);
		}
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_declaracion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			tipo();
			setState(84);
			match(ID);
			setState(85);
			inic();
			setState(86);
			listavar();
			setState(87);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListavarContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladorParser.COMA, 0); }
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public InicContext inic() {
			return getRuleContext(InicContext.class,0);
		}
		public ListavarContext listavar() {
			return getRuleContext(ListavarContext.class,0);
		}
		public ListavarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listavar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterListavar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitListavar(this);
		}
	}

	public final ListavarContext listavar() throws RecognitionException {
		ListavarContext _localctx = new ListavarContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_listavar);
		try {
			setState(95);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				match(COMA);
				setState(90);
				match(ID);
				setState(91);
				inic();
				setState(92);
				listavar();
				}
				break;
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InicContext extends ParserRuleContext {
		public TerminalNode ASIG() { return getToken(compiladorParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public InicContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inic; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterInic(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitInic(this);
		}
	}

	public final InicContext inic() throws RecognitionException {
		InicContext _localctx = new InicContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_inic);
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ASIG:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				match(ASIG);
				setState(98);
				opal();
				}
				break;
			case PYC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(compiladorParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(compiladorParser.DOUBLE, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitTipo(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==DOUBLE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(compiladorParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladorParser.PYC, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(ID);
			setState(105);
			match(ASIG);
			setState(106);
			opal();
			setState(107);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpalContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public OpalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterOpal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitOpal(this);
		}
	}

	public final OpalContext opal() throws RecognitionException {
		OpalContext _localctx = new OpalContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_opal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			exp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			term();
			setState(112);
			e();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EContext extends ParserRuleContext {
		public TerminalNode SUMA() { return getToken(compiladorParser.SUMA, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public TerminalNode RESTA() { return getToken(compiladorParser.RESTA, 0); }
		public EContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterE(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitE(this);
		}
	}

	public final EContext e() throws RecognitionException {
		EContext _localctx = new EContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_e);
		try {
			setState(123);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(114);
				match(SUMA);
				setState(115);
				term();
				setState(116);
				e();
				}
				break;
			case RESTA:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				match(RESTA);
				setState(119);
				term();
				setState(120);
				e();
				}
				break;
			case PC:
			case PYC:
			case COMA:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			factor();
			setState(126);
			t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TContext extends ParserRuleContext {
		public TerminalNode MULT() { return getToken(compiladorParser.MULT, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TerminalNode DIV() { return getToken(compiladorParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(compiladorParser.MOD, 0); }
		public TContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_t; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterT(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitT(this);
		}
	}

	public final TContext t() throws RecognitionException {
		TContext _localctx = new TContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_t);
		try {
			setState(141);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MULT:
				enterOuterAlt(_localctx, 1);
				{
				setState(128);
				match(MULT);
				setState(129);
				factor();
				setState(130);
				t();
				}
				break;
			case DIV:
				enterOuterAlt(_localctx, 2);
				{
				setState(132);
				match(DIV);
				setState(133);
				factor();
				setState(134);
				t();
				}
				break;
			case MOD:
				enterOuterAlt(_localctx, 3);
				{
				setState(136);
				match(MOD);
				setState(137);
				factor();
				setState(138);
				t();
				}
				break;
			case PC:
			case PYC:
			case COMA:
			case SUMA:
			case RESTA:
				enterOuterAlt(_localctx, 4);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode NUMERO() { return getToken(compiladorParser.NUMERO, 0); }
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_factor);
		try {
			setState(149);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMERO:
				enterOuterAlt(_localctx, 1);
				{
				setState(143);
				match(NUMERO);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(144);
				match(ID);
				}
				break;
			case PA:
				enterOuterAlt(_localctx, 3);
				{
				setState(145);
				match(PA);
				setState(146);
				exp();
				setState(147);
				match(PC);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0016\u0098\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0003\u0001.\b\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u00025\b\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006K\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\t`\b\t\u0001\n\u0001\n\u0001\n\u0003\ne\b\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f|\b\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u008e\b\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0003\u0012\u0096\b\u0012\u0001\u0012\u0000\u0000\u0013\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$\u0000\u0001\u0001\u0000\u000e\u000f\u0093\u0000&\u0001\u0000\u0000\u0000"+
		"\u0002-\u0001\u0000\u0000\u0000\u00044\u0001\u0000\u0000\u0000\u00066"+
		"\u0001\u0000\u0000\u0000\b:\u0001\u0000\u0000\u0000\n@\u0001\u0000\u0000"+
		"\u0000\fJ\u0001\u0000\u0000\u0000\u000eL\u0001\u0000\u0000\u0000\u0010"+
		"S\u0001\u0000\u0000\u0000\u0012_\u0001\u0000\u0000\u0000\u0014d\u0001"+
		"\u0000\u0000\u0000\u0016f\u0001\u0000\u0000\u0000\u0018h\u0001\u0000\u0000"+
		"\u0000\u001am\u0001\u0000\u0000\u0000\u001co\u0001\u0000\u0000\u0000\u001e"+
		"{\u0001\u0000\u0000\u0000 }\u0001\u0000\u0000\u0000\"\u008d\u0001\u0000"+
		"\u0000\u0000$\u0095\u0001\u0000\u0000\u0000&\'\u0003\u0002\u0001\u0000"+
		"\'(\u0005\u0000\u0000\u0001(\u0001\u0001\u0000\u0000\u0000)*\u0003\u0004"+
		"\u0002\u0000*+\u0003\u0002\u0001\u0000+.\u0001\u0000\u0000\u0000,.\u0001"+
		"\u0000\u0000\u0000-)\u0001\u0000\u0000\u0000-,\u0001\u0000\u0000\u0000"+
		".\u0003\u0001\u0000\u0000\u0000/5\u0003\u0018\f\u000005\u0003\u0010\b"+
		"\u000015\u0003\n\u0005\u000025\u0003\b\u0004\u000035\u0003\u0006\u0003"+
		"\u00004/\u0001\u0000\u0000\u000040\u0001\u0000\u0000\u000041\u0001\u0000"+
		"\u0000\u000042\u0001\u0000\u0000\u000043\u0001\u0000\u0000\u00005\u0005"+
		"\u0001\u0000\u0000\u000067\u0005\u0003\u0000\u000078\u0003\u0002\u0001"+
		"\u000089\u0005\u0004\u0000\u00009\u0007\u0001\u0000\u0000\u0000:;\u0005"+
		"\u0013\u0000\u0000;<\u0005\u0001\u0000\u0000<=\u0003\u001a\r\u0000=>\u0005"+
		"\u0002\u0000\u0000>?\u0003\u0004\u0002\u0000?\t\u0001\u0000\u0000\u0000"+
		"@A\u0005\u0010\u0000\u0000AB\u0005\u0001\u0000\u0000BC\u0003\u001a\r\u0000"+
		"CD\u0005\u0002\u0000\u0000DE\u0003\u0004\u0002\u0000EF\u0003\f\u0006\u0000"+
		"F\u000b\u0001\u0000\u0000\u0000GH\u0005\u0011\u0000\u0000HK\u0003\u0004"+
		"\u0002\u0000IK\u0001\u0000\u0000\u0000JG\u0001\u0000\u0000\u0000JI\u0001"+
		"\u0000\u0000\u0000K\r\u0001\u0000\u0000\u0000LM\u0005\u0012\u0000\u0000"+
		"MN\u0005\u0001\u0000\u0000NO\u0005\u0005\u0000\u0000OP\u0005\u0005\u0000"+
		"\u0000PQ\u0005\u0002\u0000\u0000QR\u0003\u0004\u0002\u0000R\u000f\u0001"+
		"\u0000\u0000\u0000ST\u0003\u0016\u000b\u0000TU\u0005\u0014\u0000\u0000"+
		"UV\u0003\u0014\n\u0000VW\u0003\u0012\t\u0000WX\u0005\u0005\u0000\u0000"+
		"X\u0011\u0001\u0000\u0000\u0000YZ\u0005\u0007\u0000\u0000Z[\u0005\u0014"+
		"\u0000\u0000[\\\u0003\u0014\n\u0000\\]\u0003\u0012\t\u0000]`\u0001\u0000"+
		"\u0000\u0000^`\u0001\u0000\u0000\u0000_Y\u0001\u0000\u0000\u0000_^\u0001"+
		"\u0000\u0000\u0000`\u0013\u0001\u0000\u0000\u0000ab\u0005\u0006\u0000"+
		"\u0000be\u0003\u001a\r\u0000ce\u0001\u0000\u0000\u0000da\u0001\u0000\u0000"+
		"\u0000dc\u0001\u0000\u0000\u0000e\u0015\u0001\u0000\u0000\u0000fg\u0007"+
		"\u0000\u0000\u0000g\u0017\u0001\u0000\u0000\u0000hi\u0005\u0014\u0000"+
		"\u0000ij\u0005\u0006\u0000\u0000jk\u0003\u001a\r\u0000kl\u0005\u0005\u0000"+
		"\u0000l\u0019\u0001\u0000\u0000\u0000mn\u0003\u001c\u000e\u0000n\u001b"+
		"\u0001\u0000\u0000\u0000op\u0003 \u0010\u0000pq\u0003\u001e\u000f\u0000"+
		"q\u001d\u0001\u0000\u0000\u0000rs\u0005\b\u0000\u0000st\u0003 \u0010\u0000"+
		"tu\u0003\u001e\u000f\u0000u|\u0001\u0000\u0000\u0000vw\u0005\t\u0000\u0000"+
		"wx\u0003 \u0010\u0000xy\u0003\u001e\u000f\u0000y|\u0001\u0000\u0000\u0000"+
		"z|\u0001\u0000\u0000\u0000{r\u0001\u0000\u0000\u0000{v\u0001\u0000\u0000"+
		"\u0000{z\u0001\u0000\u0000\u0000|\u001f\u0001\u0000\u0000\u0000}~\u0003"+
		"$\u0012\u0000~\u007f\u0003\"\u0011\u0000\u007f!\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0005\n\u0000\u0000\u0081\u0082\u0003$\u0012\u0000\u0082"+
		"\u0083\u0003\"\u0011\u0000\u0083\u008e\u0001\u0000\u0000\u0000\u0084\u0085"+
		"\u0005\u000b\u0000\u0000\u0085\u0086\u0003$\u0012\u0000\u0086\u0087\u0003"+
		"\"\u0011\u0000\u0087\u008e\u0001\u0000\u0000\u0000\u0088\u0089\u0005\f"+
		"\u0000\u0000\u0089\u008a\u0003$\u0012\u0000\u008a\u008b\u0003\"\u0011"+
		"\u0000\u008b\u008e\u0001\u0000\u0000\u0000\u008c\u008e\u0001\u0000\u0000"+
		"\u0000\u008d\u0080\u0001\u0000\u0000\u0000\u008d\u0084\u0001\u0000\u0000"+
		"\u0000\u008d\u0088\u0001\u0000\u0000\u0000\u008d\u008c\u0001\u0000\u0000"+
		"\u0000\u008e#\u0001\u0000\u0000\u0000\u008f\u0096\u0005\r\u0000\u0000"+
		"\u0090\u0096\u0005\u0014\u0000\u0000\u0091\u0092\u0005\u0001\u0000\u0000"+
		"\u0092\u0093\u0003\u001c\u000e\u0000\u0093\u0094\u0005\u0002\u0000\u0000"+
		"\u0094\u0096\u0001\u0000\u0000\u0000\u0095\u008f\u0001\u0000\u0000\u0000"+
		"\u0095\u0090\u0001\u0000\u0000\u0000\u0095\u0091\u0001\u0000\u0000\u0000"+
		"\u0096%\u0001\u0000\u0000\u0000\b-4J_d{\u008d\u0095";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}