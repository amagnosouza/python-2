# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_da_familia = Carro(modelo="Monza", cor="Azul", ano=1997)

# 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, ativo=False, reputacao=0, momento=""):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.reputação = float
        self.momento = momento
    
    def __str__(self):
        return f"{self.nome} | {self.categoria}"

churrasco_do_jackson = Restaurante(nome="Churrascaria do Jackson",categoria="Carnes",ativo=True,reputacao=4.0,momento="festa")
print(vars(churrasco_do_jackson))

# 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
feijoada_da_maria = Restaurante(nome="Feijoada da Maria",categoria="Refeição")
print(vars(feijoada_da_maria))

# 4- Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
print(feijoada_da_maria)

# 5 -Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, comida_preferida, localizacao):
        self.nome = nome
        self.idade = idade
        self.comida_preferida = comida_preferida
        self.localizacao = localizacao
    def __str__(self):
        return f"{self.nome} | {self.idade} | {self.comida_preferida} | {self.localizacao}"

joao = Cliente(nome="João", idade=18, comida_preferida="sushi", localizacao="BA")
maria = Cliente(nome="Maria", idade=35, comida_preferida="carne", localizacao="GO")
jose = Cliente(nome="Jose", idade=55, comida_preferida="feijoada", localizacao="DF")

print(joao,"\n", maria,"\n", jose)
