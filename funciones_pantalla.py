import pygame
from funciones_menu import (colocar_rectangulo, colocar_texto, colocar_opciones)
from constantes import (TITULO, TIPO_FUENTE, COLORES, PANTALLA, IMAGENES_FONDO)

def colocar_fondo(condicion: int) -> None:
    """
    Coloca el fondo de imagen dependiendo de la condicion

    Args:
    condicion(int)

    Returns:
    None
    """

    if condicion == 1:

        PANTALLA.blit(IMAGENES_FONDO['PRIMER'], (0, 0))
        PANTALLA.blit(IMAGENES_FONDO['SEGUNDO'], (0, 0))
        PANTALLA.blit(IMAGENES_FONDO['TERCER'], (0, 0))
        PANTALLA.blit(IMAGENES_FONDO['CUARTO'], (0, -180))

    else:

        pass
        

def colocar_menu() -> list:
    """
    Coloca el fondo de imagen de menu

    Args:
    None

    Returns:
    Retorna los rectangulos necesarios para decorar el menu
    """

    colocar_fondo(1)
    colocar_rectangulo(35, 80, 750, 50)
    colocar_texto(TITULO, 400, 100)
    rectangulos = colocar_opciones()
    pygame.display.flip()
    pygame.time.Clock().tick(5)

    return rectangulos

def colocar_puntuaciones(lineas: list, vertical: int, posicion: int) -> None:
    """
    Coloca el fondo de imagen de puntuaciones

    Args:
    lineas(list)
    vertical(int)
    posicion(int)

    Returns:
    None
    """

    colocar_fondo(1)

    for indice, linea in enumerate(lineas):
        texto = TIPO_FUENTE.render(linea.strip(), True, COLORES["COLOR_TEXTO"])
        PANTALLA.blit(texto, (400 - texto.get_width() // 2, vertical +  indice * posicion - texto.get_height() // 2))

    colocar_texto("Puntuaciones: ", 400, 100)
    colocar_texto("Pulse -> Esc -- para volver al menu", 400, 50)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

def colocar_nombre_pantalla(nombre) -> None:
    """
    Coloca el fondo de imagen de ingresar nombre

    Args:
    nombre(str)

    Returns:
    Retorna el nombre ingresado mostrado en la pantalla
    """

    colocar_fondo(1)
    colocar_texto("Su nombre buscador: ", 400, 50)
    rectangulo = pygame.Rect(100, 200, 700, 50)
    pygame.draw.rect(PANTALLA, COLORES["COLOR_RECTANGULO"], rectangulo, 2)
    nombre_a_colocar = TIPO_FUENTE.render(nombre, True, COLORES["COLOR_TEXTO"])
    PANTALLA.blit(nombre_a_colocar, (rectangulo.x + 5, rectangulo.y + 5))
    pygame.display.flip()

    return nombre


    