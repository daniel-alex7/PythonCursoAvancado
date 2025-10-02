"""
Fatiamento de strings 

012345678
Olá Mundo
-987654321

Fatiamento [i:f:p]    [::]
inicio:fim:passo

Obs.: len retorna quantidade de caracteres da string
"""

variavel = 'Olá Mundo'
print(len(variavel))  
print(variavel[4])  # Pega o caractere da posição 4
print(variavel[0:len(variavel):1])  # Pega do 0 ao 8
print(variavel[1:9:3])  #Passo de 3 em 3
print(variavel[::-1])  