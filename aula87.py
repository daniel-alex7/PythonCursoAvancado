# isinstace - para saber se objeto é de determinado tipo

lista = [  
    'a', 1, 1.1, True, [0, 1, 2], (1,2),
    {0,1}, {'nome': 'Daniel'},
]

# itens não uniformes.

for item in lista:
    if isinstance(item, set):
        print('Set')
        item.add(5)
        print(item, isinstance(item, set))
        
    #Checar o tipo de um elemento
    elif isinstance(item, str):
        print('STR')
        print(item.upper())
        # print(item.upper(), isinstance(item, set))   
        
        
    # Checa mais de um tipo / numerico
    elif isinstance(item, (int, float)):
        print('Number')
        print(item,item * 2)
        
    else:
        print("Outro")
        print(item)
        
        