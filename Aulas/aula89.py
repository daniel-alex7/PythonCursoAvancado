# dir, hasattr e getattr 
string = 'Daniel'
metodo = 'upper'

if hasattr(string, 'upper'):
    print("Existe upper")
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
