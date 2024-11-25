from constantes import (pygame, SONIDO_TECLADO_MENU, COLORES, PANTALLA)
from funciones_menu import (colocar_fondo, colocar_texto)

def leer_archivo(ruta: str, ejecutar: bool, fuente, vertical: int, posicion: int) -> None:
    """
    Lee el archivo

    Args:
    ruta(str)
    ejecutar(bool)
    fuente(font)
    vertical(int)
    posicion(int)

    Returns:
    None
    """

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    while ejecutar:

        colocar_fondo()
        colocar_texto(fuente, "Puntuaciones: ", 400, 100)
        colocar_texto(fuente, "Pulse -> Esc -- para volver al menu", 400, 50)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutar = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    SONIDO_TECLADO_MENU.play()
                    ejecutar = False

        for indice, linea in enumerate(lineas):
            texto = fuente.render(linea.strip(), True, COLORES["COLOR_TEXTO"])
            PANTALLA.blit(texto, (400 - texto.get_width() // 2, vertical +  indice * posicion - texto.get_height() // 2))

        pygame.display.flip()
        pygame.time.Clock().tick(60)
                
    return ejecutar

def agregar_jugador(ruta: str, jugador: str) -> None:
    """
    Agrega un jugador con su puntuacion en el archivo ya elegido

    Args:
    ruta(str)
    jugador(str)

    Returns:
    None
    """

    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(jugador + "\n")