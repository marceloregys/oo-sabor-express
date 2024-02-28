from modelos.avaliacao import Avaliacao

class Restaurante():
    '''Representa um restaurante e suas caracteristicas'''

    restaurantes = []

    def __init__(self, _nome, categoria):
        '''Inicializa uma instancia de restaurante
        input:
        nome: Nome do restaurante
        categoria: Categoria do restaurante
        '''
        self._nome = _nome.title()
        self.categoria = categoria.upper()
        self._ativo = False #_ativo - Não esperamos que seja acionado de forma direta
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna a representação em string do restaurante'''
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista de restaurantes já formatada'''
        print('Nome do restaurante'.ljust(25) + ' | Categoria'.ljust(25) + '|' + 'Avaliação'.ljust(25) + '| Status' )
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(21)} | {str(restaurante.media_avaliacoes).ljust(23)} | {restaurante.ativo}')

    @property #Pesquisar sobre
    def ativo(self):
        '''Retorna um simbolo representando o estado do restaurante'''
        return '⌧' if self._ativo else '☐' #Emoji https://coolsymbol.com/
    
    def alternar_estado(self):
        '''Alterna o estado do restaurante ativado/desativado'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Registra uma avaliação para o restaurante
        input:
        cliente: O nome do cliente que realizou a avaliação
        Nota: Nota dada pelo cliente para o restaurasnte
        '''
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        

    @property
    def media_avaliacoes(self):
        '''
        Calcula e retorna a média de notas do restaurante
        '''
        if not self._avaliacao: # caso o restaurante não possua nota cadastrada retorna '-'
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media