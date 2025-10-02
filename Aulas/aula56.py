"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = "Olha, que coisa"
lista_pala = frase.split()
# lista_frase = frase.split(',')
lista_frase_cruas = frase.split(',')
# print(lista_pala)

lista_frase = []

for i, frase in enumerate(lista_frase_cruas):
    # print(lista_frase[i].strip())
    lista_frase.append(lista_frase_cruas[i].strip()) 

# print(lista_frase)
# print(lista_frase_cruas)
frase_unidas = '-'.join(lista_frase)
print(frase_unidas)
