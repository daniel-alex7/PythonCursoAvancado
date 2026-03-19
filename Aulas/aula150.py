# Context Manager com função - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
        
    except Exception as e:
        print('Ocrreu erro', e)
    finally:
        print('Fechando o arquivo')
        arquivo.close()

with my_open('Aulas/aula150.txt', 'w') as arquivo:
    arquivo.write('Linha A \n')
    arquivo.write('Linha B \n')
    arquivo.write('Linha C \n')
    print('WITH', arquivo)