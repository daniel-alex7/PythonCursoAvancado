# Problemas de parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None): 
    if lista is None:
        lista = []
    lista.append(nome)
    return lista



# lista1 = []

cliente1 = adiciona_clientes('Daniel')
adiciona_clientes('Carlos', cliente1)
adiciona_clientes('Fernando', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Davi')
adiciona_clientes('Carlota', cliente2)

print(cliente2)