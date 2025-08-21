frase = 'O Python é uma liguagem de programação' \
'multiparadgma, '\
'Python foi criado por Guido van Rossum.'

i = 0
mais_vezes = 0
letra_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    cont_letra_atual = frase.count(letra_atual)

    if mais_vezes < cont_letra_atual:
        mais_vezes = cont_letra_atual
        letra_mais = letra_atual

    

print('Letra que apareceu mais vezes foi: '
      f'{letra_mais} que apareceu {mais_vezes}x')

