# pylint: disable=no-member
import pygame
from constantes_inicio import SONIDO_TECLADO_MENU, IMAGENES_FONDO
from funciones_menu import PANTALLA, COLORES
from funciones_juego import iniciar_juego, mostrar_puntuaciones
from constantes_juego import FONDO, FONDO_1, FONDO_2, ALTO, ANCHO
from funciones_pantalla import colocar_menu, colocar_nombre_pantalla


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
        mostrar_puntuaciones(PANTALLA, "puntuaciones.json", ANCHO,
                             ALTO, COLORES["COLOR_TEXTO"], IMAGENES_FONDO["PRIMER"])

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

    while ejecutar:

        # # Redibuja el fondo para limpiar la pantalla
        # PANTALLA.blit(FONDO_MENU, (0, 0))

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
