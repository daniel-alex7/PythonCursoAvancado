"""
Tipo de tupla - Uma lista imutável
"""
#Como criar? Não coloque os colchetes ou coloque parentes
#Se trona imutável

nomes = 'Maria', 'Helena', 'Luiz'

nomes2 = ('Maria', 'Helena', 'Luiz')

nomesA = ['Maria', 'Helena', 'Luiz']
nomesA = tuple(nomesA)
print(nomes[0])


nomes[1] = 'outro' #vai dar erro 