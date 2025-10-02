"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
      append - Adiciona item no final
      insert - Adiciona um item no índice escolhido
      pop - Remove do final ou do índice escolhido
      del - apaga um índice
      clear - limpa a lista
      extend - estende a lsita
      + - concatena lsitas
Create Read Uptade Delete
Criar Ler Alterar apagar = lista[i] (CRUD)

"""

lista = [10, 20, 30, 40]

# Adiciona item no final
lista.append(70)
print(lista)


# Remove ultimo item
nome = lista.pop()
print(lista)

# Deleta
del lista[-1]
print(lista)

# Limpa lista
# lista.clear()
# print(lista)

# Inserindo nos índices

lista.insert(0, 65)
print(lista)