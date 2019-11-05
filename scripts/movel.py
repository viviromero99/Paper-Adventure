from PPlay.sprite import *

# Como plataformas e itens têm comportamentos muito semelhantes,
# essa classe reune os comportamentos em comum entre os dois.
# Serve como uma base para as classes Plataforma e Item
class Movel(Sprite):

    # Objeto da main
    janela = None

    # Variavel de velocidade
    x_vel = 0

    # Inicializa a classe
    def __init__(self, img_file):
        Sprite.__init__(self, img_file)

    # Controle de colisão
    def colisao(self, obj):
        if obj.x - self.width <= self.x <= obj.x + obj.width:
            if (self.y <= obj.y + obj.height <= self.y + self.height + obj.height):
                return True
        else:
            return False

# Herda as funções da classe Movel
class Item(Movel):

    def __init__(self, img_file, x, y, plataforma):
        Movel.__init__(self, img_file)
        self.set_position(x, y - self.height)
        self.plataforma = plataforma


    def mover(self):
        self.x -= Movel.x_vel * Movel.janela.delta_time()
        self.y += self.plataforma.y_vel * Movel.janela.delta_time()
