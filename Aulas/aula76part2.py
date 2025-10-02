# Manipulando chaves e valores em dicionario
pessoa = {
    
}

# criar chaves
chave = 'nome'
pessoa['nome'] = 'Daniel Robson'
pessoa['sobrenome'] = 'Alexandre'

# acessar chave
print(pessoa[chave])

# alterar chave
pessoa[chave] = 'Juliana'

# excluir chave
# del pessoa ['sobrenome']
print(pessoa)
print(pessoa['nome'])


#  .get procura alguma chave
if (pessoa.get('sobrenome')) is None:
   print('Não existe')
else:
   print(pessoa['sobrenome'])
