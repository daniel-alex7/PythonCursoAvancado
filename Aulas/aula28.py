"""
Exercicio 

Peça ao usuário digitar seu nome
Peça ao usuário digitar sua idade
Se a idade e noem forem digitados:
    Exiba:
       Seu nome é {nome}
       Seu nome invertido é {nome invertido}
       Se nome contém (ou não) espaços
       Seu nome tem {n} letras
       A primeira letra do seu nome é {letra}
       A ultima letra do seu nome é {letra}
       Se nada for digitado em nome ou idade,
         exiba "Desculpe, você deixou campos vazios"
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if " " in nome or idade:
    
 print(f'Seu nome é {nome} e sua idade é {idade}')
 print(f'Seu nome invertido é {nome[::-1]}')
 print(f'Seu nome contém espaços? {" " in nome}')
 print(f'Seu nome tem {len(nome)} letras')
 print(f'A primeira letra do seu nome é {nome[0]}')
 print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios")  



