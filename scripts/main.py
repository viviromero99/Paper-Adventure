from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from hud import *
from menu import *
from itens import *
from ranking_funcoes import *

from random import randint

########### Funções Auxiliares ##############################################
def mover_objs(jogador, plataformas, itens):
    for plataforma in plataformas:
        plataforma.mover()
    for item in itens:
        item.mover()
    jogador.mover()

def colisoes_objs(jogador, plataformas, itens, janela):
    jogador.colisao = False
    for plataforma in plataformas:
        if plataforma.colisao(jogador.controler) and jogador.y_vel >= 0 and jogador.colisao == False:
            if plataforma.y_vel != 0:
                jogador.y_vel = plataforma.y_vel + (Pontilhada.gravidade * janela.delta_time())
            else:
                jogador.y_vel = 0
            jogador.colisao = True

    for i in range(len(itens) - 1, -1, -1):
        if itens[i].colisao(jogador.cur_sprt):
            itens[i].efeito(jogador)
            if itens[i].__class__.__name__ != "Borracha":
                itens.pop(i)


def atualizar_objs(jogador, plataformas, itens, janela):
    for i in range(len(plataformas) - 1, -1, -1):
        if plataformas[i].x < -plataformas[i].width or plataformas[i].y > janela.height + plataformas[i].height + jogador.cur_sprt.height:
            plataformas.pop(i)

    for j in range(len(itens) - 1, -1, -1):
        if itens[j].x < -itens[j].width or itens[j].y > janela.height + itens[j].height:
            itens.pop(j)

    # Controle do tempo de duração do efeito da Caneta
    # Se passar o tempo
    if janela.time_elapsed() - Caneta.timer >= Caneta.t_efeito and Caneta.ativo:
        jogador.invulneravel = False
        Caneta.ativo = False
        # Volta com os sprites normais
        if jogador.cur_sprt == jogador.corrida_blue:
            jogador.trocar_sprite(jogador.corrida)
        else:
            jogador.trocar_sprite(jogador.pulo)

    # Controle do tempo de duração do efeito da Caneca
    # Se passar o tempo
    if janela.time_elapsed() - Cafe.timer >= Cafe.t_efeito and Cafe.ativo:
        # Volta com a velocidade anterior
        Movel.x_vel = Cafe.vel_init
        Cafe.ativo = False

    jogador.corrida.update()
    jogador.corrida_blue.update()

def desenhar_objs(jogador, plataformas, itens):
    for plataforma in plataformas:
        plataforma.draw()

    for item in itens:
        item.draw()

    #jogador.controler.draw()
    jogador.cur_sprt.draw()

