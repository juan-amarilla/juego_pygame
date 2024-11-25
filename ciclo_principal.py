from funciones_archivos import (pygame, SONIDO_TECLADO_MENU, leer_archivo, colocar_fondo, colocar_texto, 
COLORES, agregar_jugador) 
import random
from funciones_menu import (ajustar, colocar_rectangulo, PANTALLA, colocar_opciones, 
iniciar_con_musica, colocar_titulo) 

def eleccion(opcion: int, fuente, ejecutar: bool) -> bool:
    """
    Elegis una opcion

    Args:
    opcion(int)
    fuente(font)
    ejecutar(bool)

    Returns:
    Retorna True si sigue iterando o False si deja de iterar
    """

    if opcion == 0:
        SONIDO_TECLADO_MENU.play()
        nombre = ingresar_nombre(fuente)
        #jugar(nombre)
        ajustar(-1)

    elif opcion == 1:
        SONIDO_TECLADO_MENU.play()
        leer_archivo("puntuaciones.txt", ejecutar, fuente, 200, 50)

    elif opcion == 2:
        SONIDO_TECLADO_MENU.play()
        ejecutar = False

    return ejecutar

def menu(ejecutar: bool, fuente, titulo: str):
    """
    Te muestra un menu

    Args:
    ejecutar(bool)
    fuente(font)
    titulo(str)

    Returns:
    Returna True si sigue iterando o False si deja de iterar
    """
   
    ajustar(-1)

    while ejecutar:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutar = False

            
            elif evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:
                    x, y = evento.pos

                    for i, rectangulo in enumerate(rectangulos):

                        if rectangulo.collidepoint(x, y):
                            ejecutar = eleccion(i, fuente, ejecutar)

        colocar_fondo()
        colocar_rectangulo(70, 80, 700, 50)
        colocar_texto(fuente, titulo, 400, 100)
        rectangulos = colocar_opciones(fuente)
        pygame.display.flip()
        pygame.time.Clock().tick(5)

    return ejecutar

def ingresar_nombre(fuente):
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

        colocar_fondo()

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

        colocar_texto(fuente, "Su nombre buscador: ", 400, 50)
        rectangulo = pygame.Rect(100, 200, 700, 50)
        pygame.draw.rect(PANTALLA, COLORES["COLOR_RECTANGULO"], rectangulo, 2)

        nombre_a_colocar = fuente.render(nombre, True, COLORES["COLOR_TEXTO"])
        PANTALLA.blit(nombre_a_colocar, (rectangulo.x + 5, rectangulo.y + 5))

        pygame.display.flip()

    return nombre