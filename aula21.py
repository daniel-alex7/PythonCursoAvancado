# Operadores lógicos
# and(e) or(ou) not(não)
# and -> todas condições precisam ser verdadeiras
# Se algum valor = false, expressão inteira será avaliada naquele valor
# None é usado para representar um não valor
# #

entrada = input('[E]entrar [S]sair ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito
print(True and False and True)