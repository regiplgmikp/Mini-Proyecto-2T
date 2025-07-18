
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CATEGORIA_E CATEGORIA_S DESCRIPCION_E DESCRIPCION_S ID_E ID_S INGREDIENTES_E INGREDIENTES_S INGREDIENTE_E INGREDIENTE_S MARCA_E MARCA_S NOMBRE_E NOMBRE_S PRECIO_E PRECIO_S PRODUCTOS_E PRODUCTOS_S PRODUCTO_E PRODUCTO_S STOCK_E STOCK_S TEXTproductos : PRODUCTOS_S lista_productos PRODUCTOS_Elista_productos : productolista_productos : producto lista_productosproducto : PRODUCTO_S id nombre marca categoria precio stock descripcion ingredientes PRODUCTO_Eid : ID_S TEXT ID_Enombre : NOMBRE_S TEXT NOMBRE_Emarca : MARCA_S TEXT MARCA_Ecategoria : CATEGORIA_S TEXT CATEGORIA_Eprecio : PRECIO_S TEXT PRECIO_Estock : STOCK_S TEXT STOCK_Edescripcion : DESCRIPCION_S TEXT DESCRIPCION_Eingredientes : INGREDIENTES_S lista_ingredientes INGREDIENTES_Elista_ingredientes : INGREDIENTE_S TEXT INGREDIENTE_Elista_ingredientes : INGREDIENTE_S TEXT INGREDIENTE_E lista_ingredientes'
    
_lr_action_items = {'PRODUCTOS_S':([0,],[2,]),'$end':([1,6,],[0,-1,]),'PRODUCTO_S':([2,4,37,],[5,5,-4,]),'PRODUCTOS_E':([3,4,7,37,],[6,-2,-3,-4,]),'ID_S':([5,],[9,]),'NOMBRE_S':([8,16,],[11,-5,]),'TEXT':([9,11,14,18,22,26,30,39,],[12,15,19,23,27,31,35,42,]),'MARCA_S':([10,20,],[14,-6,]),'ID_E':([12,],[16,]),'CATEGORIA_S':([13,24,],[18,-7,]),'NOMBRE_E':([15,],[20,]),'PRECIO_S':([17,28,],[22,-8,]),'MARCA_E':([19,],[24,]),'STOCK_S':([21,32,],[26,-9,]),'CATEGORIA_E':([23,],[28,]),'DESCRIPCION_S':([25,36,],[30,-10,]),'PRECIO_E':([27,],[32,]),'INGREDIENTES_S':([29,40,],[34,-11,]),'STOCK_E':([31,],[36,]),'PRODUCTO_E':([33,41,],[37,-12,]),'INGREDIENTE_S':([34,43,],[39,39,]),'DESCRIPCION_E':([35,],[40,]),'INGREDIENTES_E':([38,43,44,],[41,-13,-14,]),'INGREDIENTE_E':([42,],[43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'productos':([0,],[1,]),'lista_productos':([2,4,],[3,7,]),'producto':([2,4,],[4,4,]),'id':([5,],[8,]),'nombre':([8,],[10,]),'marca':([10,],[13,]),'categoria':([13,],[17,]),'precio':([17,],[21,]),'stock':([21,],[25,]),'descripcion':([25,],[29,]),'ingredientes':([29,],[33,]),'lista_ingredientes':([34,43,],[38,44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> productos","S'",1,None,None,None),
  ('productos -> PRODUCTOS_S lista_productos PRODUCTOS_E','productos',3,'p_productos','archivo_yacc.py',8),
  ('lista_productos -> producto','lista_productos',1,'p_lista_productos_uno','archivo_yacc.py',17),
  ('lista_productos -> producto lista_productos','lista_productos',2,'p_lista_productos_mas','archivo_yacc.py',21),
  ('producto -> PRODUCTO_S id nombre marca categoria precio stock descripcion ingredientes PRODUCTO_E','producto',10,'p_producto','archivo_yacc.py',25),
  ('id -> ID_S TEXT ID_E','id',3,'p_id','archivo_yacc.py',45),
  ('nombre -> NOMBRE_S TEXT NOMBRE_E','nombre',3,'p_nombre','archivo_yacc.py',49),
  ('marca -> MARCA_S TEXT MARCA_E','marca',3,'p_marca','archivo_yacc.py',53),
  ('categoria -> CATEGORIA_S TEXT CATEGORIA_E','categoria',3,'p_categoria','archivo_yacc.py',57),
  ('precio -> PRECIO_S TEXT PRECIO_E','precio',3,'p_precio','archivo_yacc.py',61),
  ('stock -> STOCK_S TEXT STOCK_E','stock',3,'p_stock','archivo_yacc.py',65),
  ('descripcion -> DESCRIPCION_S TEXT DESCRIPCION_E','descripcion',3,'p_descripcion','archivo_yacc.py',69),
  ('ingredientes -> INGREDIENTES_S lista_ingredientes INGREDIENTES_E','ingredientes',3,'p_ingredientes','archivo_yacc.py',73),
  ('lista_ingredientes -> INGREDIENTE_S TEXT INGREDIENTE_E','lista_ingredientes',3,'p_lista_ingredientes_uno','archivo_yacc.py',78),
  ('lista_ingredientes -> INGREDIENTE_S TEXT INGREDIENTE_E lista_ingredientes','lista_ingredientes',4,'p_lista_ingredientes_mas','archivo_yacc.py',83),
]
