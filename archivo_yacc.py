import ply.yacc as yacc
from archivo_lex import tokens

inserts = []

# Regla inicial: <productos> ... </productos>
def p_productos(p):
    'productos : PRODUCTOS_S lista_productos PRODUCTOS_E'
    # Al terminar, guardar los INSERT en un archivo
    with open("insert_productos.txt", "w", encoding="utf-8") as f:
        for ins in inserts:
            f.write(ins + '\n')
    print("Inserts generados y guardados en 'insert_productos.txt'")

# Regla para una lista con un solo producto
def p_lista_productos_uno(p):
    'lista_productos : producto'

# Regla para más de un producto
def p_lista_productos_mas(p):
    'lista_productos : producto lista_productos'

# Estructura completa del producto con campos y anidación
def p_producto(p):
    '''producto : PRODUCTO_S id nombre marca categoria precio stock descripcion ingredientes PRODUCTO_E'''
    producto = {
        "id": p[2],
        "nombre": p[3],
        "marca": p[4],
        "categoria": p[5],
        "precio": p[6],
        "stock": p[7],
        "descripcion": p[8],
        "ingredientes": p[9]
    }

    insert_producto = f"INSERT INTO productos (id, nombre, marca, categoria, precio, stock, descripcion) VALUES ('{producto['id']}', '{producto['nombre']}', '{producto['marca']}', '{producto['categoria']}', {producto['precio']}, {producto['stock']}, '{producto['descripcion']}');"
    inserts.append(insert_producto)

    for ing in producto['ingredientes']:
        insert_ing = f"INSERT INTO ingredientes (producto_id, nombre) VALUES ('{producto['id']}', '{ing}');"
        inserts.append(insert_ing)

def p_id(p):
    'id : ID_S TEXT ID_E'
    p[0] = p[2]

def p_nombre(p):
    'nombre : NOMBRE_S TEXT NOMBRE_E'
    p[0] = p[2]

def p_marca(p):
    'marca : MARCA_S TEXT MARCA_E'
    p[0] = p[2]

def p_categoria(p):
    'categoria : CATEGORIA_S TEXT CATEGORIA_E'
    p[0] = p[2]

def p_precio(p):
    'precio : PRECIO_S TEXT PRECIO_E'
    p[0] = p[2]

def p_stock(p):
    'stock : STOCK_S TEXT STOCK_E'
    p[0] = p[2]

def p_descripcion(p):
    'descripcion : DESCRIPCION_S TEXT DESCRIPCION_E'
    p[0] = p[2]

def p_ingredientes(p):
    'ingredientes : INGREDIENTES_S lista_ingredientes INGREDIENTES_E'
    p[0] = p[2]
    
# Ingredientes: un solo ingrediente
def p_lista_ingredientes_uno(p):
    'lista_ingredientes : INGREDIENTE_S TEXT INGREDIENTE_E'
    p[0] = [p[2]]

# Ingredientes: uno + más
def p_lista_ingredientes_mas(p):
    'lista_ingredientes : INGREDIENTE_S TEXT INGREDIENTE_E lista_ingredientes'
    p[0] = [p[2]] + p[4]

# Error de sintaxisvo
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final del archivo")

# Crear el parser
parser = yacc.yacc()

# Leer XML desde archivo
with open("entrada.xml", "r", encoding="utf-8") as f:
    data = f.read()

# Parsear el contenido
parser.parse(data)
