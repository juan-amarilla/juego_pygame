from constantes import *

def iniciar_con_musica(ruta: str) -> None:
    """
    Inicias la aplicacion con una musica elegida 

    Args:
    ruta(str)

    Returns:
    None
    """

    pygame.init()
    pygame.mixer.music.load(ruta)


def colocar_titulo(titulo: str) -> str:
    """
    Colocas un titulo a la aplicacion

    Args:
    titulo(str)

    Returns:
    None
    """

    pygame.display.set_caption(titulo)

    return titulo

def ajustar(ajustado: int) -> None:
    """
    Ajustas el volumen de la musica

    Args:
    ajustado(int)

    Returns:
    None
    """

    pygame.mixer.music.play(ajustado)


def renderizar(fuente, texto: str) -> str:
    """
    Renderizas un texto

    Args:
    fuente(font)
    texto(str)

    Returns:
    Retornas un texto renderizado
    """

    resultado = fuente.render(texto, True, COLORES["COLOR_TEXTO"])

    return resultado

def colocar_texto(fuente, texto: str, x: int, y: int) -> None:
    """
    Coloca texto en la posicion indicada(x, y)

    Args:
    fuente(font)
    texto(str)
    x(int)
    y(int)

    Returns:
    None
    """

    resultado = renderizar(fuente, texto)
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

def colocar_opciones(fuente):
    """
    Coloca varias opciones en formato menu

    Args:
    fuente(font)

    Returns:
    Retorna cierta cantidad de rectangulos
    """

    rectangulos = []

    for i, opcion in enumerate(OPCIONES):

        rectangulo = pygame.Rect(200, VERTICAL + i * POSICION, 400, 50)
        pygame.draw.rect(PANTALLA, COLORES["COLOR_RECTANGULO"], rectangulo, 2)

        colocar_texto(fuente, opcion, rectangulo.centerx, rectangulo.centery)

        rectangulos.append(rectangulo)

    return rectangulos

def colocar_fondo() -> None:
    """
    Coloca el fondo de menu

    Args:
    None

    Returns:
    None
    """

    PANTALLA.blit(IMAGENES["PRIMER"], (0, 0))
    PANTALLA.blit(IMAGENES["SEGUNDO"], (0, 0))
    PANTALLA.blit(IMAGENES["TERCER"], (0, 0))
    PANTALLA.blit(IMAGENES["CUARTO"], (0, -180))