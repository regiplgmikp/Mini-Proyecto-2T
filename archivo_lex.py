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

t_PRODUCTOS_S = r''
t_PRODUCTOS_E = r''

t_PRODUCTO_S = r''
t_PRODUCTO_E = r''

t_ID_S = r''
t_ID_E = r''

t_NOMBRE_S = r''
t_NOMBRE_E = r''

t_MARCA_S = r''
t_MARCA_E = r''

t_CATEGORIA_S = r''
t_CATEGORIA_E = r''

t_PRECIO_S = r''
t_PRECIO_E = r''

t_STOCK_S = r''
t_STOCK_E = r''

t_DESCRIPCION_S = r''
t_DESCRIPCION_E = r''

t_INGREDIENTES_S = r''
t_INGREDIENTES_E = r''

t_INGREDIENTE_S = r''
t_INGREDIENTE_E = r''

# Texto entre etiquetas
t_TEXT =r''

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