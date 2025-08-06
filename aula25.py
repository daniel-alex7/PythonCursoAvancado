"""
Intepolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Daniel'
preco = 1000.958
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)

print(variavel)

print('O hexadecimal de %d é %04x' % (1500, 1500))