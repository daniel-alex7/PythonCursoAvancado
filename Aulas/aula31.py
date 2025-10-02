"""
Flag (Bandeira) - Marcar um local 
None = Sem valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade do objeto (endereço de memória)
"""
'''
v1 = 'a'
v2 = 'a'
print(id(v1))  # Identidade do objeto v1
print(id(v2))  # Identidade do objeto v2

As duas variáveis apontam para o mesmo valor na memoria 

'''
condicao = False
passou_no_if = None  

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não Faça')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')