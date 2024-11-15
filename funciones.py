import pygame
from constantes import *

def iniciar() -> None:
    """
    Descripcion

    Args:
    None

    Returns:
    None
    """

    pygame.init()

def colocar_titulo(titulo):

    pygame.display.set_caption(titulo)

def menu(fuente, ejecutar):

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutar = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 1:

                x, y = evento.pos

                for i, opcion in enumerate(OPCIONES):

                    texto = fuente.render(opcion, True, COLOR_TEXTO)
                    texto_rectangulo = texto.get_rect(center=(400, 300 + i * 100))

                    #rango de cuando el usuario hace click y es en ese rango de unos de los botones hace tal cosa
                    if texto_rectangulo.collidepoint(x, y):

                        if i == 0:
                            jugar()

                        elif i == 1:
                            ejecutar = False

    return ejecutar

def jugar():
    #logica
    #personajes, animacion y imagenes de fondo

    x, y = 400, 300
    velocidad_x = 5
    velocidad_y = 0
    gravedad = 1
    salto = False

    ejecutando = True

    while ejecutando:

        for evento in pygame.event.get():
            print("as")
    

def colocar_opciones(fuente, pantalla):

    for i, opcion in enumerate(OPCIONES):

        if i == opcion:
            texto = fuente.render(opcion, True, COLOR_SELECCIONADO)

        else:
            texto = fuente.render(opcion, True, COLOR_TEXTO)

        pantalla.blit(texto, (400 - texto.get_width() // 2, 300 + i * 100 - texto.get_height() // 2))