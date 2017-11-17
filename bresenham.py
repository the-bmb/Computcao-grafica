import pygame
import sys

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROXO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

pantalla = pygame.display.set_mode([ANCHO, ALTO])


def DrawPixel(p,color):
    pantalla.set_at(p,color)
    pygame.display.flip()

#Funcao para desenhar a reta
def bresenham(x1, y1, x2, y2):

       # Onde inverte a linha x1 > x2
       if x1 > x2:
           bresenham(x2, y2, x1, y1)
           return
       dx = x2 - x1
       dy = y2 - y1

       if dy < 0:
           slope = -1
           dy = -dy
       else:
          slope = 1

       # Constante de Bresenham
       incE = 2 * dy;
       incNE = 2 * dy - 2 * dx
       d = 2 * dy - dx
       y = y1
       for x in range(x1,x2):
           DrawPixel((x, y), BRANCO)
           if (d <= 0):
             d += incE
           else:
             d += incNE
             y += slope


# Funcao para desenhar o circulo
def drawCircle(xC, yC, r, color):
    x = 0
    y = r
    u = 1
    v = 2 * r - 1
    E = 0
    while (x < y):
        DrawPixel((xC + x, yC + y), color)
        DrawPixel((xC + y, yC - x), color)
        DrawPixel((xC - x, yC - y), color)
        DrawPixel((xC - y, yC + x), color)
        x+=1
        E += u
        u += 2
        if (v < 2 * E):
            y-=1
            E -= v
            v -= 2
        if (x > y):
            break
        DrawPixel((xC + y, yC + x), color)
        DrawPixel((xC + x, yC - y), color)
        DrawPixel((xC - y, yC - x), color)
        DrawPixel((xC - x, yC + y), color)

# Chamada das funcoes
bresenham(20, 20, 120, 240)
drawCircle(150, 150, 20, BRANCO)

# Codigo para interface grafica pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
