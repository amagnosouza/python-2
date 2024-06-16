"""
Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.

Adicione um método especial __str__ para imprimir uma representação em string da pessoa.

Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.

Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada
com base na profissão da pessoa.
"""

class Pessoa:
    def __init__ (self, nome="", idade=0, profissao=""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'"{self.nome}, {self.idade}, {self.profissao}"'

    def aniversario(self):
        self.idade += 1

    @property
    def msg(self):
        if self.profissao:
            return f'"Meu nome é {self.nome}, tenho {self.idade} anos" e trabalho como {self.profissao}'
        else:
            return f"Olá, me chamo {self.nome}"

juvenal = Pessoa("Juvenal", 35, "Bicheiro")
rosa = Pessoa("Rosa", 30, "Vendedora")
chica = Pessoa("Chica", 45, "Pasteleira")
manoel = Pessoa("Manoel", 42)

print("Pessoas:")
print(juvenal)
print(rosa)
print(chica)
print(manoel)
print("-" * 30)

# add aniversario +1
chica.aniversario()
rosa.aniversario()

print("Informações após aniversário:")
print(chica)
print(rosa)
print("-" * 30)
print()

print(juvenal.msg)
print(rosa.msg)
print(chica.msg)
print(manoel.msg)