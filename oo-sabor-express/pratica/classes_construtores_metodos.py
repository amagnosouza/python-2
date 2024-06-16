"""
1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

5 - Crie uma instância da classe e imprima o valor da propriedade titular.

6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

7 - Crie um método de classe para a conta ClienteBanco.
"""

class ContaBancaria:
    def __init__(self, titular="", saldo=0.0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"{self.titular}, {self.saldo}"

    @classmethod
    def ativar_conta(cls,conta):
        conta._ativo = True
    
    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def ativo(self):
        return self._ativo

juvenal = ContaBancaria("Juvenal", 100)
rosa = ContaBancaria("Rosa", 90)
print(juvenal)
print(rosa)

chica = ContaBancaria("chica", 200)
print(f"Conta ativa: {chica._ativo}")
ContaBancaria.ativar_conta(chica)
print(f"Conta ativa: {chica._ativo}")

manoel = ContaBancaria("Manoel",500)
print(manoel.titular)

class ClienteBanco:
    def __init__(self, nome, cpf, nascimento, profissao,status):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.profissao = profissao
        self.status = status
    
    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.nascimento}, {self.profissao}, {self.status}"

    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        return conta


pessoa1 = ClienteBanco("Bernardo", 00000000000, "01/01/1991", "Pedreiro", True)
pessoa2 = ClienteBanco("Pedro",11111111111, "02/02/1992", "Empreendedora", False)
pessoa3 = ClienteBanco("Jose", 22222222222, "03/03/1993", "Policial", True)

print(pessoa1)
print(pessoa2)
print(pessoa3)
print()
conta_cliente1 = ClienteBanco.criar_conta("Jaqueline", 1200)
print(conta_cliente1)