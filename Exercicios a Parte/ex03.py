palavra = input("Digite uma palavra: ")

print(f'A palavra {palavra} tem {len(palavra)} caracter')
print(f'Seus primeiros 3 são {palavra[0:3]}')
print(f'E ela invertida é {palavra[::-1]}')