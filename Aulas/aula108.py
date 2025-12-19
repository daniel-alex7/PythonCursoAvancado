# count iterator sem fim, muito similiar ao range, mas sem lugar para acabar

from itertools import count

c1 = count(5, 5) #so podemos passar o start e o step
r1 = range(5, 20, 5)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))
print()

print('count')
for i in c1:
    if i >= 20:
        break
    print(i)
    
    
print()

print('range')
for i in r1:
    print(i)