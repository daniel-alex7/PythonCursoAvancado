import random
import sys

# Cria 100 CPF's aleatórios

for _ in range(100):
    nove_digito = ''
    for i in range(9):
        nove_digito += str(random.randint(0, 9))


    contador_regressivo = 10

    resultado_dig1 = 0

    for digito_1 in nove_digito:

        resultado_dig1 += int(digito_1) * contador_regressivo
        contador_regressivo -= 1

    digito_1 = (resultado_dig1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0



    dez_digito = nove_digito + str(digito_1)
    contador_regressivo_2 = 11

    resultado_dig2 = 0

    for digito in dez_digito:
        resultado_dig2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_dig2 * 10 ) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digito}{digito_1}{digito_2}'

    print(cpf_gerado)