# Utilizando o .format para formatar

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1


string = 'b = {1} || a = {0} || a = {0} || a = {0} || c= {nome3:.2f} '
formato = string.format(
    nome1 = a, nome2 = b, nome3 = c) #São argumentos dentro de format

print(formato)