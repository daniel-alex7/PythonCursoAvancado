"""
Formatação de strings
s - string
d - inteiro 
f - float
. <número de dígitos>f - float com n dígitos após o ponto
x ou X - Hexadecimal 
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= força o número aparacer antes do 0
Sinal - + ou -
Ex.: 0>-100,.1f
Coversion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel:>10}')  # Preenche com zeros à esquerda até
print(f'{variavel:<10}')  # Preenche com zeros à direita até
print(f'{variavel:^10}')  # Preenche com zeros ao centro até
print(f'{1000.304954534:0=+10,.1f}') # Preenche com zeros à esquerda, sinal +, 10 caracteres, 1 dígito após a vírgula
print(f'O hexadecimal de 1500 é {1500:08X}') # Preenche com zeros à esquerda, 8 caracteres, em hexadecimal
print(f'{variavel!r}') # Representação oficial da variável

