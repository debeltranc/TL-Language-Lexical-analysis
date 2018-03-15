import re
import ply.lex as lex
import sys

tokens = (
		'token_llave_izq',
        'token_llave_der',
        'token_cor_izq',
        'token_cor_der',
        'token_par_izq',
        'token_par_der',
        'token_mayor',
        'token_menor',
        'token_mayor_igual',
        'token_menor_igual',
        'token_igual_num',
        'token_point',
        'token_diff_num',
        'token_and',
        'token_or',
        'token_not',
        'token_mas',
        'token_menos',
        'token_mul',
        'token_div',
        'token_mod',
        'token_pot',
        'token_assign',
        'token_coma',
        'token_dosp',
        'TRUE',
        'FALSE',
        'NIL',
        'IF',
        'ELSE',
        'WHILE',
        'LOG',
        'FOR',
        'IN',
        'FUNCION',
        'END',
        'RETORNO',
        'IMPORTAR',
        'DESDE',
        'TODO',
        'ID',
        'token_float',
        'token_integer',
        'token_string',
        'COMENTARIO'
	)

special_tokens = [
		'token_llave_izq',
		'token_llave_der',
		'token_cor_izq',
		'token_cor_der',
		'token_par_izq',
		'token_par_der',
		'token_mayor',
		'token_menor',
		'token_mayor_igual',
		'token_menor_igual',
		'token_igual_num',
		'token_point',
		'token_diff_num',
		'token_and',
		'token_or',
		'token_not',
		'token_mas',
		'token_menos',
		'token_mul',
		'token_div',
		'token_mod',
		'token_pot',
		'token_assign',
		'token_coma',
		'token_dosp'
	]

#OPERADORES ESPECIALES

def t_token_llave_izq(token):
    r"[\{]"
    token.type = 'token_llave_izq'
    return token

def t_token_llave_der(token):
    r"[\}]"
    token.type = 'token_llave_der'
    return token

def t_token_cor_izq(token):
    r"[\[]"
    token.type = 'token_cor_izq'
    return token

def t_token_cor_der(token):
    r"[\]]"
    token.type = 'token_cor_der'
    return token

def t_token_par_izq(token):
    r"[\(]"
    token.type = 'token_par_izq'
    return token

def t_token_par_der(token):
    r"[\)]"
    token.type = 'token_par_der'
    return token

def t_token_mayor(token):
    r"[>]"
    token.type = 'token_mayor'
    return token

def t_token_menor(token):
    r"[<]"
    token.type = 'token_menor'
    return token

def t_token_mayor_igual(token):
    r"[>][=]"
    token.type = 'token_mayor_igual'
    return token

def t_token_menor_igual(token):
    r"[<][=]"
    token.type = 'token_menor_igual'
    return token

def t_token_igual_num(token):
    r"[=][=]"
    token.type = 'token_igual_num'
    return token

def t_token_point(token):
    r"[\.]"
    token.type = 'token_point'
    return token

def t_token_diff_num(token):
    r"[!][=]"
    token.type = 'token_diff_num'
    return token

def t_token_and(token):
    r"[&][&]"
    token.type = 'token_and'
    return token

def t_token_or(token):
    r"[|][|]"
    token.type = 'token_or'
    return token

def t_token_not(token):
    r"[!]"
    token.type = 'token_not'
    return token

def t_token_mas(token):
    r"[+]"
    token.type = 'token_mas'
    return token

def t_token_menos(token):
    r"[-]"
    token.type = 'token_menos'
    return token

def t_token_mul(token):
    r"[*]"
    token.type = 'token_mul'
    return token

def t_token_div(token):
    r"[/]"
    token.type = 'token_div'
    return token

def t_token_mod(token):
    r"[%]"
    token.type = 'token_mod'
    return token

def t_token_pot(token):
    r"[\^]"
    token.type = 'token_pot'
    return token

def t_token_assign(token):
    r"[=]"
    token.type = 'token_assign'
    return token

def t_token_coma(token):
    r"[,]"
    token.type = 'token_coma'
    return token

def t_token_dosp(token):
    r"[:]"
    token.type = 'token_dosp'
    return token

#PALABRAS RESERVADAS

reserved = {
	"true" : "TRUE",
	"false" : "FALSE",
	"nil" : "NIL",
	"if" : "IF",
	"else" : "ELSE",
	"while" : "WHILE",
	"log" : "LOG",
	"for" : "FOR",
	"in" : "IN",
	"funcion" : "FUNCION",
	"end" : "END",
	"retorno" : "RETORNO",
	"importar" : "IMPORTAR",
	"desde" : "DESDE",
	"todo" : "TODO"
}

#IDENTIFICADORES

def t_token_id(token):
	r"[a-zA-Z_][a-zA-Z_0-9]*"
	token.type = reserved.get(token.value,'ID')
	return token

def t_token_float(token):
    r"[0-9]*[.][0-9]+"
    token.type = 'token_float'
    return token

def t_token_int(token):
    r"[0-9]+"
    token.type = 'token_integer'
    return token

def t_token_string(token):
	r"[\"].*[\"]"
	token.type = 'token_string'
	token.value = token.value.strip('"')
	return token

def t_token_comentario(token):
    r"\#.*"
    token.type = 'COMENTARIO'
    pass

t_ignore = ' \t\v\r' # whitespace

def t_error(t):
	line_start = myTokens.rfind('\n', 0, t.lexpos)
	global error_flag
	error_flag = True
	global error_message
	error_message = str(">>> Error lexico(linea:"+ str(t.lexer.lineno) + ",posicion:" + str(t.lexpos - line_start) + "))")
	t.lexer.skip(1)

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

#MAIN MENU

myTokens = sys.stdin.read()

lexer = lex.lex()

def test_lexer(input_string):
	lexer.input(input_string)
	result = []
	while True:
		tok = lexer.token()
		if not tok: break
		#result = result + [(tok.type,tok.value)]
		#result = result + [tok]
		line_start = input_string.rfind('\n', 0, tok.lexpos)
		if tok.type.lower() == tok.value.lower():
			result += [(tok.value, tok.lineno, tok.lexpos - line_start)]
		elif tok.type in special_tokens:
			result += [(tok.type.lower(), tok.lineno, tok.lexpos - line_start)]
		else:
			result += [(tok.type.lower(), tok.value, tok.lineno, tok.lexpos - line_start)]
	return result

for item in test_lexer(myTokens):
	res = "<"
	for i in item:
		res += str(i) + ","
	res = res[:-1] + ">"
	print(res)
if error_flag:
	print(error_message)