def criar_objs(plataformas, itens, timer, playing, janela):

    # Testa o intervalo entre a criação dos objetos
    if janela.time_elapsed() - timer >= 1500 and playing:
        aux = randint(0, 5)
        if aux < 2:
            # Cria uma plataforma nova
            plataformas.append(Pontilhada(randint(0, 4), width = randint(Pontilhada.max_width // 5, Pontilhada.max_width // 2)))
        else:
            # Cria uma plataforma nova
            plataformas.append(Plataforma(randint(0, 4), width = randint(Plataforma.max_width // 5, Plataforma.max_width // 2)))
        # Calcula a quantidade de itens na plataforma
        qtd_itens = int(plataformas[-1].width / 88)
        plt = plataformas[-1]

        # Cria os itens em cima da plataforma
        for i in range(qtd_itens):
            aux = randint(0, 100)
            if aux < 1: # 1% de chance de aparecer um café
                itens.append(Cafe(plt.x + 88 * i, plt.y, plt))
            elif aux < 2: # 1% de chance de aparecer uma caneta
                itens.append(Caneta(plt.x + 88 * i, plt.y, plt))
            elif aux < 22 and i == 0: # 20% de chance de aparecer uma borracha (se for borracha, vai ser o único item na plataforma)
                itens.append(Borracha(plt.x + 88 * i, plt.y, plt))
                break
            elif aux < 72: # 70% de chance de aparecer um lápis
                itens.append(Lapis(plt.x + 88 * i, plt.y, plt))
            # 28% de chance de não ter item nenhum

            timer = janela.time_elapsed()

    return timer # Passa o tempo atual para o controle de criação

##############################################################################

########### Função Principal #################################################
# Variável de controle
# Indica se o jogo está pausado ou não
def play():
    # Define as configurações da janela
    janela = Window(1280, 630)
    # janela = Window(1, 1) #<------ Isso aqui é só uma gambiarra minha. Liga não
    janela.set_title("Paper Adventure!")
    mouse = Window.get_mouse()
    logo = Sprite("../sprites/PAlogo.png")
    logo.set_position(janela.width/2 - logo.width/2, logo.height/10)
    cursor = Sprite("../sprites/lapis.png")
    # Game Loop
    # Chama funções das classes para atualizar os objetos
    while True:

        fundo = GameImage("../sprites/background.jpg")
        op1 = Sprite("../sprites/menuu1.png")
        op1.set_position(janela.width/2 - op1.width/2,2.5*(janela.height/7)+ op1.height)
        op2 = Sprite("../sprites/menu3.png")
        op2.set_position(janela.width/2 - op2.width/2,4*(janela.height/7) + op2.height/2)
        op3 = Sprite("../sprites/menu2.png")
        op3.set_position(janela.width/2 - op3.width/2,5.5*(janela.height/7))
        hover1 = hover2 = hover3 = False
        mouse.hide()
        while True:
            fundo.draw()
            logo.draw()
            op1.draw()
            op2.draw()
            op3.draw()
            # pos = mouse.get_position()
            cursor.x, cursor.y = mouse.get_position()
            cursor.draw()
            # cursor.y = pos[1]
            if mouse.is_over_area([janela.width/2 - op1.width/2,2.5*(janela.height/7) + op1.height],[janela.width/2 + op1.width/2,2.5*(janela.height/7) + 2*op1.height])== True:
                if hover1 == False:
                    op1 = Sprite("../sprites/menuu12.png")
                    op1.set_position(janela.width/2 - op1.width/2,2.5*(janela.height/7)+ op1.height)
                    hover1 = True
                if mouse.is_button_pressed(1) == True:
                    break
            elif hover1 == True:
                op1 = Sprite("../sprites/menuu1.png")
                op1.set_position(janela.width/2 - op1.width/2,2.5*(janela.height/7)+ op1.height)
                hover1 = False

            if mouse.is_over_area([janela.width/2 - op2.width/2,4*(janela.height/7) + op2.height/2],[janela.width/2 + op2.width/2,4*(janela.height/7) + 1.5*op2.height])== True:
                if hover2 == False:
                    op2 = Sprite("../sprites/menu32.png")
                    op2.set_position(janela.width/2 - op2.width/2,4*(janela.height/7) + op2.height/2)
                    hover2 = True
                if mouse.is_button_pressed(1) == True:
                    ranking(janela, "ranking.txt", fundo)
            elif hover2 == True:
                op2 = Sprite("../sprites/menu3.png")
                op2.set_position(janela.width/2 - op2.width/2,4*(janela.height/7) + op2.height/2)
                hover2 = False

            if mouse.is_over_area([janela.width/2 - op3.width/2,5.5*(janela.height/7)], [janela.width/2 + op3.width/2,5.5*(janela.height/7) + op3.height])== True:
                if hover3 == False:
                    op3 = Sprite("../sprites/menu22.png")
                    op3.set_position(janela.width/2 - op3.width/2,5.5*(janela.height/7))
                    hover3 = True
                if mouse.is_button_pressed(1) == True:
                    sys.exit()
            elif hover3 == True:
                op3 = Sprite("../sprites/menu2.png")
                op3.set_position(janela.width/2 - op3.width/2,5.5*(janela.height/7))
                hover3 = False
            janela.update()

        op1 = op2 = op3 = None

        fundo = GameImage("../sprites/background.jpg")

        # Define atributos da main usados nas classes
        Movel.janela = Player.janela = Menu.janela = HUD.janela = janela
        Player.teclado = teclado = janela.get_keyboard()
        Menu.mouse = janela.get_mouse()
        Movel.x_vel = janela.width / 7

        itens, plataformas = [], []

        # Define objetos do jogo
        hud = HUD()
        menu = Menu()
        Pontilhada.jogador = jogador = Player()
        plataformas.append(Plataforma(0, 0))
        timer = 0
        playing = True
        janela.update()
        while True:
            fundo.draw()
            # Atualiza o hud (classe HUD)
            hud.atualizar(playing)

            if playing:
                if HUD.count_lapis < 0 or jogador.cur_sprt.y > janela.height:
                    armazenaRanking("ranking.txt", HUD.count_dist)
                    break
                colisoes_objs(jogador, plataformas, itens, janela)
                mover_objs(jogador, plataformas, itens)
                atualizar_objs(jogador, plataformas, itens, janela)
            desenhar_objs(jogador, plataformas, itens)

            # Se pressionar ESC ou o jogo estiver pausado
            if teclado.key_pressed("ESC") or not playing:
                retorno = menu.atualizar()
                cursor.x, cursor.y = mouse.get_position()
                cursor.draw()
                if retorno == 0:
                    playing = True
                elif retorno == 1:
                    playing = True
                    break
                elif retorno == 2:
                    playing = False


            janela.update()
            # Controle de criação de novos objetos
            timer = criar_objs(plataformas, itens, timer, playing, janela)

play()
