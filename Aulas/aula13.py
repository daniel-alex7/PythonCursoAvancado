#Formatação de str

nome = 'Daniel'
altura = 1.78
peso = 74

imc = 74 / (altura ** 2)

linha1 = f'{nome}, tem {peso}kg e {altura} de altura. Seu imc é {imc:.2f}'
linha2 = f'pesa {peso}Kg'  

print(linha1)
print(linha2)