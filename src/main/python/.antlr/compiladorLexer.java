// Generated from c:/Users/Usuario/OneDrive/Documents/DHS2025/src/main/python/compilador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class compiladorLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PA=1, PC=2, LLA=3, LLC=4, PYC=5, ASIG=6, COMA=7, SUMA=8, RESTA=9, MULT=10, 
		DIV=11, MOD=12, NUMERO=13, INT=14, DOUBLE=15, IF=16, ELSE=17, FOR=18, 
		WHILE=19, ID=20, WS=21, OTRO=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LETRA", "DIGITO", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", "COMA", "SUMA", 
			"RESTA", "MULT", "DIV", "MOD", "NUMERO", "INT", "DOUBLE", "IF", "ELSE", 
			"FOR", "WHILE", "ID", "WS", "OTRO"
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


	public compiladorLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "compilador.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0016\u0081\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0004\u000eO\b\u000e\u000b\u000e\f\u000eP\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001"+
		"\u0015\u0003\u0015r\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0005"+
		"\u0015w\b\u0015\n\u0015\f\u0015z\t\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0000\u0000\u0018\u0001\u0000"+
		"\u0003\u0000\u0005\u0001\u0007\u0002\t\u0003\u000b\u0004\r\u0005\u000f"+
		"\u0006\u0011\u0007\u0013\b\u0015\t\u0017\n\u0019\u000b\u001b\f\u001d\r"+
		"\u001f\u000e!\u000f#\u0010%\u0011\'\u0012)\u0013+\u0014-\u0015/\u0016"+
		"\u0001\u0000\u0003\u0002\u0000AZaz\u0001\u000009\u0003\u0000\t\n\r\r "+
		" \u0083\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000"+
		"!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001"+
		"\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000"+
		"\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000"+
		"\u0000/\u0001\u0000\u0000\u0000\u00011\u0001\u0000\u0000\u0000\u00033"+
		"\u0001\u0000\u0000\u0000\u00055\u0001\u0000\u0000\u0000\u00077\u0001\u0000"+
		"\u0000\u0000\t9\u0001\u0000\u0000\u0000\u000b;\u0001\u0000\u0000\u0000"+
		"\r=\u0001\u0000\u0000\u0000\u000f?\u0001\u0000\u0000\u0000\u0011A\u0001"+
		"\u0000\u0000\u0000\u0013C\u0001\u0000\u0000\u0000\u0015E\u0001\u0000\u0000"+
		"\u0000\u0017G\u0001\u0000\u0000\u0000\u0019I\u0001\u0000\u0000\u0000\u001b"+
		"K\u0001\u0000\u0000\u0000\u001dN\u0001\u0000\u0000\u0000\u001fR\u0001"+
		"\u0000\u0000\u0000!V\u0001\u0000\u0000\u0000#]\u0001\u0000\u0000\u0000"+
		"%`\u0001\u0000\u0000\u0000\'e\u0001\u0000\u0000\u0000)i\u0001\u0000\u0000"+
		"\u0000+q\u0001\u0000\u0000\u0000-{\u0001\u0000\u0000\u0000/\u007f\u0001"+
		"\u0000\u0000\u000012\u0007\u0000\u0000\u00002\u0002\u0001\u0000\u0000"+
		"\u000034\u0007\u0001\u0000\u00004\u0004\u0001\u0000\u0000\u000056\u0005"+
		"(\u0000\u00006\u0006\u0001\u0000\u0000\u000078\u0005)\u0000\u00008\b\u0001"+
		"\u0000\u0000\u00009:\u0005{\u0000\u0000:\n\u0001\u0000\u0000\u0000;<\u0005"+
		"}\u0000\u0000<\f\u0001\u0000\u0000\u0000=>\u0005;\u0000\u0000>\u000e\u0001"+
		"\u0000\u0000\u0000?@\u0005=\u0000\u0000@\u0010\u0001\u0000\u0000\u0000"+
		"AB\u0005,\u0000\u0000B\u0012\u0001\u0000\u0000\u0000CD\u0005+\u0000\u0000"+
		"D\u0014\u0001\u0000\u0000\u0000EF\u0005-\u0000\u0000F\u0016\u0001\u0000"+
		"\u0000\u0000GH\u0005*\u0000\u0000H\u0018\u0001\u0000\u0000\u0000IJ\u0005"+
		"/\u0000\u0000J\u001a\u0001\u0000\u0000\u0000KL\u0005%\u0000\u0000L\u001c"+
		"\u0001\u0000\u0000\u0000MO\u0003\u0003\u0001\u0000NM\u0001\u0000\u0000"+
		"\u0000OP\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000PQ\u0001\u0000"+
		"\u0000\u0000Q\u001e\u0001\u0000\u0000\u0000RS\u0005i\u0000\u0000ST\u0005"+
		"n\u0000\u0000TU\u0005t\u0000\u0000U \u0001\u0000\u0000\u0000VW\u0005d"+
		"\u0000\u0000WX\u0005o\u0000\u0000XY\u0005u\u0000\u0000YZ\u0005b\u0000"+
		"\u0000Z[\u0005l\u0000\u0000[\\\u0005e\u0000\u0000\\\"\u0001\u0000\u0000"+
		"\u0000]^\u0005i\u0000\u0000^_\u0005f\u0000\u0000_$\u0001\u0000\u0000\u0000"+
		"`a\u0005e\u0000\u0000ab\u0005l\u0000\u0000bc\u0005s\u0000\u0000cd\u0005"+
		"e\u0000\u0000d&\u0001\u0000\u0000\u0000ef\u0005f\u0000\u0000fg\u0005o"+
		"\u0000\u0000gh\u0005r\u0000\u0000h(\u0001\u0000\u0000\u0000ij\u0005w\u0000"+
		"\u0000jk\u0005h\u0000\u0000kl\u0005i\u0000\u0000lm\u0005l\u0000\u0000"+
		"mn\u0005e\u0000\u0000n*\u0001\u0000\u0000\u0000or\u0003\u0001\u0000\u0000"+
		"pr\u0005_\u0000\u0000qo\u0001\u0000\u0000\u0000qp\u0001\u0000\u0000\u0000"+
		"rx\u0001\u0000\u0000\u0000sw\u0003\u0001\u0000\u0000tw\u0003\u0003\u0001"+
		"\u0000uw\u0005_\u0000\u0000vs\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000"+
		"\u0000vu\u0001\u0000\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000"+
		"\u0000\u0000xy\u0001\u0000\u0000\u0000y,\u0001\u0000\u0000\u0000zx\u0001"+
		"\u0000\u0000\u0000{|\u0007\u0002\u0000\u0000|}\u0001\u0000\u0000\u0000"+
		"}~\u0006\u0016\u0000\u0000~.\u0001\u0000\u0000\u0000\u007f\u0080\t\u0000"+
		"\u0000\u0000\u00800\u0001\u0000\u0000\u0000\u0005\u0000Pqvx\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}