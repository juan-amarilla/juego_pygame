from constantes import *
from funciones_menu import *

def leer_archivo(ruta: str, ejecutar: bool, vertical: int, posicion: int) -> None:
    """
    Lee el archivo

    Args:
    ruta(str)
    ejecutar(bool)
    vertical(int)
    posicion(int)

    Returns:
    None
    """

    condicion = 1

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    while ejecutar:

        colocar_fondo(condicion)
        colocar_texto("Puntuaciones: ", 400, 100)
        colocar_texto("Pulse -> Esc -- para volver al menu", 400, 50)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutar = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    SONIDO_TECLADO_MENU.play()
                    ejecutar = False

        for indice, linea in enumerate(lineas):
            texto = TIPO_FUENTE.render(linea.strip(), True, COLORES["COLOR_TEXTO"])
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