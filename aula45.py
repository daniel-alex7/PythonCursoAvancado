"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> entrega o próximo valor do iterador
iter -> entrega seu iterador
"""

# texto = iter('Python') #__iter__()

# print(next(texto)) #__next__()


# for letra in texto
texto = 'Daniel' # iterável

iterador = iter(texto) # iterador 

while True:
    try:
       letra = (next(iterador)) 
       print(letra)
    except StopIteration: #tratando o proprio erro
       break
    