# groupby - agrupamento valores (itertools)

from itertools import groupby
alunos = [
    {'nome': 'Daniel', 'nota' : 'A'},
    {'nome': 'Danilo', 'nota' : 'B'},
    {'nome': 'Daniela', 'nota' : 'A'},
    {'nome': 'Davi', 'nota' : 'C'},
    {'nome': 'Fernando', 'nota' : 'A'},
    {'nome': 'Carlos', 'nota' : 'C'},
    {'nome': 'Daniel R', 'nota' : 'A'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)


for chave,grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)