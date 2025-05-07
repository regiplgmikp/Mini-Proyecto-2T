import ply.lex as lex

# Definición de los tokens
tokens = (
    #Productos
    'PRODUCTOS_S', 'PRODUCTOS_E',
    #Producto individual
    'PRODUCTO_S', 'PRODUCTO_E',
    #Atributos del producto
    'ID_S', 'ID_E',
    'NOMBRE_S', 'NOMBRE_E',
    'MARCA_S', 'MARCA_E',
    'CATEGORIA_S', 'CATEGORIA_E',
    'PRECIO_S', 'PRECIO_E',
    'STOCK_S', 'STOCK_E',
    'DESCRIPCION_S', 'DESCRIPCION_E',
    'INGREDIENTES_S', 'INGREDIENTES_E',
    'INGREDIENTE_S', 'INGREDIENTE_E',
    #texto
    'TEXT',
)

# Definir etiquetas para los tokens

t_PRODUCTOS_S = r'<PRODUCTOS>'
t_PRODUCTOS_E = r'</PRODUCTOS>'

t_PRODUCTO_S = r'<PRODUCTO>'
t_PRODUCTO_E = r'</PRODUCTO>'

t_ID_S = r'<ID>'
t_ID_E = r'</ID>'

t_NOMBRE_S = r'<NOMBRE>'
t_NOMBRE_E = r'</NOMBRE>'

t_MARCA_S = r'<MARCA>'
t_MARCA_E = r'</MARCA>'

t_CATEGORIA_S = r'<CATEGORIA>'
t_CATEGORIA_E = r'</CATEGORIA>'

t_PRECIO_S = r'<PRECIO>'
t_PRECIO_E = r'</PRECIO>'

t_STOCK_S = r'<STOCK>'
t_STOCK_E = r'</STOCK>'

t_DESCRIPCION_S = r'<DESCRIPCION>'
t_DESCRIPCION_E = r'</DESCRIPCION>'

t_INGREDIENTES_S = r'<INGREDIENTES>'
t_INGREDIENTES_E = r'</INGREDIENTES>'

t_INGREDIENTE_S = r'<INGREDIENTE>'
t_INGREDIENTE_E = r'</INGREDIENTE>'

# Texto entre etiquetas
t_TEXT =r'[A-ÿ0-9;,\._ ]+'

# Definir una regla para ignorar espacios en blanco y saltos de línea
t_ignore = ' \t\n'

# Definir una regla para manejar errores
def t_error(t):
    print(f"Error de análisis: {t.value[0]}")
    t.lexer.skip(1)

# Realizar validación de prueba antes de pasar a Yacc

input_string = ' '

while input_string !='':
    input_string = input('entrada a validar sintácticamente: ')
    print('Para salir introduce enter----- ')

    if input_string !='':
        lexer.input(input_string)

    for tok in lexer:
        print(tok)