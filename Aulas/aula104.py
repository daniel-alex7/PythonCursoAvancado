# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são 'Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
    # funcao interna que recebe a analise de parametros
    def interna(*args,**kwarg):
        # checando todos os parametros
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args,**kwarg)
        resultado += ' QUALF '
        print(f'O seu resultado foi  {resultado}')
        print('Decorado')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string ')


invertida = inverte_string('123')
print(invertida)