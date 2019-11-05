from PPlay.sprite import *
from PPlay.window import *
import os

def armazenaRanking(ranking, score):
    R = open(ranking, 'a')
    R.write(str(score)+'\n')
    R.close()

def ranking(janela, ranking, fundo):
    chart = Sprite("../sprites/menu3.png")
    chart.set_position(janela.width/2 - chart.width/2, 0)
    chart.draw()
    ranking_ord = []
    scores = []
    cont = 0
    y = 0
    teclado = Window.get_keyboard()
    if os.path.exists(ranking) == True:
        R = open(ranking, 'r')
        for linha in R:
            ranking_ord.append(linha)
        R.close()
        for i in range(len(ranking_ord)):
            lin = ranking_ord[i]
            var = ''
            cursor = 0
            while cursor<len(lin) and lin[cursor]!= '':
                if lin[cursor]!= '\n' and lin[cursor]!= '':
                    var = var + lin[cursor]
                else:
                    scores.append(int(var))
                cursor+=1
        scores = sorted(scores, reverse = True)
    janela.update()
    while True:
        fundo.draw()
        chart.draw()
        if len(scores)>0:
            janela.draw_text(str(scores[0]), janela.width / 2 - chart.width/4, janela.height/5, size=60,color=((0, 0, 0)), font_name="ARIAL BLACK", bold=True, italic=False)
        if len(scores)>1:
            janela.draw_text(str(scores[1]), janela.width / 2 - chart.width/4, 2* janela.height/5 , size=60,color=((0, 0, 0)), font_name="Arial BLACK", bold=True, italic=False)
        if len(scores)>2:
            janela.draw_text(str(scores[2]), janela.width / 2 - chart.width/4, 3* janela.height/5, size=60,color=((0, 0, 0)), font_name="Arial BLACK", bold=True, italic=False)
        if len(scores)>3:
            janela.draw_text(str(scores[3]), janela.width / 2 - chart.width/4, 4* janela.height/5, size=60,color=((0, 0, 0)), font_name="Arial BLACK", bold=True, italic=False)
        if teclado.key_pressed("ESC")==True:
            return
        janela.update()
