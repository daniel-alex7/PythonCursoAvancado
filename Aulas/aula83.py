#Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

# print(a, b)


# a, b = pessoa.values()
# print(a, b)

# a, b = pessoa
# print(a, b)

# a, b = pessoa.items()
# print(a, b)


# (a1, a2), (b1, b2)= pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(valor)


pessoa = {
    'nome' : 'Juliana',
    'sobrenome' : 'Bellomo',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# como juntar os dois?
pessoa_completa = {**pessoa,**dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# args (já vimos) - não nomeados
# kwargs = keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Daniel', qlq=123)
mostro_argumentos_nomeados(**pessoa_completa) #desempacotar chamada de função com argumentos


configu = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
}

mostro_argumentos_nomeados(**configu)