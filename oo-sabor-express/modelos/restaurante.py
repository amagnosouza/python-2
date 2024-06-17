from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    # construtor da classe
    def __init__ (self, nome, categoria):
        self._nome = nome.title() # Primeira letra sempre Maiuscula
        self.categoria = categoria.upper() # Toda a palavra Maiuscula
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # criar um objeto e colocar dentro da lista

    # metodo para exibir no formato de texto
    def __str__(self):
        return f"{self._nome} | {self.categoria}" # usar self para referenciar o objeto

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao) # adiciona a avaliação na lista

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas, 1) # arredonda usando 1 casa decimal
        return media