"""
Closure e funções que retornam outras funções
"""

def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar #Sem o clousure lá embaixo ele retorna lugar na memoria

falar_bom_dia = saudacao("Bom dia")
falar_boa_noite = saudacao("Boa noite")

# Closure -> ele precisa fechar o saudar
# print(s1("Daniel"))
# print(s2("Daniel"))

for nome in ['Maria', 'Joana', 'Carlos']:
    print(falar_bom_dia(nome))
    # print(falar_boa_noite(nome))