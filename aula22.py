# Operadores lógicos
# and(e) or(ou) not(não)
# or -> qualquer condição verdadeira avalidada
# Se algum valor = True, expressão inteira será avaliada naquele valor
# None é usado para representar um não valor
# #

entrada = input('[E]entrar [S]sair ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')



# Avaliação de curto circuito no or
senha = input('Senha: ') or 'Sem senha'
print(senha)