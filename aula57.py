"""
Lista de listas e seus índices
"""

salas = [
    ['Maria', 'Helena', 'Carla'],
    ['Juliana', ],
    ['Daniel', 'Robson' , 'Eduarda',] #(0, 10, 20 ,30 ,40)]
]

# print(salas [0][1]) #Helena
# print(salas [2][2]) #Alexandre
# print(salas [2][3][2]) #Acessando lista dentro de lista

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
