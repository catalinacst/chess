import pygame
import random

ANCHO = 900
ALTO = 600

map_columnas = 8
map_filas = 8
white = 50
black = 50
color_fondo = [82, 82, 82]

        #   a  b  c  d  e  f  g  h
board = [   0, 1, 0, 1, 0, 1, 0, 1, # 8
            1, 0, 1, 0, 1, 0, 1, 0, # 7
            0, 1, 0, 1, 0, 1, 0, 1, # 6
            1, 0, 1, 0, 1, 0, 1, 0, # 5
            0, 1, 0, 1, 0, 1, 0, 1, # 4
            1, 0, 1, 0, 1, 0, 1, 0, # 3
            0, 1, 0, 1, 0, 1, 0, 1, # 2
            1, 0, 1, 0, 1, 0, 1, 0, # 1
            ]

'''
blacks pares
blackKing = 2 rey
blackQueen = 4 reina
blackRook = 6 torre
blackBishop = 8 alfil
blackKnight = 10 caballo
blackPawn = 12 peon

whites impares
whiteKing = 3 rey
whiteQueen = 5 reina
whiteRook = 7 torre
whiteBishop = 9 alfil
whiteKnight = 11 caballo
whitePawn = 13 peon

0 = white
1 = black
'''
        #   a  b  c  d  e  f  g  h
pieces = [  6, 10, 8, 4, 2, 8, 10, 6, # 8
            12, 12, 12, 12, 12, 12, 12, 12, # 7
            -1, -1, -1, -1, -1, -1, -1, -1, # 6
            -1, -1, -1, -1, -1, -1, -1, -1, # 5
            -1, -1, -1, -1, -1, -1, -1, -1, # 4
            -1, -1, -1, -1, -1, -1, -1, -1, # 3
            13, 13, 13, 13, 13, 13, 13, 13, # 2
            7, 11, 9, 5, 3, 9, 11, 7, # 1
            ]

# upload images
piece_white = pygame.image.load('white.png')
piece_black = pygame.image.load('gray.png')
blackKing = pygame.image.load('blackKing.png')
whiteKing = pygame.image.load('whiteKing.png')
blackQueen = pygame.image.load('blackQueen.png')
whiteQueen = pygame.image.load('whiteQueen.png')
blackRook = pygame.image.load('blackRook.png')
whiteRook = pygame.image.load('whiteRook.png')
blackBishop = pygame.image.load('blackBishop.png')
whiteBishop = pygame.image.load('whiteBishop.png')
blackKnight = pygame.image.load('blackKnight.png')
whiteKnight = pygame.image.load('whiteKnight.png')
blackPawn = pygame.image.load('blackPawn.png')
whitePawn = pygame.image.load('whitePawn.png')

posi = 0
posf = 0
caballo = None

def Draw(nombre_mapa):
    inicio = x_i = y_j = 0
    y = 100
    fin = map_columnas
    for k in range(map_filas):
        x_i = 0
        fila = nombre_mapa[inicio:fin]
        for element in fila:
            x = 250 + (x_i * white)
            if element == 0:
                pantalla.blit(piece_white,(x,y))
            elif element == 1:
                pantalla.blit(piece_black,(x,y))
            elif element == 2:
                pantalla.blit(blackKing,(x,y))
            elif element == 3:
                pantalla.blit(whiteKing,(x,y))
            elif element == 4:
                pantalla.blit(blackQueen,(x,y))
            elif element == 5:
                pantalla.blit(whiteQueen,(x,y))
            elif element == 6:
                pantalla.blit(blackRook,(x,y))
            elif element == 7:
                pantalla.blit(whiteRook,(x,y))
            elif element == 8:
                pantalla.blit(blackBishop,(x,y))
            elif element == 9:
                pantalla.blit(whiteBishop,(x,y))
            elif element == 10:
                pantalla.blit(blackKnight,(x,y))
            elif element == 11:
                pantalla.blit(whiteKnight,(x,y))
            elif element == 12:
                pantalla.blit(blackPawn,(x,y))
            elif element == 13:
                pantalla.blit(whitePawn,(x,y))
            elif element == -1:
                pass
            x_i = x_i + 1
        y_j = y_j + 1
        y = 100 + (y_j * black)
        inicio = fin
        fin = fin + map_columnas

def row(pixel):
    if pixel <= 300:
        return 0
    elif pixel > 300 and pixel <= 350:
        return 1
    elif pixel > 350 and pixel <= 400:
        return 2
    elif pixel > 400 and pixel <= 450:
        return 3
    elif pixel > 450 and pixel <= 500:
        return 4
    elif pixel > 500 and pixel <= 550:
        return 5
    elif pixel > 550 and pixel <= 600:
        return 6
    elif pixel > 600:
        return 7

def column(pixel):
    if pixel <= 150:
        return 0
    elif pixel > 150 and pixel <= 200:
        return 1
    elif pixel > 200 and pixel <= 250:
        return 2
    elif pixel > 250 and pixel <= 300:
        return 3
    elif pixel > 300 and pixel <= 350:
        return 4
    elif pixel > 350 and pixel <= 400:
        return 5
    elif pixel > 400 and pixel <= 450:
        return 6
    elif pixel > 450:
        return 7

