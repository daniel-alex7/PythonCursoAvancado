
"""
Reptições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira. 

Loop infinito -> Quando um código não tem fim

"""
contador = 0 


while contador <= 100:
    contador += 1 #linha que incrementa o contador, mais importante do while

# pulou o 6
    if contador == 6:
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostraro o', contador)
        continue

    print(contador) 

    if contador == 40:
        break

print('Acabou')