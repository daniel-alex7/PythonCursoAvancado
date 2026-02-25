# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base calss, parent class
# Classe filhas (Cliente)
#   -> sub class, child class, derived class


# class MinhaString(str):
#     def upper(self):
#         print('Chamou upper')
#         retorno = super(MinhaString, self).upper()
#         print('Depois do upper')
#         return retorno
    
# string = MinhaString('Daniel')
# print(string.upper())

class A:
    atributo_a = 'valor a'
    
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo(self):
        print('A')
        
        
class B(A):
    atributo_b = 'valor b '
    
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('B')
        
        
class C(B):
    atributo_c = 'valor c '
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('Burlamos o sistema')
    
    
    def metodo(self):
        # super().metodo()
        # super(C, self).metodo()
        # super(A, self).metodo() é igaul a.... proxima linha
        A.metodo(self)
        B.metodo(self)
        print('C')
        
        
        
# print(C.mro())     
# print(B.mro())   
# print(A.mro())
  
c = C('atributo', 'outra coisa')
print(c.atributo)
print(c.outra_coisa)

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()

