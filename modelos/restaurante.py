class Restaurante():

    restaurantes = []

    def __init__(self, _nome, categoria):
        self._nome = _nome.title()
        self.categoria = categoria.upper()
        self._ativo = False #_ativo - Não esperamos que seja acionado de forma direta
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Nome do restaurante'.ljust(25) + ' | Categoria'.ljust(25) + '| Status' )
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(21)} | {restaurante.ativo}')

    @property #Pesquisar sobre
    def ativo(self):
        return '⌧' if self._ativo else '☐' #Emoji https://coolsymbol.com/
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

#print(vars(restaurante_praca)) #Ver dicionário vinculado ao atributo 

Restaurante.listar_restaurantes()