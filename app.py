from modelos.restaurante import Restaurante #Importa a classe restaurante da pasta modelos

restaurante_praca = Restaurante('praça', 'Gourmet') # Cria um restaurante
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

'''
Inserindo Notas para avaliação
'''
restaurante_praca.receber_avaliacao('Gui', 2)
restaurante_praca.receber_avaliacao('Marcelo', 3)
restaurante_praca.receber_avaliacao('Tais', 5)

'''
Altera o estado do restaurante praça
'''
restaurante_praca.alternar_estado() 
restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()