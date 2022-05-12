import numpy as np
import pygame
from pygame.locals import *
import sys
import math

pygame.init()


schack = False

SVART = (88, 40, 77)
VIT = (203, 144, 190)
RÖD = (255,0,0)
drag=[]
vita_pjäser = ["b", "n", "p", "q", "r"]
svarta_pjäser = ["B", "N", "P", "Q", "R"]

# bräde = np.zeros(64)
bräde = np.empty((8, 8), dtype=str)
x = 0
y = 0

p_bild = pygame.transform.scale(pygame.image.load(r'grafik\w_pawn_2x_ns.png'), (70, 70))
b_bild = pygame.transform.scale(pygame.image.load(r'grafik\w_bishop_2x_ns.png'), (70, 70))
k_bild = pygame.transform.scale(pygame.image.load(r'grafik\w_king_2x_ns.png'), (70, 70))
q_bild = pygame.transform.scale(pygame.image.load(r'grafik\w_queen_2x_ns.png'), (70, 70))
n_bild = pygame.transform.scale(pygame.image.load(r'grafik\w_knight_2x_ns.png'), (70, 70))
r_bild = pygame.transform.scale(pygame.image.load(r'grafik\w_rook_2x_ns.png'), (70, 70))

P_bild = pygame.transform.scale(pygame.image.load(r'grafik\b_pawn_2x_ns.png'), (70, 70))
B_bild = pygame.transform.scale(pygame.image.load(r'grafik\b_bishop_2x_ns.png'), (70, 70))
K_bild = pygame.transform.scale(pygame.image.load(r'grafik\b_king_2x_ns.png'), (70, 70))
Q_bild = pygame.transform.scale(pygame.image.load(r'grafik\b_queen_2x_ns.png'), (70, 70))
N_bild = pygame.transform.scale(pygame.image.load(r'grafik\b_knight_2x_ns.png'), (70, 70))
R_bild = pygame.transform.scale(pygame.image.load(r'grafik\b_rook_2x_ns.png'), (70, 70))


def fen2bräde(bräde, fen, x, y):
    for i in fen:
        if i == "r":
            bräde[x][y] = "r"
        if i == "n":
            bräde[x][y] = "n"
        if i == "b":
            bräde[x][y] = "b"
        if i == "q":
            bräde[x][y] = "q"
        if i == "k":
            bräde[x][y] = "k"
        if i == "p":
            bräde[x][y] = "p"
        if i == "R":
            bräde[x][y] = "R"
        if i == "N":
            bräde[x][y] = "N"
        if i == "B":
            bräde[x][y] = "B"
        if i == "Q":
            bräde[x][y] = "Q"
        if i == "K":
            bräde[x][y] = "K"
        if i == "P":
            bräde[x][y] = "P"
        if i == "/":
            x = -1
            y += 1
        if i == "1":
            x += 1
        if i == "2":
            x += 2
        if i == "3":
            x += 3
        if i == "4":
            x += 4
        if i == "5":
            x += 5
        if i == "6":
            x += 6
        if i == "7":
            x += 7
        if i == "8":
            x += 8
        x += 1

    return bräde

är_vit = True


def ta_pjäs(bräde,y,x,tur,drag_ta):
    if tur == "vit":
        if bräde[y][x]=="P" or bräde[y][x]=="Q" or bräde[y][x]=="R" or bräde[y][x]=="N" or bräde[y][x]=="B":
            drag_ta.append((y,x))

    if tur == "svart":
        if bräde[y][x]=="p" or bräde[y][x]=="q" or bräde[y][x]=="r" or bräde[y][x]=="n" or bräde[y][x]=="b":
            drag_ta.append((y,x))

    return drag_ta

