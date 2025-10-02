"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai proipor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, você vai conferir se a letra
existe na palavra secreta.
  - Se a letra digitada estiver na palavra secreta, exiba a letra
  - Se a letra não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do usuário.
"""


# for letra in palavra_secreta:
#     letra = input(f'Digite a letra: ')
#     repeticao += 1 

#     if letra in palavra_secreta:
#         print(letra)
#         continue
#     if letra not in palavra_secreta:
#         print('*')


import os

palavra_secreta = 'Jesus'
letras_certas = ''
tentativas = 0
    
while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 2:
        print('Digite apenas uma letra por vez')    
        continue
    
    if letra_digitada.isdigit():
        print('Não digite números')

    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você ganhou PARABÉNS!')
        print('A palavra era: ', palavra_secreta)
        print('Tentativas: ', tentativas)
        letras_certas = ''
        tentativas = 0
    



  

 

    



    

  
  
  

  
    



