from constantes import (pygame, SONIDO_TECLADO_MENU, PANTALLA, COLORES, 
FONDO, VELOCIDAD_FONDO, FONDO_ANCHO, SONIDO_TESORO, SONIDO_VIDA, 
SONIDO_BOMBA, BOMBAS_MAX, ANCHO, ALTO, FONDO_1, NOMBRE_JUEGO)
from colores import *
from funciones_archivos import leer_archivo
from funciones_menu import ajustar, colocar_fondo, colocar_rectangulo, colocar_texto, colocar_opciones
from lectura_json import guardar_datos
from clases import Jugador
from funciones_jugando import generar_bombas, cargar_objetos

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
        jugar(nombre)
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

def jugar(nombre):

    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(NOMBRE_JUEGO)

    # Cargar música de fondo
    pygame.mixer.music.stop()
    pygame.mixer.music.load("recursos/musica/musica_fondo.ogg")
    pygame.mixer.music.play(-1)  # -1 para reproducir en bucle

    # Creación del jugador
    jugador = Jugador()

    # Llamar a la función cargar_objetos
    objetos, objetivos = cargar_objetos("objetos.json")

    # Bucle principal
    CORRIENDO = True
    reloj = pygame.time.Clock()
    try:

        while CORRIENDO:
            pantalla.blit(FONDO, (0, 0))

            # Eventos y controles
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    CORRIENDO = False

            FONDO_1 -= VELOCIDAD_FONDO
            FONDO_2 -= VELOCIDAD_FONDO

            pantalla.blit(FONDO, (FONDO_1, 0))
            pantalla.blit(FONDO, (FONDO_2, 0))

            if FONDO_1 <= -FONDO_ANCHO:
                FONDO_1 = FONDO_ANCHO
            if FONDO_2 <= -FONDO_ANCHO:
                FONDO_2 = FONDO_ANCHO

            teclas = pygame.key.get_pressed()

            # Movimiento hacia la izquierda y derecha con las flechas
            if teclas[pygame.K_LEFT]:
                jugador.mover(-5, 0, objetos)
            if teclas[pygame.K_RIGHT]:
                jugador.mover(5, 0, objetos)
            if teclas[pygame.K_UP]:
                jugador.mover(0, -5, objetos)
            if teclas[pygame.K_DOWN]:
                jugador.mover(0, 5, objetos)
            if teclas[pygame.K_a]:  # Salto
                jugador.saltar()

            jugador.aplicar_gravedad()

            # Detección de colisiones
            for obj in objetos[:]:  # Iteramos sobre una copia para eliminar objetos sin problemas
                # Calculamos la colisión con un rectángulo
                jugador_rect = pygame.Rect(jugador.x, jugador.y, 200, 200)
                objeto_rect = pygame.Rect(obj.x, obj.y, 50, 50)

                if jugador_rect.colliderect(objeto_rect):
                    if obj.tipo == "tesoro":
                        jugador.puntos += 10
                        SONIDO_TESORO.play()
                        objetos.remove(obj)
                        # Eliminar de la lista de objetivos
                        for objetivo in objetivos:
                            if objetivo == obj:
                                objetivos.remove(objetivo)
                                break  # Romper el bucle ya que hemos encontrado y eliminado el objetivo
                    elif obj.tipo == "vida":
                        jugador.vidas += 1
                        SONIDO_VIDA.play()
                        objetos.remove(obj)
                        # Eliminar de la lista de objetivos
                        for objetivo in objetivos:
                            if objetivo == obj:
                                objetivos.remove(objetivo)
                                break  # Romper el bucle ya que hemos encontrado y eliminado el objetivo
                    elif obj.tipo == "bomba":
                        jugador.vidas -= 1
                        SONIDO_BOMBA.play()
                        objetos.remove(obj)  # Eliminar la bomba de objetos
            # Generar nuevas bombas si es necesario
            generar_bombas(objetos, BOMBAS_MAX)

            for obj in objetos:
                obj.mover()  # Mueve solo si el objeto lo soporta (bomba)
                obj.dibujar(pantalla)

            # Dibuja el jugador y objetos
            jugador.dibujar(pantalla)
            for obj in objetos:
                obj.dibujar(pantalla)

                # Mostrar puntos y vidas en pantalla
            fuente = pygame.font.Font(None, 36)
            texto_puntos = fuente.render(f"Puntos: {jugador.puntos}", True, BLANCO)
            texto_vidas = fuente.render(f"Vidas: {jugador.vidas}", True, BLANCO)
            pantalla.blit(texto_puntos, (10, 10))
            pantalla.blit(texto_vidas, (10, 50))

            # Terminar el juego si las vidas llegan a cero
            if jugador.vidas <= 0:
                fuente = pygame.font.Font(None, 72)
                texto_perder = fuente.render("¡Perdiste!", True, ROJO)

                # Obtener el ancho y alto del texto para centrarlo
                ancho_texto_perder = texto_perder.get_width()
                alto_texto_perder = texto_perder.get_height()

                # Dibujar el texto "¡Perdiste!" en el centro de la pantalla
                pantalla.blit(texto_perder, (ANCHO // 2 - ancho_texto_perder //
                            2, ALTO // 2 - alto_texto_perder // 2))

                # Ahora los puntos
                fuente_puntos = pygame.font.Font(None, 48)
                texto_puntos = fuente_puntos.render(
                    f"Puntos: {jugador.puntos}", True, ROJO)

                # Obtener el ancho y alto del texto de los puntos para centrarlo
                ancho_texto_puntos = texto_puntos.get_width()
                alto_texto_puntos = texto_puntos.get_height()

                # Dibujar el texto de los puntos debajo de "¡Perdiste!"
                pantalla.blit(texto_puntos, (ANCHO // 2 - ancho_texto_puntos //
                            2, ALTO // 2 + alto_texto_perder // 2))

                # Ahora las vidas
                fuente_vidas = pygame.font.Font(None, 48)
                texto_vidas = fuente_vidas.render(
                    f"Vidas: {jugador.vidas}", True, ROJO)

                # Obtener el ancho y alto del texto de las vidas para centrarlo
                ancho_texto_vidas = texto_vidas.get_width()
                alto_texto_vidas = texto_vidas.get_height()

                # Dibujar el texto de las vidas debajo de los puntos
                pantalla.blit(texto_vidas, (ANCHO // 2 - ancho_texto_vidas //
                            2, ALTO // 2 + alto_texto_perder // 2 + alto_texto_puntos))

                pygame.display.flip()
                # Iniciar un temporizador para dar tiempo al jugador de ver el mensaje
                tiempo_espera = pygame.time.get_ticks()  # Capturamos el tiempo actual

                while pygame.time.get_ticks() - tiempo_espera < 3000:  # Esperamos 3 segundos
                    # Mantenemos el bucle de eventos para que no se cierre inmediatamente
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            CORRIENDO = False
                            break
                    pygame.display.flip()  # Seguimos actualizando la pantalla durante los 3 segundos
                    # Guardar datos en JSON
                guardar_datos("resultado.json", {
                    "estado": "perdiste",
                    "puntos": jugador.puntos,
                    "vidas": jugador.vidas
                })

                CORRIENDO = False
            # Verificamos si Gano
            if len(objetivos) == 0:
                fuente = pygame.font.Font(None, 72)
                texto_ganar = fuente.render("¡Ganaste!", True, VERDE)

                # Obtener el ancho y alto del texto para centrarlo
                ancho_texto_ganar = texto_ganar.get_width()
                alto_texto_ganar = texto_ganar.get_height()

                # Dibujar el texto "¡Ganaste!" en el centro de la pantalla
                pantalla.blit(texto_ganar, (ANCHO // 2 - ancho_texto_ganar //
                            2, ALTO // 2 - alto_texto_ganar // 2))

                # Ahora los puntos
                fuente_puntos = pygame.font.Font(None, 48)
                texto_puntos = fuente_puntos.render(
                    f"Puntos: {jugador.puntos}", True, VERDE)

                # Obtener el ancho y alto del texto de los puntos para centrarlo
                ancho_texto_puntos = texto_puntos.get_width()
                alto_texto_puntos = texto_puntos.get_height()

                # Dibujar el texto de los puntos debajo de "¡Ganaste!"
                pantalla.blit(texto_puntos, (ANCHO // 2 - ancho_texto_puntos //
                            2, ALTO // 2 + alto_texto_ganar // 2))

                # Ahora las vidas
                fuente_vidas = pygame.font.Font(None, 48)
                texto_vidas = fuente_vidas.render(
                    f"Vidas: {jugador.vidas}", True, VERDE)

                # Obtener el ancho y alto del texto de las vidas para centrarlo
                ancho_texto_vidas = texto_vidas.get_width()
                alto_texto_vidas = texto_vidas.get_height()

                # Dibujar el texto de las vidas debajo de los puntos
                pantalla.blit(texto_vidas, (ANCHO // 2 - ancho_texto_vidas //
                            2, ALTO // 2 + alto_texto_ganar // 2 + alto_texto_puntos))

                pygame.display.flip()
                pygame.time.wait(3000)  # Espera 3 segundos antes de salir

                # Guardar datos en JSON
                guardar_datos("resultado.json", {
                    "estado": "ganaste",
                    "puntos": jugador.puntos,
                    "vidas": jugador.vidas
                })
                CORRIENDO = False

            # Actualización de pantalla
            pygame.display.flip()
            reloj.tick(30)
    except Exception as e:
        print(f"Error inesperado: {e}")

    pygame.quit()