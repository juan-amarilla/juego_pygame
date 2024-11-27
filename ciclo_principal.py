import pygame
from constantes import SONIDO_TECLADO_MENU
from funciones_archivos import leer_archivo
from funciones_pantalla import (colocar_menu, colocar_nombre_pantalla)

def eleccion(opcion: int, ejecutar: bool) -> bool:
    """
    Elegis una opcion

    Args:
    opcion(int)
    ejecutar(bool)

    Returns:
    Retorna True si sigue iterando o False si deja de iterar
    """

    if opcion == 0:
        SONIDO_TECLADO_MENU.play()
        nombre = ingresar_nombre()
        print(nombre)

    elif opcion == 1:
        SONIDO_TECLADO_MENU.play()
        leer_archivo("puntuaciones.txt", ejecutar, 200, 50)

    elif opcion == 2:
        SONIDO_TECLADO_MENU.play()
        ejecutar = False

    return ejecutar

def menu(ejecutar: bool):
    """
    Te muestra un menu

    Args:
    ejecutar(bool)

    Returns:
    Returna True si sigue iterando o False si deja de iterar
    """
   
    pygame.mixer.music.play(-1)

    while ejecutar:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutar = False

            
            elif evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:
                    x, y = evento.pos

                    for i, rectangulo in enumerate(rectangulos):

                        if rectangulo.collidepoint(x, y):
                            ejecutar = eleccion(i, ejecutar)

        rectangulos = colocar_menu()

    return ejecutar

def ingresar_nombre():
    """
    Ingresas un nombre

    Args:
    fuente(font)

    Returns:
    Returna True si sigue iterando o False si deja de iterar
    """

    nombre = ""
    ejecutar = True

    while ejecutar:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutar = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:
                        SONIDO_TECLADO_MENU.play()
                        ejecutar = False

                elif evento.key == pygame.K_BACKSPACE:
                        SONIDO_TECLADO_MENU.play()
                        nombre = nombre[:-1]

                elif len(nombre) <= 12:
                    SONIDO_TECLADO_MENU.play()
                    nombre += evento.unicode

        nombre = colocar_nombre_pantalla(nombre)  

    return nombre