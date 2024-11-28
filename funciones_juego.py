import pygame
import random
from funciones_lectura_json import (leer_objetos, guardar_datos)
from funciones_archivos import agregar_jugador
from clases_juego import (Jugador, Objeto)
from constantes_juego import (SONIDO_BOMBA, SONIDO_TESORO, SONIDO_VIDA, BOMBAS_MAX, ALTO, ANCHO)
from constantes import PANTALLA
from colores_juego import (BLANCO, VERDE, ROJO)
from constantes_juego import (ANCHO, ALTO, FONDO_ANCHO, VELOCIDAD_FONDO)


def iniciar_juego(nombre: str, FONDO, FONDO_1: int, FONDO_2: int) -> str:
    """
    Inicia el juego

    Args:
    nombre(str)
    FONDO(surface)
    FONDO_1(int)
    FONDO_2(int)

    Return:
    retornara gano o perdio
    """

    pygame.mixer.music.load("recursos_juego/musica/musica_fondo.ogg")
    pygame.mixer.music.play(-1)  # -1 para reproducir en bucle
    
    objetos, objetivos = cargar_objetos("objetos.json")

    jugador = Jugador()

    CORRIENDO = True
    reloj = pygame.time.Clock()

    try:
        while CORRIENDO:

            PANTALLA.blit(FONDO, (0, 0))

            CORRIENDO = manejar_eventos()

            FONDO_1, FONDO_2 = actualizar_fondo(PANTALLA, FONDO, FONDO_1, FONDO_2, VELOCIDAD_FONDO, FONDO_ANCHO)

            teclas = pygame.key.get_pressed()
            manejar_movimiento(jugador, teclas, objetos)
            jugador.aplicar_gravedad()

            manejar_colisiones(jugador, objetos, objetivos)

            dibujar_elementos(PANTALLA, jugador, objetos, jugador.puntos,
                              jugador.vidas, pygame.font.Font(None, 36))

            if jugador.vidas <= 0:
                agregar_jugador("puntuaciones.txt", f"{nombre} -- {jugador.puntos * jugador.vidas}")
                mostrar_mensaje_perder(PANTALLA, jugador, guardar_datos, ANCHO, ALTO, ROJO)
                return "perdio"

            if len(objetivos) == 0:
                agregar_jugador("puntuaciones.txt", f"{nombre} -- {jugador.puntos * jugador.vidas}")
                mostrar_mensaje_victoria(PANTALLA, "¡Ganaste!", VERDE, jugador.puntos, jugador.vidas, "ganaste")
                return "gano"

            pygame.display.flip()
            reloj.tick(30)

    except pygame.error as e:  # Errores relacionados con Pygame
        print(f"Error de Pygame: {e}")
    except FileNotFoundError as e:  # Archivos faltantes
        print(f"Archivo no encontrado: {e}")
    except ValueError as e:  # Valores inválidos
        print(f"Error de valor: {e}")


def manejar_eventos() -> bool:
    """
    Manejara un evento

    Args:
    None

    Return:
    False si sale o True que no saldra
    """

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
    return True


def actualizar_fondo(pantalla, fondo, fondo_1: int, fondo_2: int, velocidad: int, ancho: int):
    """
    Actualizara el fondo de manera dinamica

    Args:
    pantalla(surface)
    fondo(surface)
    fondo_1(int)
    fondo_2(int)
    velocidad(int)
    ancho(int)

    Return:
    Retorna un doble entero
    """

    fondo_1 -= velocidad
    fondo_2 -= velocidad

    pantalla.blit(fondo, (fondo_1, 0))
    pantalla.blit(fondo, (fondo_2, 0))

    if fondo_1 <= -ancho:
        fondo_1 = ancho
    if fondo_2 <= -ancho:
        fondo_2 = ancho

    return fondo_1, fondo_2


def manejar_movimiento(jugador, teclas: list, objetos: list) -> None:
    """
    Podras manejar el personaje con las flechas

    Args:
    jugador(class)
    teclas(list)
    objetos(list)

    Return:
    None
    """
    
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


def cargar_objetos(nombre_archivo: str):
    """
    Cargaras todos los objetos

    Args:
    nombre_archivo(str)

    Return:
    Retorna dos listas
    """
    
    datos = leer_objetos(nombre_archivo)

    objetos = []
    objetivos = []
   
    for entrada in datos["objetos"]:
        tipo = entrada["tipo"]
        cantidad = entrada["cantidad"]
        for _ in range(cantidad):
            nuevo_objeto = Objeto(tipo)
            objetos.append(nuevo_objeto)
            if tipo == "tesoro" or tipo == "vida":
                
                objetivos.append(nuevo_objeto)

    for _ in range(cantidad):
        objetos.append(Objeto("bomba", direccion="vertical"))

    for _ in range(cantidad):  # 5 bombas de movimiento lateral
        objetos.append(Objeto("bomba", direccion="horizontal"))

    return objetos, objetivos


