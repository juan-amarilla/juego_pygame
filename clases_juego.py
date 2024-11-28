import pygame
import random
from constantes_juego import (ANCHO, ALTO)


class Jugador:
    def __init__(self):
        self.x, self.y = ANCHO // 2, ALTO - 200  # Posición inicial cerca del suelo
        self.velocidad_y = 0
        self.en_suelo = False
        self.saltando = False
        self.vidas = 3
        self.puntos = 0
        self.imagen = pygame.image.load(
            "recursos_juego/imagenes/Explorador.png")
        self.imagen = pygame.transform.scale(self.imagen, (200, 200))

    def mover(self, dx, dy, objetos):

        nueva_x = self.x + dx
        nueva_y = self.y + dy

        # Verificar colisiones con objetos
        for obj in objetos:
            if self.colisiona_con(obj):
                print(f"Colisión con objeto de tipo: {obj.tipo}")

        # Limitar el movimiento a los bordes de la pantalla
        if 0 <= nueva_x <= ANCHO - 200:  # ANCHO menos el ancho del jugador
            self.x = nueva_x
        if 0 <= nueva_y <= ALTO - 200:  # ALTO menos la altura del jugador
            self.y = nueva_y

        # cambiar la imagen del jugador segun la posicion
        if dx > 0:  # Movimiento a la izquierda
            self.imagen = pygame.transform.flip(pygame.image.load(
                "recursos_juego/imagenes/Explorador.png"), True, False)
            self.imagen = pygame.transform.scale(self.imagen, (200, 200))
        elif dx < 0:  # Movimiento a la derecha
            self.imagen = pygame.image.load(
                "recursos_juego/imagenes/Explorador.png")
            self.imagen = pygame.transform.scale(self.imagen, (200, 200))

    def colisiona_con(self, objeto):
        """Verificar si el jugador colisiona con un objeto."""
        jugador_rect = pygame.Rect(self.x, self.y, 200, 200)
        objeto_rect = pygame.Rect(objeto.x, objeto.y, 50, 50)
        return jugador_rect.colliderect(objeto_rect)

    def saltar(self):
        if not self.saltando:  # Solo saltar si no esta ya en el aire
            self.saltando = True
            self.velocidad_y = -15  # Fuerza inicial del salto

    def aplicar_gravedad(self):
        if self.saltando:  # Aplica gravedad si no está en el suelo
            self.velocidad_y += 1  # Aceleración por gravedad
            self.y += self.velocidad_y

        if self.y >= ALTO - 200:  # suelo
            self.y = ALTO - 200
            self.saltando = False
            self.velocidad_y = 0  # Detener la caida
            self.en_suelo = True
        else:
            self.en_suelo = False  # No esta en el suelo si esta saltando

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))


class Objeto:
    def __init__(self, tipo_objeto, x=None, y=None, direccion="vertical"):
        # Usa coordenadas específicas si se proporcionan, o valores aleatorios en su defecto
        self.x = x if x is not None else random.randint(0, ANCHO - 50)
        self.y = y if y is not None else random.randint(0, ALTO - 50)
        self.tipo = tipo_objeto
        self.direccion = direccion

        # Velocidad según la dirección
        if tipo_objeto == "bomba":
            if self.direccion == "vertical":
                self.velocidad_y = random.randint(2, 5)
                self.velocidad_x = 0
            elif self.direccion == "horizontal":
                self.velocidad_x = random.randint(2, 5)
                self.velocidad_y = 0

        # Cargar imágenes según el tipo de objeto
        if self.tipo == "tesoro":
            self.imagen = pygame.image.load(
                "recursos_juego/imagenes/tesoro.png")
        elif self.tipo == "vida":
            self.imagen = pygame.image.load("recursos_juego/imagenes/vida.png")
        elif self.tipo == "bomba":
            self.imagen = pygame.image.load(
                "recursos_juego/imagenes/bomba.png")

        # Escalar la imagen al tamaño deseado (50x50 en este caso)
        self.imagen = pygame.transform.scale(self.imagen, (50, 50))

    def mover(self):
        if self.tipo == "bomba":
            if self.direccion == "vertical":
                # Movimiento vertical (caída)
                self.y += self.velocidad_y
                if self.y > ALTO:  # Reaparecer arriba si sale de la pantalla
                    self.y = random.randint(-50, -10)
                    self.x = random.randint(0, ANCHO - 50)
            elif self.direccion == "horizontal":
                # Movimiento horizontal (de izquierda a derecha)
                self.x += self.velocidad_x
                if self.x > ANCHO:  # Reaparecer en el lado izquierdo si sale de la pantalla
                    self.x = random.randint(-50, -10)
                    self.y = random.randint(0, ALTO - 50)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))
