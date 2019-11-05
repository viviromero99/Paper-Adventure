from PPlay.sprite import *
from movel import *

class HUD():
    # Objetos da main
    janela = None

    # Variaveis acessadas fora da classe
    count_lapis = count_dist = timer = 0

    # Inicializa classe e objetos e variáveis auxiliares
    def __init__(self):
        # Variáveis contadoras
        HUD.count_lapis = HUD.count_dist = 0
        self.icone_lapis = Sprite("../sprites/icone_lapis.png")
        self.icone_dist = Sprite("../sprites/icone_seta.png")
        self.icone_lapis.set_position(125, 10)
        self.icone_dist.set_position(115, HUD.janela.height * 1.15 / 14)

    def controle_dist(playing):
        if HUD.janela.time_elapsed() - HUD.timer >= 1000 and playing:
            HUD.count_dist += 1
            HUD.timer = HUD.janela.time_elapsed()
            Movel.x_vel += 1

    # Desenha o que é necessario na tela
    def atualizar(self, playing):
        # if playing:
        #   pass
        HUD.controle_dist(playing)
        self.icone_dist.draw()
        self.icone_lapis.draw()
        HUD.janela.draw_text(str(int(HUD.count_lapis)), 175, -7, size = 45, font_name = "Comic Sans MS", bold = True)
        HUD.janela.draw_text(str(int(HUD.count_dist)), 175, HUD.janela.height * 0.9 / 14, size = 45, font_name = "Comic Sans MS", bold = True)
