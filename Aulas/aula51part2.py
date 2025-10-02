"""
Introdução ao desempacotamento + tuples(tuplas)
"""

nomes = ['Maria', 'Helena', 'Luiz']

nome1, nome2, nome3 = nomes
print(nome2)

#*resto ou _

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)