# senha_salva = '123456'
# senha_digitada = ''
# repeticao = 0

# while senha_digitada != senha_salva:
#     senha_digitada = input(f'Sua senha ({repeticao}x): ')

#     repeticao += 1

# print('Aquele laço acima pode ter infinitas repetições')

texto = 'Python'

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
    
print(novo_texto + '*')
