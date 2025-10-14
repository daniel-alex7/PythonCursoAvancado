#  Try, except, else e finally

try:
    print('Abir arquivo')
    1 / 0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero')
except IndexError as error:
    print('IndexError')

else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')
