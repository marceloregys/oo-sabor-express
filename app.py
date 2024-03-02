from modelos.restaurante import Restaurante #Importa a classe restaurante da pasta modelos
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet') # Cria um restaurante
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
#restaurante_japones = Restaurante('Japa', 'Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


'''
Inserindo Notas para avaliação
'''
#restaurante_praca.receber_avaliacao('Gui', 2)
#restaurante_praca.receber_avaliacao('Marcelo', 3)
#restaurante_praca.receber_avaliacao('Tais', 5)

'''
Altera o estado do restaurante praça
'''
restaurante_praca.alternar_estado() 
#restaurante_mexicano.alternar_estado()

def main():
    #Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()