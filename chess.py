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
blacks
blackKing = 2 rey
blackQueen = 4 reina
blackRook = 6 torre
blackBishop = 8 alfil
blackKnight = 10 caballo
blackPawn = 12 peon

whites
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

class Caballo(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(archivo_img).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.mover = 0
        self.x = 0
        self.y = 0
        self.m = 0
        self.xf = 0
        self.yf = 0
        self.xt = 0
        self.yt = 0

    def move(self, pos):
        if self.mover == 0:
            self.mover = 1
            self.xf = pos[0] - 15
            self.yf = pos[1] - 10
            self.x = self.rect.x
            self.y = self.rect.y
            self.xt = float(self.xf - self.rect.x)
            self.yt = float(self.yf - self.rect.y)
            if self.xt < 0:
                self.xt =  self.xt * -1
            if self.yt < 0:
                self.yt = self.yt * -1

    def update(self):
        if self.mover == 1:
            if self.xt > self.yt:
                # Primero en X
                if self.x < self.xf:
                    self.x+= 1
                    self.rect.x = self.x
                elif self.x > self.xf:
                    self.x-= 1
                    self.rect.x = self.x
                elif self.y > self.yf:
                    self.y-= 1
                    self.rect.y = self.y
                elif self.y < self.yf:
                    self.y+= 1
                    self.rect.y = self.y
                else:
                    self.mover = 0
            if self.xt < self.yt:
                # Primero en Y
                if self.y > self.yf:
                    self.y-= 1
                    self.rect.y = self.y
                elif self.y < self.yf:
                    self.y+= 1
                    self.rect.y = self.y
                elif self.x < self.xf:
                    self.x+= 1
                    self.rect.x = self.x
                elif self.x > self.xf:
                    self.x-= 1
                    self.rect.x = self.x
                else:
                    self.mover = 0

'''
    # Movimiento Alfil
    def update(self):
        if self.mover == 1:
            if self.x < self.xf:
                self.x+= 1
                self.y+= self.m
                self.rect.x = self.x
                self.rect.y = int(self.y)
            elif self.x > self.xf:
                self.x-= 1
                self.y-= self.m
                self.rect.x = self.x
                self.rect.y = int(self.y)
            else:
                self.mover = 0
'''

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
    reloj = pygame.time.Clock()
    coord1 = 0
    coord2 = 0
    while not fin:
        #Capturar eventos
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if coord1 == 0:
                    posicion1 = row(pos[0]) + column(pos[1]) * 8
                    if pieces[posicion1] == -1:
                        coord1 = 0
                    else:
                        coord1 = 1
                elif coord2 == 0:
                    posicion2 = row(pos[0]) + column(pos[1]) * 8
                    if pieces[posicion2] == -1:
                        pieces[posicion2] = pieces[posicion1]
                        # print posicion1
                        pieces[posicion1] = -1
                        coord1 = 0
                        coord2 = 0
                    else:
                        coord1 = 0
                        coord2 = 0
        # print pieces
        #print str(pieces[posicion])
        #caballo.move(pos)
        pantalla.fill(color_fondo)
        Draw(board)
        Draw(pieces)

        pygame.display.flip()







#
