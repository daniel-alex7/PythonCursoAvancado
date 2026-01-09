# fazer, desfazer e refazer tarefa

for i in range(10):
    print('Comandos: digitar,listar, desfazer e refazer')
    tarefa_comando = input('Digite uma tarefa ou comando: ')
    print()


    
    if tarefa_comando == 'listar' and tarefa_comando == '':
        print('NADA A DIGITAR')
        print(lista)
        
        
    
    
        
    def desfazer_tarefas(tarefa, lista=None):
        if lista is None:
            lista = []
            lista.pop(tarefa)
        return lista
        
    if tarefa_comando == 'remover':
        lista = desfazer_tarefas
        print(lista)
    
    
    def adiciona_tarefas(tarefa, lista=None): 
        if lista is None:
            lista = []
            lista.append(tarefa)
        return lista
        
    if tarefa_comando == 'digitar':
        
        print('Digite sua tarefa: ')
        lista = adiciona_tarefas
        print(lista)
        continue
    break
    

    
        








 





   

 





         






