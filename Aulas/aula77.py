#  Exercício - sistema de perguntas respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
# 1. Variável de contagem precisa ser inicializada
# Correção: Inicializei 'qtd_acertos' antes do loop.
qtd_acertos = 0

for pergunta in perguntas:
    # 2. Impressão da pergunta com a chave correta
    # Correção: Removi a concatenação extra 'Pergunta' no print.
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            # 3. Comparação com a RESPOSTA correta
            # Correção: A comparação deve ser com pergunta['Resposta'], e não com pergunta['Pergunta'].
            if opcoes[escolha_int] == pergunta['Resposta']:
                # 4. Atribuição de valor à variável 'acertou'
                # Correção: Usei '=' para atribuir 'True', e não '==' que é usado para comparação.
                acertou = True

    if acertou:
        # ADICIONE ISTO:
        qtd_acertos += 1 
        print('Acertou!')
    else:
        print('Errou!')
print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

