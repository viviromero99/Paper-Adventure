from PPlay.sprite import *
from PPlay.gameimage import *

class Menu():
    # Objetos da main
    janela = mouse = None

    # Inicializa objetos e variáveis auxiliares
    def __init__(self):
        # Lista de botões
        self.botoes = []
        # Variavel auxiliar
        self.hover_b4 = False
        self.alpha = GameImage("../sprites/alpha.png")
        self.papel = Sprite("../sprites/post-it.png")
        self.botoes.append(Sprite("../sprites/resume.png")) # Adiciona os botoes à lista
        self.botoes.append(Sprite("../sprites/sair.png")) # Adiciona os botoes à lista
        self.papel.set_position((Menu.janela.width - self.papel.width) / 2, (Menu.janela.height - self.papel.height) / 2)
        self.botoes[0].set_position((Menu.janela.width - self.botoes[0].width) / 2 - 20, (Menu.janela.height - self.botoes[0].height) / 3)
        self.botoes[1].set_position((Menu.janela.width - self.botoes[1].width) / 2, (Menu.janela.height - self.botoes[1].height) * 2 / 3)

    # Controle de ações dos botões
    def controle_click(self):
        # Se o cursor estiver sobre o botão "Resume"
        if Menu.mouse.is_over_object(self.botoes[0]):
            if not self.hover_b4:
                # Define o sprite e o posiciona
                self.botoes[0] = Sprite("../sprites/resume_hover.png")
                self.botoes[0].set_position((Menu.janela.width - self.botoes[0].width) / 2 - 20, (Menu.janela.height - self.botoes[0].height) / 3)
                self.hover_b4 = True
            # Se clicar no botão:
            if Menu.mouse.is_button_pressed(1):
                return 0

        # Se o cursor estiver sobre o botão "Sair"
        elif Menu.mouse.is_over_object(self.botoes[1]):
            if not self.hover_b4:
                # Define o sprite e o posiciona
                self.botoes[1] = Sprite("../sprites/sair_hover.png")
                self.botoes[1].set_position((Menu.janela.width - self.botoes[1].width) / 2, (Menu.janela.height - self.botoes[1].height) * 2 / 3)
                self.hover_b4 = True
            # Se clicar no botão:
            if Menu.mouse.is_button_pressed(1):
                return 1
        # Se não estiver sobre nenhum botão
        else:
            if self.hover_b4:
                # Define o sprite e o posiciona
                self.botoes[0] = Sprite("../sprites/resume.png")
                self.botoes[1] = Sprite("../sprites/sair.png")
                self.botoes[0].set_position((Menu.janela.width - self.botoes[0].width) / 2 - 20, (Menu.janela.height - self.botoes[0].height) / 3)
                self.botoes[1].set_position((Menu.janela.width - self.botoes[1].width) / 2, (Menu.janela.height - self.botoes[1].height) * 2 / 3)
                self.hover_b4 = False
        # Retorno padrão (sem clicar em nenhum botao)
        return 2


    # Chama as funções da classe e desenha o que for necessário
    def atualizar(self):
        self.alpha.draw()
        self.papel.draw()
        for i in range(len(self.botoes)): # Desenha cada botão
            self.botoes[i].draw()
        return self.controle_click()
