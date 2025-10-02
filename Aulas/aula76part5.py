# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
     'nome': 'Daniel Robson',
     'sobrenome': 'Alexandre',
 }

# obtem umaq chave
# print(p1.get('nome'))

# nome = p1.pop('nome')
# print(nome)


# Exclui ultima chave
# ultima_cahve = p1.popitem()
# print(ultima_cahve)
# print(p1)

# # p1.uptade({
# #     'nome' : 'novo valor',
# #     'idade': 20,
# # })
# p1.update(nome='novo valor', idade = 20)

tupla = ('nome', 'novo valor'),('idade',20)
lista = [['nome', 'novo valor'],['idade',20]]
p1.update(lista)
print(p1)
