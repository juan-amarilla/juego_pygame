# pylint: disable=no-member
import pygame
from constantes_inicio import *
from funciones_archivos import leer_archivo
from funciones_menu import *
from funciones_juego import iniciar_juego
from constantes_juego import FONDO, FONDO_1, FONDO_2


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

        resultado = iniciar_juego(nombre, FONDO, FONDO_1, FONDO_2)
        if resultado in ["gano", "perdio"]:
            print(f"El jugador {
                  nombre} terminó el juego con el resultado: {resultado}")
            ejecutar = True  # Volver al menú principal

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
    pygame.mixer.music.stop()  # Detiene cualquier música que estuviera sonando
    pygame.mixer.music.load("recursos_menu/musica/musica_menu/ambient 9.mp3")
    pygame.mixer.music.play(-1)  # Reproduce la música del menú en bucle
    condicion = 1

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

        # colocar_fondo(condicion)
        colocar_rectangulo(35, 80, 750, 50)
        colocar_texto(TITULO, 400, 100)
        rectangulos = colocar_opciones()
        pygame.display.flip()
        pygame.time.Clock().tick(5)

    return ejecutar


def ingresar_nombre():
    """
    Ingresas un nombre

    Args:
    fuente(font)

    Returns:
    Returna True si sigue iterando o False si deja de iterar
    """

    condicion = 1
    nombre = ""
    ejecutar = True

    while ejecutar:

        # colocar_fondo(condicion)

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

        colocar_texto("Su nombre buscador: ", 400, 50)
        rectangulo = pygame.Rect(100, 200, 700, 50)
        pygame.draw.rect(PANTALLA, COLORES["COLOR_RECTANGULO"], rectangulo, 2)

        nombre_a_colocar = TIPO_FUENTE.render(
            nombre, True, COLORES["COLOR_TEXTO"])
        PANTALLA.blit(nombre_a_colocar, (rectangulo.x + 5, rectangulo.y + 5))

        pygame.display.flip()

    return nombre
