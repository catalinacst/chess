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
board = [ 0, 1, 0, 1, 0, 1, 0, 1, # 8
            1, 0, 1, 0, 1, 0, 1, 0, # 7
            0, 1, 0, 1, 0, 1, 0, 1, # 6
            1, 0, 1, 0, 1, 0, 1, 0, # 5
            0, 1, 0, 1, 0, 1, 0, 1, # 4
            1, 0, 1, 0, 1, 0, 1, 0, # 3
            0, 1, 0, 1, 0, 1, 0, 1, # 2
            1, 0, 1, 0, 1, 0, 1, 0, # 1
            ]

# Creando grupos - Globales -
caballos = pygame.sprite.Group()
todos = pygame.sprite.Group()

def Draw(nombre_mapa):
    piece_white = pygame.image.load('white.png')
    piece_black = pygame.image.load('gray.png')
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
                print x,y
            elif element == 1:
                pantalla.blit(piece_black,(x,y))
                print x,y
            x_i = x_i + 1
        y_j = y_j + 1
        y = 100 + (y_j * black)
        inicio = fin
        fin = fin + map_columnas

def row(pixel):
    if pixel >= 250 and pixel <= 300:
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
    elif pixel > 600 and pixel <= 700:
        return 7

def column(pixel):
    if pixel >= 100 and pixel <= 150:
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
    elif pixel > 450 and pixel <= 500:
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
    caballo = Caballo('blackKnight.png', [250, 100])
    caballos.add(caballo)
    todos.add(caballo)
    reloj = pygame.time.Clock()
    while not fin:
        #Capturar eventos
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion = row(pos[0]) + column(pos[1]) * 8
                print posicion
                #caballo.move(pos)

        #Draw(board)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(300)







#
