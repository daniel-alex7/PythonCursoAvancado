"""
Argumentos noemados e não nomeados em funções Python
Argumento nomeado tem nome com sinal igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z):
    # Definição
    print(f'{x=} + y={y}  z={z} ','|' ,'x + y + z =', x + y + z)

soma(1, 3, 3) #Não nomeados
# soma(z=3,y=2, x=1) #Nomeados, podem ser passados em qualquer ordem
soma(1,2, z=5)

print(1, 2, 3, sep ='-')