# Dictionary Comprehension e Set Comprehension

produto = {
    'nome' : 'Caneta azul',
    'preco' : 2.5,
    'categoria': 'Escritorio'
}



dc = {
   chave: valor.upper()
   if isinstance(valor, str) else valor
#  if isinstance(valor, (int, float)) else valor.upper()
   for chave, valor
   in produto.items()
   if chave == 'categoria' #só vai inclui categoria se queiser o contrario é só usar !=
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c')
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

print(dict(dc)) # faz a mesma coisa

#Set comprehension

s1 = {2 ** i for i in range(10)}
print(s1)

# ou
# print(set(range(10)))