#  Introdução as Generator functions em Python
#  generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return
       
    
    
    # yield 1 # para pausar função em python
    # print('Continuando...')
    # yield 2
    # print('Continuando...')
    # yield 3
    # print('Terminou')
    # return 'Acabou'

gen = generator(maximum=100)
# dinamicamente
for n in gen:
    print(n)