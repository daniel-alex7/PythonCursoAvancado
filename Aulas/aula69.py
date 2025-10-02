"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma váriavel do escopo externo
ser a mesma no escopo interno
"""


x = 1
def escopo():
    # #mexe no x de fora das funções
    x = 12
    
    def outra_fun():
        # global x
        x = 10
        y = 2
        print(x, y)

    outra_fun()
    # print(x)

# print(x)
escopo()