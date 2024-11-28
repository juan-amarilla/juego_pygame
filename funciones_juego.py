# pylint: disable=no-member
import pygame
import random
from funciones_lectura_json import leer_objetos, guardar_datos
from clases_juego import Jugador, Objeto
from constantes_juego import SONIDO_BOMBA, SONIDO_TESORO, SONIDO_VIDA, BOMBAS_MAX, ALTO, ANCHO, NOMBRE_JUEGO, FONDO_ANCHO, VELOCIDAD_FONDO
from colores_juego import BLANCO, VERDE, ROJO
import json


def iniciar_juego(nombre, FONDO, FONDO_1, FONDO_2):
    # Inicialización de Pygame
    pygame.init()

    # Configuración de la pantalla

    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(f"{NOMBRE_JUEGO} - Jugador: {nombre}")

    # Cargar música de fondo
    pygame.mixer.music.load("recursos_juego/musica/musica_fondo.ogg")
    pygame.mixer.music.play(-1)  # -1 para reproducir en bucle
    # Llamar a la función cargar_objetos
    objetos, objetivos = cargar_objetos("objetos.json")

    # Creación del jugador
    jugador = Jugador()

    # # Bucle principal
    CORRIENDO = True
    reloj = pygame.time.Clock()

    try:
        while CORRIENDO:
            pantalla.blit(FONDO, (0, 0))

            # Manejo de eventos
            CORRIENDO = manejar_eventos()
            # Actualizar fondo
            FONDO_1, FONDO_2 = actualizar_fondo(
                pantalla, FONDO, FONDO_1, FONDO_2, VELOCIDAD_FONDO, FONDO_ANCHO)

            # Movimiento del jugador
            teclas = pygame.key.get_pressed()
            manejar_movimiento(jugador, teclas, objetos)
            jugador.aplicar_gravedad()

            # Manejo de colisiones
            manejar_colisiones(jugador, objetos, objetivos)

            # Dibujar elementos
            dibujar_elementos(pantalla, jugador, objetos, jugador.puntos,
                              jugador.vidas, pygame.font.Font(None, 36))

            # Verificar si perdió
            if jugador.vidas <= 0:
                mostrar_mensaje_perder(
                    pantalla, jugador, guardar_datos, ANCHO, ALTO, ROJO, nombre)
                return "perdio"

            # Verificar si ganó
            if len(objetivos) == 0:
                mostrar_mensaje_victoria(pantalla, "¡Ganaste!", VERDE,
                                         jugador.puntos, jugador.vidas, "ganaste", nombre)
                return "gano"

            # Actualizar pantalla
            pygame.display.flip()
            reloj.tick(30)

    except pygame.error as e:  # Errores relacionados con Pygame
        print(f"Error de Pygame: {e}")
    except FileNotFoundError as e:  # Archivos faltantes
        print(f"Archivo no encontrado: {e}")
    except ValueError as e:  # Valores inválidos
        print(f"Error de valor: {e}")

    pygame.quit()


def manejar_eventos():
    """Maneja eventos de entrada del usuario."""

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
    return True


def actualizar_fondo(pantalla, fondo, fondo_1, fondo_2, velocidad, ancho):
    """Actualiza la posición y dibuja el fondo."""
    fondo_1 -= velocidad
    fondo_2 -= velocidad

    pantalla.blit(fondo, (fondo_1, 0))
    pantalla.blit(fondo, (fondo_2, 0))

    if fondo_1 <= -ancho:
        fondo_1 = ancho
    if fondo_2 <= -ancho:
        fondo_2 = ancho

    return fondo_1, fondo_2


def manejar_movimiento(jugador, teclas, objetos):
    """Maneja el movimiento del jugador."""
    if teclas[pygame.K_LEFT]:
        jugador.mover(-5, 0, objetos)
    if teclas[pygame.K_RIGHT]:
        jugador.mover(5, 0, objetos)
    if teclas[pygame.K_UP]:
        jugador.mover(0, -5, objetos)
    if teclas[pygame.K_DOWN]:
        jugador.mover(0, 5, objetos)
    if teclas[pygame.K_a]:
        jugador.saltar()


