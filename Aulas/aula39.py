"""
Iterando strings com while
"""

nome = 'Daniel Robson'



indice = 0
novo_nome = '' # variveis vazias que tem valores acumulados durante while

while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
    
    
