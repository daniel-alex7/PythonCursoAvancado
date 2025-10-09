#  Yield from

def gen1():
    print('Começou gen 1')
    yield 1
    yield 2
    yield 3
    
    
def gen3():
    print('Começou gen 3')
    yield 6
    yield 7
    
def gen2(gen=None):
    print('Começou gen 2')
    if gen is None:
      yield from gen
    yield 4
    yield 5
    

    
g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
    
for numero in g2:
    print(numero)
    
for numero in g3:
    print(numero)
print()