def cargar_objetos(nombre_archivo):
    # Leer los datos del archivo JSON
    datos = leer_objetos(nombre_archivo)

    # Inicializar las listas
    objetos = []
    objetivos = []

    # Crear los objetos de acuerdo al archivo JSON
    for entrada in datos["objetos"]:
        tipo = entrada["tipo"]
        cantidad = entrada["cantidad"]
        for _ in range(cantidad):
            nuevo_objeto = Objeto(tipo)
            objetos.append(nuevo_objeto)
            if tipo == "tesoro" or tipo == "vida":
                # Agregar a la lista de objetivos
                objetivos.append(nuevo_objeto)

    # Crear bombas con diferentes direcciones
    for _ in range(cantidad):
        objetos.append(Objeto("bomba", direccion="vertical"))

    for _ in range(cantidad):  # 5 bombas de movimiento lateral
        objetos.append(Objeto("bomba", direccion="horizontal"))

    # Devolver las listas de objetos y objetivos
    return objetos, objetivos


def manejar_colisiones(jugador, objetos, objetivos):
    """Maneja las colisiones entre el jugador y los objetos."""
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
                objetos.remove(obj)
        # Generar nuevas bombas si es necesario
    generar_bombas(objetos, BOMBAS_MAX)


def dibujar_elementos(pantalla, jugador, objetos, puntos, vidas, fuente):
    """Dibuja los elementos del juego en pantalla."""
    jugador.dibujar(pantalla)

    for obj in objetos:
        obj.mover()
        obj.dibujar(pantalla)

    texto_puntos = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)
    pantalla.blit(texto_puntos, (10, 10))
    pantalla.blit(texto_vidas, (10, 50))


