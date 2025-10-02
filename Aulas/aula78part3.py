# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set

# Métodos úteis:
# add, update, clear, discard

s1 = set()

s1.add('Daniel')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()

s1.discard('Olá mundo')
s1.discard('Daniel')
print(s1)