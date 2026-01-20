# __dict__ e vars para atributos de instâncias

class Pessoa:
    ano_atual = 2026
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

    
dados = {'nome': 'Daniel', 'idade': 21}
p1 = Pessoa(**dados)



# p1 = Pessoa('Daniel', 21)


# p1.__dict__['outra'] = 'coisa'
# print(p1.outra) #p1 agora tem outra: coisa dentro dele

# print(p1.__dict__)

print(vars(p1))
print(p1.nome)