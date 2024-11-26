
from funciones_juego import iniciar_juego
from constantes_juego import FONDO, FONDO_1, FONDO_2


# def iniciar_juego(FONDO, FONDO_1, FONDO_2):
#     # Inicialización de Pygame
#     pygame.init()

#     # Configuración de la pantalla

#     pantalla = pygame.display.set_mode((ANCHO, ALTO))
#     pygame.display.set_caption(NOMBRE_JUEGO)

#     # Cargar música de fondo
#     pygame.mixer.music.load("recursos_juego/musica/musica_fondo.ogg")
#     pygame.mixer.music.play(-1)  # -1 para reproducir en bucle
#     # Llamar a la función cargar_objetos
#     objetos, objetivos = cargar_objetos("objetos.json")

#     # Creación del jugador
#     jugador = Jugador()

#     # # Bucle principal
#     CORRIENDO = True
#     reloj = pygame.time.Clock()

#     try:
#         while CORRIENDO:
#             pantalla.blit(FONDO, (0, 0))

#             # Manejo de eventos
#             CORRIENDO = manejar_eventos()
#             # Actualizar fondo
#             FONDO_1, FONDO_2 = actualizar_fondo(
#                 pantalla, FONDO, FONDO_1, FONDO_2, VELOCIDAD_FONDO, FONDO_ANCHO)

#             # Movimiento del jugador
#             teclas = pygame.key.get_pressed()
#             manejar_movimiento(jugador, teclas, objetos)
#             jugador.aplicar_gravedad()

#             # Manejo de colisiones
#             manejar_colisiones(jugador, objetos, objetivos)

#             # Dibujar elementos
#             dibujar_elementos(pantalla, jugador, objetos, jugador.puntos,
#                               jugador.vidas, pygame.font.Font(None, 36))

#             # Verificar si perdió
#             if jugador.vidas <= 0:
#                 mostrar_mensaje_perder(
#                     pantalla, jugador, guardar_datos, ANCHO, ALTO, ROJO)
#                 CORRIENDO = False

#             # Verificar si ganó
#             if len(objetivos) == 0:
#                 mostrar_mensaje_victoria(pantalla, "¡Ganaste!", VERDE,
#                                          jugador.puntos, jugador.vidas, "ganaste")
#                 CORRIENDO = False

#             # Actualizar pantalla
#             pygame.display.flip()
#             reloj.tick(30)

#     except pygame.error as e:  # Errores relacionados con Pygame
#         print(f"Error de Pygame: {e}")
#     except FileNotFoundError as e:  # Archivos faltantes
#         print(f"Archivo no encontrado: {e}")
#     except ValueError as e:  # Valores inválidos
#         print(f"Error de valor: {e}")

#     pygame.quit()


# iniciar_juego(FONDO, FONDO_1, FONDO_2)
iniciar_juego(FONDO, FONDO_1, FONDO_2)
