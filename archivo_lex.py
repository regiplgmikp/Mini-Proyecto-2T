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

t_PRODUCTOS_S = r'<productos>'
t_PRODUCTOS_E = r'</productos>'

t_PRODUCTO_S = r'<producto>'
t_PRODUCTO_E = r'</producto>'

t_ID_S = r'<id>'
t_ID_E = r'</id>'

t_NOMBRE_S = r'<nombre>'
t_NOMBRE_E = r'</nombre>'

t_MARCA_S = r'<marca>'
t_MARCA_E = r'</marca>'

t_CATEGORIA_S = r'<categoria>'
t_CATEGORIA_E = r'</categoria>'

t_PRECIO_S = r'<precio>'
t_PRECIO_E = r'</precio>'

t_STOCK_S = r'<stock>'
t_STOCK_E = r'</stock>'

t_DESCRIPCION_S = r'<descripcion>'
t_DESCRIPCION_E = r'</descripcion>'

t_INGREDIENTES_S = r'<ingredientes>'
t_INGREDIENTES_E = r'</ingredientes>'

t_INGREDIENTE_S = r'<ingrediente>'
t_INGREDIENTE_E = r'</ingrediente>'

# Texto entre etiquetas
t_TEXT =r'[A-ÿ0-9;,\._ ]+'

# Definir una regla para ignorar espacios en blanco y saltos de línea
t_ignore = ' \t\n'

# Definir una regla para manejar errores
def t_error(t):
    print(f"Error de análisis: {t.value[0]}")
    t.lexer.skip(1)

# Realizar validación de prueba antes de pasar a Yacc

lexer = lex.lex()

input_string = ' '

while input_string !='':
    input_string = input('entrada a validar sintácticamente: ')
    print('Para salir introduce enter----- ')

    if input_string !='':
        lexer.input(input_string)

    for tok in lexer:
        print(tok)

        