"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
# Utilizando o replace para cpf com pontos e traços

import re
import sys

entrada = input('CPF [746.824.890-70]: ')
cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    '746.824.890-70')

entrada_sequencial = entrada[0] * len(entrada)

if entrada_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

nove_digito = cpf_enviado[:9]
contador_regressivo = 10
resultado_dig1 = 0



for digito_1 in nove_digito:

    resultado_dig1 += int(digito_1) * contador_regressivo
    contador_regressivo -= 1

digito_1 = (resultado_dig1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0



dez_digito = nove_digito + str(digito_1)
contador_regressivo_2 = 11
resultado_digi2 = 0


for digito in dez_digito:
    resultado_dig2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_dig2 * 10 ) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digito}{digito_1}{digito_2}'

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF inválido')