def manejar_colisiones(jugador, objetos: list, objetivos: list) -> None:
    """
    Verificaras el tema de colisiones

    Args:
    jugador(class)
    objetos(list)
    objetivos(list)

    Return:
    None
    """
    
    for obj in objetos[:]: 

        jugador_rect = pygame.Rect(jugador.x, jugador.y, 200, 200)
        objeto_rect = pygame.Rect(obj.x, obj.y, 50, 50)

        if jugador_rect.colliderect(objeto_rect):
            if obj.tipo == "tesoro":
                jugador.puntos += 10
                SONIDO_TESORO.play()
                objetos.remove(obj)

                for objetivo in objetivos:
                    if objetivo == obj:
                        objetivos.remove(objetivo)
                        break  
            elif obj.tipo == "vida":
                jugador.vidas += 1
                SONIDO_VIDA.play()
                objetos.remove(obj)
    
                for objetivo in objetivos:
                    if objetivo == obj:
                        objetivos.remove(objetivo)
                        break 
            elif obj.tipo == "bomba":
                jugador.vidas -= 1
                SONIDO_BOMBA.play()
                objetos.remove(obj)
        
    generar_bombas(objetos, BOMBAS_MAX)


def dibujar_elementos(pantalla, jugador, objetos: list, puntos: int, vidas: int, fuente) -> None:
    """
    Dibujas los elementos necesarios

    Args:
    pantalla(surface)
    jugador(class)
    objetos(list)
    puntos(int)
    vidas(int)
    fuente(font)

    Return:
    None
    """

    jugador.dibujar(pantalla)

    for obj in objetos:
        obj.mover()
        obj.dibujar(pantalla)

    texto_puntos = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)
    pantalla.blit(texto_puntos, (10, 10))
    pantalla.blit(texto_vidas, (10, 50))


def mostrar_mensaje_perder(pantalla, jugador, guardar_datos, ANCHO: int, ALTO: int, ROJO: tuple) -> None:
    """
    Mostras el mensaje cuando perdiste

    Args:
    pantalla(surface)
    jugador(class)
    guardar_datos(function)
    ANCHO(int)
    ALTO(int)
    ROJO(tuple)

    Return:
    None
    """
    
    fuente = pygame.font.Font(None, 72)
    texto_perder = fuente.render("¡Perdiste!", True, ROJO)

    ancho_texto_perder = texto_perder.get_width()
    alto_texto_perder = texto_perder.get_height()

    pantalla.blit(texto_perder, (ANCHO // 2 - ancho_texto_perder //
                  2, ALTO // 2 - alto_texto_perder // 2))

    fuente_puntos = pygame.font.Font(None, 48)
    texto_puntos = fuente_puntos.render(
        f"Puntos: {jugador.puntos}", True, ROJO)
    ancho_texto_puntos = texto_puntos.get_width()
    pantalla.blit(texto_puntos, (ANCHO // 2 - ancho_texto_puntos //
                  2, ALTO // 2 + alto_texto_perder // 2))

    fuente_vidas = pygame.font.Font(None, 48)
    texto_vidas = fuente_vidas.render(f"Vidas: {jugador.vidas}", True, ROJO)
    ancho_texto_vidas = texto_vidas.get_width()
    pantalla.blit(texto_vidas, (ANCHO // 2 - ancho_texto_vidas //
                  2, ALTO // 2 + alto_texto_perder // 2 + 50))

    pygame.display.flip()

    pygame.time.wait(3000)

    guardar_datos("resultado.json", {
        "estado": "perdiste",
        "puntos": jugador.puntos,
        "vidas": jugador.vidas
    })


def mostrar_mensaje_victoria(pantalla, texto: str, color: tuple, puntos: int, vidas: int, estado: str) -> None:
    """
    Mostras el mensaje cuando ganaste

    Args:
    pantalla(surface)
    texto(str)
    color(tuple)
    puntos(int)
    vidas(int)
    estado(str)

    Return:
    None
    """

    if not (isinstance(color, tuple) and len(color) == 3 and all(0 <= c <= 255 for c in color)):
        raise ValueError(
            "El color debe ser una tupla RGB válida (R, G, B) con valores entre 0 y 255.")

    fuente = pygame.font.Font(None, 72)
    texto_ganar = fuente.render(texto, True, color)

    ancho_texto_ganar = texto_ganar.get_width()
    alto_texto_ganar = texto_ganar.get_height()

    pantalla.blit(texto_ganar, (ANCHO // 2 - ancho_texto_ganar //
                  2, ALTO // 2 - alto_texto_ganar // 2))

    fuente_puntos = pygame.font.Font(None, 48)
    texto_puntos = fuente_puntos.render(f"Puntos: {puntos}", True, color)
    pantalla.blit(texto_puntos, (ANCHO // 2 - texto_puntos.get_width() //
                  2, ALTO // 2 + alto_texto_ganar // 2))

    fuente_vidas = pygame.font.Font(None, 48)
    texto_vidas = fuente_vidas.render(f"Vidas: {vidas}", True, color)
    pantalla.blit(texto_vidas, (ANCHO // 2 - texto_vidas.get_width() //
                  2, ALTO // 2 + alto_texto_ganar // 2 + 50))

    pygame.display.flip()
    pygame.time.wait(3000)

    guardar_datos("resultado.json", {
        "estado": estado,
        "puntos": puntos,
        "vidas": vidas
    })


def generar_bombas(objetos: list, bombas_max: int) -> None:
    """
    Generas bombas al azar en cualquier coordenadas

    Args:
    objetos(list)
    bombas_max(int)

    Return:
    None
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
