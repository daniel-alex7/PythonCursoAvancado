"""
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'João', 1, 2, 3, 'Daniel']
tupla = 'Python', 'é', 'legal'


salas = [
    ['Maria', 'Helena', 'Carla'],
    ['Juliana', ],
    ['Daniel', 'Robson' , 'Eduarda',] #(0, 10, 20 ,30 ,40)]
]

# p, b, *_, ap,u = lista
# print(p, ap,u)

# for nome in lista:
#     print(nome, end=' ')

    #ou

# print(*lista)
# print(*string)
# print(* tupla)

print(*salas, sep='\n')