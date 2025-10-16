# from sys import path

# import aula99_package # 1

# from aula99_package.modulo import soma # 2

# from aula99_package.modulo import modulo # 3

# # from aula99_package.modulo import * Má pratica de código

# # print(*path, sep ='\n')

# print(soma(1, 2)) # 1 
# print(aula99_package.modulo.soma(1, 5))  #2 muito grande
# print(modulo.soma(1, 5))  #3 grande

# Part 2 da aula

# from aula99_package.modulo import soma, fala_oi

# print(__name__)
# fala_oi()


# Parte 3
from aula99_package import soma, fala_oi

print(soma(2,3))
fala_oi()