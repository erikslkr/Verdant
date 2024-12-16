import ply.lex


tokens = (
    "LITERAL_INT",
    
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "POW",
    
    "ASSIGN",
    
    "LPAREN",
    "RPAREN",
    
    "KW_VAR",
    
    "IDENTIFIER",
)

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_POW = r"\*\*"

t_ASSIGN = "="

t_LPAREN = r"\("
t_RPAREN = r"\)"

t_ignore = " \t"

def t_LITERAL_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    match t.value:
        case "var":
            t.type = "KW_VAR"
    return t

def t_newline(t):
    r"\r?\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def lex(source):
    lexer = ply.lex.lex()
    lexer.input(source)
    return lexer
