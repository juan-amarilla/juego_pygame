from constantes import *

def colocar_texto(texto: str, x: int, y: int) -> None:
    """
    Coloca texto en la posicion indicada(x, y)

    Args:
    texto(str)
    x(int)
    y(int)

    Returns:
    None
    """

    resultado = TIPO_FUENTE.render(texto, True, COLORES["COLOR_TEXTO"])
    PANTALLA.blit(resultado, (x - resultado.get_width() // 2, y - resultado.get_height() // 2))

def colocar_rectangulo(x: int, y: int, ancho: int, altura: int) -> None:
    """
    Coloca un rentangulo en la posicion indicada(x, y), ademas con su ancho y altura

    Args:
    x(int)
    y(int)
    ancho(int)
    altura(int)

    Returns:
    None
    """

    rectangulo = pygame.Rect(x, y, ancho, altura)
    pygame.draw.rect(PANTALLA, COLORES["COLOR_RECTANGULO"], rectangulo, 2)

def colocar_opciones():
    """
    Coloca varias opciones en formato menu

    Args:
    None

    Returns:
    Retorna cierta cantidad de rectangulos
    """

    rectangulos = []

    for i, opcion in enumerate(OPCIONES):

        rectangulo = pygame.Rect(200, VERTICAL + i * POSICION, 400, 50)
        pygame.draw.rect(PANTALLA, COLORES["COLOR_RECTANGULO"], rectangulo, 2)

        colocar_texto(opcion, rectangulo.centerx, rectangulo.centery)

        rectangulos.append(rectangulo)

    return rectangulos

def colocar_fondo(condicion: int) -> None:
    """
    Coloca el fondo de imagen dependiendo de la condicion

    Args:
    condicion(int)

    Returns:
    None
    """

    if condicion == 1:

        PANTALLA.blit(IMAGENES['PRIMER'], (0, 0))
        PANTALLA.blit(IMAGENES['SEGUNDO'], (0, 0))
        PANTALLA.blit(IMAGENES['TERCER'], (0, 0))
        PANTALLA.blit(IMAGENES['CUARTO'], (0, -180))

    else:

        pass