# Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo
class Musica:
    def __init__(self, nome = "", artista = "", duracao = float):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica_exemplo = Musica(nome = "Exagerado", artista = "Cazuza", duracao=3.2)


print(f"Tocando: {musica_exemplo.nome} - Banda: {musica_exemplo.artista} - tempo: {musica_exemplo.duracao} minutos")

# 1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana"
restaurante_praca.ativo = True

# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante_praca.nome)

# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo == True:
    print("Restaurante Ativo")
else:
    print("Restaurante Inativo")

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = restaurante_praca.categoria
print(categoria)

# 5 - Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = "Bistrô"
print(restaurante_praca.nome)

# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == "Fast Food":
    print("Restaurante é um fast food")
else:
    print("Restaurante não é um fast food")

# 8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(f"Restaurante: {restaurante_praca.nome} | Categoria: {restaurante_praca.categoria}")