def mostrar_mensaje_perder(pantalla, jugador, guardar_datos, ANCHO, ALTO, ROJO, nombre):
    """
    Muestra el mensaje de "Game Over" en la pantalla junto con los puntos y vidas restantes.
    También guarda los datos en un archivo JSON.
    """
    # Fuente y texto principal
    fuente = pygame.font.Font(None, 72)
    texto_perder = fuente.render("¡Perdiste!", True, ROJO)

    # Obtener el ancho y alto del texto para centrarlo
    ancho_texto_perder = texto_perder.get_width()
    alto_texto_perder = texto_perder.get_height()

    # Dibujar el texto "¡Perdiste!" en el centro de la pantalla
    pantalla.blit(texto_perder, (ANCHO // 2 - ancho_texto_perder //
                  2, ALTO // 2 - alto_texto_perder // 2))

    # Dibujar los puntos
    fuente_puntos = pygame.font.Font(None, 48)
    texto_puntos = fuente_puntos.render(
        f"Puntos: {jugador.puntos}", True, ROJO)
    ancho_texto_puntos = texto_puntos.get_width()
    pantalla.blit(texto_puntos, (ANCHO // 2 - ancho_texto_puntos //
                  2, ALTO // 2 + alto_texto_perder // 2))

    # Dibujar las vidas
    fuente_vidas = pygame.font.Font(None, 48)
    texto_vidas = fuente_vidas.render(f"Vidas: {jugador.vidas}", True, ROJO)
    ancho_texto_vidas = texto_vidas.get_width()
    pantalla.blit(texto_vidas, (ANCHO // 2 - ancho_texto_vidas //
                  2, ALTO // 2 + alto_texto_perder // 2 + 50))

    # Actualizar la pantalla para mostrar los mensajes
    pygame.display.flip()

    # Esperar 3 segundos antes de continuar
    pygame.time.wait(3000)

    # Guardar datos en JSON
    guardar_datos("puntuaciones.json", {
        "nombre": nombre,
        "estado": "perdiste",
        "puntos": jugador.puntos,
        "vidas": jugador.vidas
    })


def mostrar_mensaje_victoria(pantalla, texto, color, puntos, vidas, estado, nombre):
    # Validar el color
    if not (isinstance(color, tuple) and len(color) == 3 and all(0 <= c <= 255 for c in color)):
        raise ValueError(
            "El color debe ser una tupla RGB válida (R, G, B) con valores entre 0 y 255.")

    # Fuente y texto principal
    fuente = pygame.font.Font(None, 72)
    texto_ganar = fuente.render(texto, True, color)

    # Obtener el ancho y alto del texto para centrarlo
    ancho_texto_ganar = texto_ganar.get_width()
    alto_texto_ganar = texto_ganar.get_height()

    # Dibujar el texto "¡Ganaste!" en el centro de la pantalla
    pantalla.blit(texto_ganar, (ANCHO // 2 - ancho_texto_ganar //
                  2, ALTO // 2 - alto_texto_ganar // 2))

    # Dibujar los puntos
    fuente_puntos = pygame.font.Font(None, 48)
    texto_puntos = fuente_puntos.render(f"Puntos: {puntos}", True, color)
    pantalla.blit(texto_puntos, (ANCHO // 2 - texto_puntos.get_width() //
                  2, ALTO // 2 + alto_texto_ganar // 2))

    # Dibujar las vidas
    fuente_vidas = pygame.font.Font(None, 48)
    texto_vidas = fuente_vidas.render(f"Vidas: {vidas}", True, color)
    pantalla.blit(texto_vidas, (ANCHO // 2 - texto_vidas.get_width() //
                  2, ALTO // 2 + alto_texto_ganar // 2 + 50))

    pygame.display.flip()
    pygame.time.wait(3000)

    # Guardar datos en JSON
    guardar_datos("puntuaciones.json", {
        "nombre": nombre,
        "estado": estado,
        "puntos": puntos,
        "vidas": vidas
    })


def generar_bombas(objetos, bombas_max):
    """
    Genera nuevas bombas si el número de bombas activas es menor al máximo permitido.

    :param objetos: Lista de objetos en el juego.
    :param max_bombas: Máximo número de bombas activas.
    """
    bombas_activas = []
    for obj in objetos:
        if obj.tipo == "bomba":
            bombas_activas.append(obj)
    while len(bombas_activas) < bombas_max:
        direccion = random.choice(["vertical", "horizontal"])
        nueva_bomba = Objeto("bomba", direccion=direccion)
        objetos.append(nueva_bomba)
        bombas_activas.append(nueva_bomba)


def mostrar_puntuaciones(pantalla, archivo_json, ANCHO, ALTO, COLOR_TEXTO, IMAGENES_FONDO):

    # Cargar las puntuaciones desde el archivo JSON
    try:
        with open(archivo_json, "r") as file:
            datos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = []  # Si no hay datos, inicializamos con una lista vacía

    # Ordenar por puntos de mayor a menor
    datos_ordenados = sorted(datos, key=lambda x: x["puntos"], reverse=True)

    # Configurar fuente
    fuente_titulo = pygame.font.Font(None, 72)  # Fuente grande para el título
    # Fuente más pequeña para los datos
    fuente_texto = pygame.font.Font(None, 36)

    # Dibujar el fondo
    pantalla.blit(IMAGENES_FONDO, (0, 0))

    # Mostrar título
    texto_titulo = fuente_titulo.render("Puntuaciones", True, COLOR_TEXTO)
    pantalla.blit(texto_titulo, (ANCHO // 2 -
                  texto_titulo.get_width() // 2, 50))

    # Mostrar las puntuaciones
    y_offset = 150  # Espacio inicial desde la parte superior
    espacio_entre_lineas = 40  # Espacio entre líneas

    for jugador in datos_ordenados:
        texto = f"{jugador['nombre']}: {
            jugador['puntos']} puntos, {jugador['vidas']} vidas"
        texto_render = fuente_texto.render(texto, True, COLOR_TEXTO)

        if y_offset + texto_render.get_height() > ALTO - 50:  # Verificar si hay espacio en la pantalla
            break  # No dibujar más si se sale de la pantalla

        pantalla.blit(texto_render, (ANCHO // 2 -
                      texto_render.get_width() // 2, y_offset))
        y_offset += espacio_entre_lineas

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar hasta que el jugador presione Escape
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                esperando = False  # Salir del bucle para volver al menú principal
