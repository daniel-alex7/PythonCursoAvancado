"""
Valores padrão para parâmetros
Ao definir uma gunção, os parâmetros podem
ter valores padrão. Caso o valor não seja enviado 
para o parâmetro, o valor será usado.
Refatorar: editar código
"""
# Quando temos um parametro que pode ou não ser enviado, devemos usar isso
def soma(x,y,z=0):
    if z is not None:
      print(f'{x=} {y=} {z=} ', x + y + z) 
    else:
       print(f'{x=} {y=}', x + y)

soma(1,2)