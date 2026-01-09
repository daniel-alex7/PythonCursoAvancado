# # fazer, desfazer e refazer tarefa

# for i in range(3):
#     print('Comandos: listar, desfazer e refazer')
#     tarefa_comando = input('Digite uma tarefa ou comando: ')
#     print()


    
#     if tarefa_comando == 'listar' and tarefa_comando == '':
#         print('NADA A DIGITAR')
#         print(lista)
        
        
        
#     def desfazer_tarefas(tarefa, lista=None):
#         if lista is None:
#             lista = []
#             lista.pop(tarefa)
#         return lista
        
#     if tarefa_comando == 'remover':
#         lista = desfazer_tarefas
#         print(lista)
    
    
    
        
#     if tarefa_comando != 'remover' and 'refazer' and 'listar':
#         def adiciona_tarefas(lista=None): 
#             if lista is None:
#                lista = []
#                lista.append(tarefa_comando)
#                print(lista)
#                print('adicionado')
#             return lista
        
#         tarefa_comando = adiciona_tarefas()
#         print(tarefa_comando)
        
   
    

import os

clear = lambda: os.system('cls')
tarefas = []
tmp = []

for i in range(10):
    decisao = input('listar | desfazer | refazer | clear | sair\n')

    if decisao == 'listar':
        if not tarefas:
            print('Nenhuma tarefa cadastrada.')
        else:
            print('\n'.join('{}: {}'.format(i, t) for i, t in enumerate(tarefas)))

    elif decisao == 'desfazer':
        if not tarefas:
            print('Não há nada para desfazer')
        else:
            tmp.append(tarefas.pop())

    elif decisao == 'refazer':
        if not tmp:
            print('Não há nada para refazer')
        else:
            tarefas.append(tmp.pop())

    elif decisao == 'clear':
        clear()

    elif decisao == 'sair':
        break

    else:
        tarefas.append(decisao)
  








 





   

 





         






