"""
Exercicios
Crie funções que duplicam, triplicam e quadruplicam 
numero recebido como parâmetro
"""
# Minha

# def duplicar(duplo):
#     def numero_duplicado(numero):
#          return numero * duplo
#     return numero_duplicado

# def triplicar(triplo):
#     def numero_triplicado(numero):
#          return numero * triplo
#     return numero_triplicado

# def quadruplicar(quadruplo):
#      def numero_quadruplicado(numero):
#           return numero * quadruplo
#      return numero_quadruplicado

# duplicar_2 = duplicar(2)
# triplicado_3 = triplicar(3)
# quadruplicar_4 = quadruplicar(4)

# numero = int(input("Digite um número: ")) 

# print(duplicar_2(numero))
# print(triplicado_3(numero))
# print(quadruplicar_4(numero))

# Correção:

def criar_multiplicador(multiplicador):
     def multiplicar(numero):
          return numero * multiplicador
     return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))