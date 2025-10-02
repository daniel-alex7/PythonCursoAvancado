n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
div_inteira = n1 % n2
potencia = n1 ** n2



print(f'soma: {soma}|sub: {sub}|mul: {multi}|div: {div}' +
      f'div inteira: {div_inteira}|potencia: {potencia}|modulos: {abs(n1)} e {abs(n2)}')