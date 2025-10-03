# Use um while para pedir senhas até que o usuário digite "1234"

senha = int(input("Digite uma senha com 4 digitios: "))

senha_correta = 1234

while senha != senha_correta:
        print('Tente novamente')
        senha = int(input("Digite novamente: "))
        
if senha == senha_correta:
    print("Acesso liberado")
    
    
    
    
        
