"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754

"""
import decimal

numero_1 = 0.1
numero_2 = 0.3
numero_3 = numero_1 + numero_2
print(numero_3)

#formatado
print(f'{numero_3:.2f}')

#round -> arredonda casa finais
print(round(numero_3, 3))

#decimal para número flutuantes muito grandes
numero_4 = decimal.Decimal(0.1) 