def rita_bräde(bräde,drag):
    är_vit = True
    pygame.display.flip()
    for c in range(0, 9):
        for r in range(0, 9):
            if är_vit == True:
                pygame.draw.rect(skärm, VIT,
                                 (c * KVADRAT_STORLEK, r * KVADRAT_STORLEK, KVADRAT_STORLEK, KVADRAT_STORLEK))
                är_vit = False
            else:
                pygame.draw.rect(skärm, SVART,
                                 (c * KVADRAT_STORLEK, r * KVADRAT_STORLEK, KVADRAT_STORLEK, KVADRAT_STORLEK))
                är_vit = True

    for c in range(0, 8):
        for r in range(0, 8):
            if bräde[c][r] == "p":
                skärm.blit(p_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "b":
                skärm.blit(b_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "k":
                skärm.blit(k_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "n":
                skärm.blit(n_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "q":
                skärm.blit(q_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "r":
                skärm.blit(r_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "P":
                skärm.blit(P_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "B":
                skärm.blit(B_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "K":
                skärm.blit(K_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "N":
                skärm.blit(N_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "Q":
                skärm.blit(Q_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))
            if bräde[c][r] == "R":
                skärm.blit(R_bild, (c * KVADRAT_STORLEK + 10, r * KVADRAT_STORLEK + 10))


def häst_drag(bräde, kol, rad,tur,ta_drag):
    drag = []
    drag_ta=[]

    y = kol + 2
    x = rad + 1
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    y = kol + 1
    x = rad + 2
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    y = kol - 2
    x = rad - 1
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    y = kol - 1
    x = rad - 2
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    y = kol + 2
    x = rad - 1
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    y = kol + 1
    x = rad - 2
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    y = kol - 1
    x = rad + 2
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    y = kol - 2
    x = rad + 1
    if x < 8 and x >= 0 and y < 8 and y >= 0:
        if bräde[y][x] == "":
            drag.append((y, x))
        ta_drag = ta_pjäs(bräde,y,x,tur,drag_ta)

    drag = drag + ta_drag
    return drag


def linjära_drag(bräde, kol, rad,tur,ta_drag):
    drag = []
    drag_ta=[]

    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    x = rad
    while x > 0:

        x -= x1
        if bräde[kol][x] == "":
            drag.append((kol, x))
        else:
            ta_drag = ta_pjäs(bräde, kol, x, tur, ta_drag)
            x = 0

    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    x = rad
    while x < 7:

        x += x2
        if bräde[kol][x] == "":
            drag.append((kol, x))
        else:
            ta_drag = ta_pjäs(bräde, kol, x, tur, ta_drag)
            x = 7


    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    y = kol
    while y < 7:
        y += y1
        if bräde[y][rad] == "":
            drag.append((y, rad))
        else:
            ta_drag = ta_pjäs(bräde,y,rad,tur,ta_drag)
            y=7

    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    y = kol
    while y > 0:
        y -= y2
        if bräde[y][rad] == "":
            drag.append((y, rad))
        else:
            ta_drag = ta_pjäs(bräde, y, rad, tur, ta_drag)
            y = 0


    drag = drag + ta_drag
    return drag

def promotion_bonde(bräde, kol,rad,tur):


def kung_drag(bräde,kol,rad,tur,ta_drag):
    drag=[]
    drag_ta=[]

    if kol < 7:
        if bräde[kol+1][rad]=="":
            drag.append((kol,rad))
            ta_drag = ta_pjäs(bräde, kol+1, rad, tur,ta_drag)

    if kol > 0:
        if bräde[kol-1][rad]=="":
            drag.append((kol-1,rad))
            ta_drag = ta_pjäs(bräde, kol-1, rad, tur,ta_drag)

    if rad < 7:
        if bräde[kol][rad+1]=="":
            drag.append((kol,rad+1))
            ta_drag = ta_pjäs(bräde, kol, rad+1, tur,ta_drag)

    if rad > 0:
        if bräde[kol][rad-1]=="":
            drag.append((kol,rad-1))
            ta_drag = ta_pjäs(bräde, kol, rad-1, tur,ta_drag)

    if kol < 7 and rad < 7:
        if bräde[kol+1][rad+1]=="":
            drag.append((kol+1,rad+1))
            ta_drag = ta_pjäs(bräde, kol+1, rad+1, tur,ta_drag)

    if kol > 0 and rad < 7:
        if bräde[kol-1][rad+1]=="":
            drag.append((kol-1,rad+1))
            ta_drag = ta_pjäs(bräde, kol-1, rad+1, tur,ta_drag)

    if kol < 7 and rad > 0:
        if bräde[kol+1][rad-1]=="":
            drag.append((kol+1,rad-1))
            ta_drag = ta_pjäs(bräde, kol+1, rad-1, tur,ta_drag)

    if kol > 0 and rad > 0:
        if bräde[kol-1][rad-1]=="":
            drag.append((kol-1,rad-1))
            ta_drag = ta_pjäs(bräde, kol-1, rad-1, tur,ta_drag)

    drag = ta_drag + drag
    return drag


def diagonala_drag(bräde, kol, rad,tur,ta_drag):
    drag = []
    drag_ta=[]

    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    x = rad
    y = kol
    while x >= 0 and y >= 0:
        x -= x1
        y -= y1

        if bräde[y][x] == "":
            drag.append((y, x))
        else:
            print(y,x)
            ta_drag = ta_pjäs(bräde, y, x, tur, drag_ta)
            x = -1

    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    x = rad
    y = kol

    while x < 7 and y < 7:
        x += x2
        y += y2
        if bräde[y][x] == "":
            drag.append((y, x))
        else:
            ta_drag = ta_pjäs(bräde, y, x, tur, drag_ta)
            x = 7

    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    x = rad
    y = kol
    while x >= 0 and y < 7:
        x -= x2
        y += y1
        if bräde[y][x] == "":
            drag.append((y, x))
        else:
            ta_drag = ta_pjäs(bräde, y, x, tur, drag_ta)
            y = 7

    x1, x2, y1, y2, x, y = 1, 1, 1, 1, 0, 0
    x = rad
    y = kol
    while y >= 0 and x < 7:
        x += x1
        y -= y2
        if bräde[y][x] == "":
            drag.append((y, x))
        else:
            ta_drag = ta_pjäs(bräde, y, x, tur, drag_ta)
            y = -1


    drag = ta_drag + drag
    return drag
def vit_bonde_ta(bräde,y,x):
    drag_ta=[]
    if bräde[y-1][x+1] == "P" or bräde[y-1][x+1] == "Q" or bräde[y-1][x+1] == "R" or bräde[y-1][x+1] == "N" or bräde[y-1][x+1] == "B":
        drag_ta.append((y-1,x+1))
    if bräde[y-1][x-1] == "P" or bräde[y-1][x-1] == "Q" or bräde[y-1][x-1] == "R" or bräde[y-1][x-1] == "N" or bräde[y-1][x-1] == "B":
        drag_ta.append((y-1,x-1))
    return drag_ta

def svart_bonde_ta(bräde,kol,rad):
    drag_ta=[]
    if bräde[y+1][x+1] == "P" or bräde[y+1][x+1] == "Q" or bräde[y+1][x+1] == "R" or bräde[y+1][x+1] == "N" or bräde[y+1][x+1] == "B":
        drag_ta.append((y+1,x+1))
    if bräde[y+1][x-1] == "P" or bräde[y+1][x-1] == "Q" or bräde[y+1][x-1] == "R" or bräde[y+1][x-1] == "N" or bräde[y+1][x-1] == "B":
        drag_ta.append((y-1,x-1))
    return drag_ta

def vit_bonde_drag(bräde,kol,rad,tur,ta_drag):
    drag=[]
    drag2=[]
    if rad == 6:
        if bräde[kol][rad - 2]=="" and bräde[kol][rad-1]=="":
            drag2.append((kol,rad-2))
    if bräde[kol][rad - 1]=="":
        drag.append((kol,rad-1))

    drag_ta = vit_bonde_ta(bräde,kol,rad)

    drag=drag+drag2+drag_ta
    return drag


def svart_bonde_drag(bräde,kol,rad,tur,ta_drag):
    drag=[]
    drag2=[]
    if rad == 1:
        if bräde[kol][rad + 2]=="" and bräde[kol][rad+1]=="":
            drag2.append((kol,rad+2))
    if bräde[kol][rad + 1]=="":
        drag.append((kol,rad+1))
    drag_ta = svart_bonde_ta(bräde,kol,rad)

    drag=drag+drag2+drag_ta
    return drag

def tillåtna_drag(pjäs, bräde, kol, rad, tur):
    drag = []
    ta_drag = []
    if pjäs == "p" and tur == "vit":
        drag = vit_bonde_drag(bräde,kol,rad,tur,ta_drag)
    if pjäs == "P" and tur == "svart":
        drag = svart_bonde_drag(bräde,kol,rad,tur,ta_drag)
    if pjäs == "r" and tur == "vit":
        drag = linjära_drag(bräde, kol, rad,tur,ta_drag)
    if pjäs == "R" and tur == "svart":
        drag = linjära_drag(bräde, kol, rad,tur,ta_drag)
    if pjäs == "b" and tur == "vit":
        drag = diagonala_drag(bräde, kol, rad,tur,ta_drag)
    if pjäs == "B" and tur == "svart":
        drag = diagonala_drag(bräde, kol, rad,tur,ta_drag)
    if pjäs == "q" and tur == "vit":
        drag1 = diagonala_drag(bräde, kol, rad,tur,ta_drag)
        drag2 = linjära_drag(bräde, kol, rad,tur, ta_drag)
        drag = drag1 + drag2
    if pjäs == "Q" and tur == "svart":
        drag1 = diagonala_drag(bräde, kol, rad,tur,ta_drag)
        drag2 = linjära_drag(bräde, kol, rad,tur, ta_drag)
        drag = drag1 + drag2
    if pjäs == "n" and tur == "vit":
        drag = häst_drag(bräde, kol, rad,tur,ta_drag)
    if pjäs == "N" and tur == "svart":
        drag = häst_drag(bräde, kol, rad,tur,ta_drag)
    if pjäs == "k" and tur == "vit":
        drag = kung_drag(bräde, kol, rad,tur,ta_drag)
    if pjäs == "K" and tur == "svart":
        drag = kung_drag(bräde, kol, rad,tur,ta_drag)
    return drag


s = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
# s = str(input("Fen"))
s = s.replace(" ", "")

bräde = fen2bräde(bräde, s, x, y)
bräde = np.flip(bräde)
print(bräde)
lyckat_drag = False
KVADRAT_STORLEK = 90
tur = "vit"
bredd = 8 * KVADRAT_STORLEK
höjd = 8 * KVADRAT_STORLEK

size = (bredd, höjd)
inte_ok = True
skärm = pygame.display.set_mode(size)
rita_bräde(bräde,drag)
pygame.display.update()

myfont = pygame.font.SysFont("Comic Sans MS", 75)
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            kol = int(math.floor(posx / KVADRAT_STORLEK))
            rad = int(math.floor(posy / KVADRAT_STORLEK))
            pjäs = bräde[kol][rad]

            drag = tillåtna_drag(pjäs, bräde, kol, rad, tur)

        if event.type == pygame.MOUSEBUTTONUP:
            kol2, rad2 = kol, rad
            posx = event.pos[0]
            posy = event.pos[1]
            kol = int(math.floor(posx / KVADRAT_STORLEK))
            rad = int(math.floor(posy / KVADRAT_STORLEK))
            print(drag)
            for i in drag:
                if (kol, rad) == i:
                    bräde[kol2][rad2] = ""
                    bräde[kol][rad] = pjäs
                    lyckat_drag = True
            if lyckat_drag == True:
                if tur == "vit":
                    tur = "svart"
                elif tur == "svart":
                    tur = "vit"
            lyckat_drag = False
            print(bräde)

        rita_bräde(bräde,drag)

        pygame.display.update()

    if game_over:
        pygame.time.wait(5000)
