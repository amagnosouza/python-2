class Restaurante:
    restaurantes = []
    # construtor da classe
    def __init__ (self, nome, categoria):
        self._nome = nome.title() # Primeira letra sempre Maiuscula
        self.categoria = categoria.upper() # Toda a palavra Maiuscula
        self._ativo = False
        Restaurante.restaurantes.append(self) # criar um objeto e colocar dentro da lista

    # metodo para exibir no formato de texto
    def __str__(self):
        return f"{self._nome} | {self.categoria}" # usar self para referenciar o objeto

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def alternar_estado(self):
        self._ativo = not self._ativo