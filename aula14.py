# Utilizando o .format para formatar

a = 'AAAAA'
b = 'BBBBBB'
c = 'CCCCCC'


string = 'b = {nome1:.2f} || a = {nome2:.2f} || c= {nome3:.2f} '

formato = string.format(
     nome1 = a, nome2 = b, nome3 = c ) #São argumentos dentro de format

print(formato)