class Piece(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

def mov_torre(posi, posf, fichai, fichaf):
    if posi + 8 == posf or posi + 16 == posf or posi + 24 == posf or posi + 32 == posf or posi + 40 == posf or posi + 48 == posf or posi + 56 == posf:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1
    elif posi - 8 == posf or posi - 16 == posf or posi - 24 == posf or posi - 32 == posf or posi - 40 == posf or posi - 48 == posf or posi - 56 == posf:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1
    elif posi >= 0 and posi <= 7 and posf >= 0 and posf <= 7 or posi >= 8 and posi <= 15 and posf >= 8 and posf <= 15 or posi >= 16 and posi <= 23 and posf >= 16 and posf <= 23 or posi >= 24 and posi <= 31 and posf >= 24 and posf <= 31 or posi >= 32 and posi <= 39 and posf >= 32 and posf <= 39 or posi >= 40 and posi <= 47 and posf >= 40 and posf <= 47 or posi >= 48 and posi <= 55 and posf >= 48 and posf <= 55 or posi >= 56 and posi <= 63 and posf >= 56 and posf <= 63:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1

def mov_peon(posi, posf, fichai, fichaf):
    if posi >= 8 and posi <= 15 or posi >= 48 and posi <= 55:
        if fichai == "black" and posi + 8 == posf or fichai == "white" and posi - 8 == posf or fichai == "black" and posi + 16 == posf or fichai == "white" and posi - 16 == posf:
            if fichaf == "none":
                pieces[posf] = pieces[posi]
                pieces[posi] = -1
    elif fichai == "black" and posi + 8 == posf or fichai == "white" and posi - 8 == posf:
        if fichaf == "none":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1
    elif fichai == "black" and posi + 9 == posf or posi + 7 == posf:
        if fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1
    elif fichai == "white" and posi - 9 == posf or posi - 7 == posf:
        if fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1

def mov_alfil(posi, posf, fichai, fichaf):
    if posi + 9 == posf or posi + 18 == posf or posi + 27 == posf or posi + 36 == posf or posi + 45 == posf or posi + 54 == posf or posi + 63 == posf:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1
    elif posi - 9 == posf or posi - 18 == posf or posi - 27 == posf or posi - 36 == posf or posi - 45 == posf or posi - 54 == posf or posi - 63 == posf:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1
    elif posi + 7 == posf or posi + 14 == posf or posi + 21 == posf or posi + 28 == posf or posi + 35 == posf or posi + 42 == posf or posi + 49 == posf:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1
    elif posi - 7 == posf or posi - 14 == posf or posi - 21 == posf or posi - 28 == posf or posi - 35 == posf or posi - 42 == posf or posi - 49 == posf:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1

def mov_rey(posi, posf, fichai, fichaf):
    if posi + 1 == posf or posi - 1 == posf or posi + 8 == posf or posi - 8 == posf or posi - 7 == posf or posi - 9 == posf or posi + 7 == posf or posi + 9 == posf:
        if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
            pieces[posf] = pieces[posi]
            pieces[posi] = -1

if __name__ == '__main__':
    # Inicializar pygame
    pygame.init()
    # Inicializar pantalla
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    pantalla.fill(color_fondo)
    # Pintar tablero
    Draw(board)
    Draw(pieces)
    # reloj = pygame.time.Clock()
    coord1 = 0
    coord2 = 0
    fichai = 0
    while not fin:
        # capturar eventos
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if coord1 == 0:
                    posi = row(pos[0]) + column(pos[1]) * 8
                    if pieces[posi] == -1:
                        coord1 = 0
                    else:
                        fichai = pieces[posi]
                        if fichai % 2 == 0:
                            color_fichai = "black"
                        else:
                            color_fichai = "white"
                        coord1 = 1
                elif coord2 == 0:
                    posf = row(pos[0]) + column(pos[1]) * 8
                    fichaf = pieces[posf]
                    if fichaf == -1:
                        color_fichaf = "none"
                    elif fichaf % 2 == 0:
                        color_fichaf = "black"
                    else:
                        color_fichaf = "white"
                    if fichai == 6 or fichai == 7:
                        mov_torre(posi, posf, color_fichai, color_fichaf)
                        coord1 = 0
                        coord2 = 0
                    elif fichai == 12 or fichai == 13:
                        mov_peon(posi, posf, color_fichai, color_fichaf)
                        coord1 = 0
                        coord2 = 0
                    elif fichai == 8 or fichai == 9:
                        mov_alfil(posi, posf, color_fichai, color_fichaf)
                        coord1 = 0
                        coord2 = 0
                    elif fichai == 2 or fichai == 3:
                        mov_rey(posi, posf, color_fichai, color_fichaf)
                        coord1 = 0
                        coord2 = 0
                    else:
                        pieces[posf] = pieces[posi]
                        pieces[posi] = -1
                        coord1 = 0
                        coord2 = 0
        pantalla.fill(color_fondo)
        Draw(board)
        Draw(pieces)
        #pygame.display.update()
        pygame.display.flip()
