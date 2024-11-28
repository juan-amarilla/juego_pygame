import pygame
import random
from constantes_juego import (ANCHO, ALTO)


class Jugador:
    def __init__(self):
        """
        Inicializas los valores

        Args:
        None

        Return:
        None
        """
        self.x, self.y = ANCHO // 2, ALTO - 200
        self.velocidad_y = 0
        self.en_suelo = False
        self.saltando = False
        self.vidas = 3
        self.puntos = 0
        self.imagen = pygame.image.load("recursos_juego/imagenes/Explorador.png")
        self.imagen = pygame.transform.scale(self.imagen, (200, 200))

    def mover(self, dx: int, dy: int, objetos: list) -> None:
        """
        Moveras un personaje en base de coordenadas

        Args:
        dx(int)
        dx(int)
        objetos(list)

        Return:
        None
        """

        nueva_x = self.x + dx
        nueva_y = self.y + dy

        for obj in objetos:
            if self.colisiona_con(obj):
                print(f"Colisión con objeto de tipo: {obj.tipo}")

        if 0 <= nueva_x <= ANCHO - 200:  
            self.x = nueva_x
        if 0 <= nueva_y <= ALTO - 200: 
            self.y = nueva_y

        if dx > 0:  
            self.imagen = pygame.transform.flip(pygame.image.load(
                "recursos_juego/imagenes/Explorador.png"), True, False)
            self.imagen = pygame.transform.scale(self.imagen, (200, 200))
        elif dx < 0:
            self.imagen = pygame.image.load(
                "recursos_juego/imagenes/Explorador.png")
            self.imagen = pygame.transform.scale(self.imagen, (200, 200))

    def colisiona_con(self, objeto) -> bool:
        """
        Aca verificas una colision por el tema del personaje

        Args:
        objeto(class)

        Return:
        Retornara true si colisiona o False si no colisiona
        """
        jugador_rect = pygame.Rect(self.x, self.y, 200, 200)
        objeto_rect = pygame.Rect(objeto.x, objeto.y, 50, 50)
        return jugador_rect.colliderect(objeto_rect)

    def saltar(self) -> None:
        """
        Aca verificas el tema de salto

        Args:
        None

        Return:
        None
        """
        if not self.saltando:  
            self.saltando = True
            self.velocidad_y = -15  

    def aplicar_gravedad(self) -> None:
        """
        Aca verificas el tema de la gravedad

        Args:
        None

        Return:
        None
        """
        if self.saltando:  
            self.velocidad_y += 1
            self.y += self.velocidad_y

        if self.y >= ALTO - 200:  
            self.y = ALTO - 200
            self.saltando = False
            self.velocidad_y = 0  
            self.en_suelo = True
        else:
            self.en_suelo = False

    def dibujar(self, pantalla) -> None:
        """
        Aca dibujas la imagen

        Args:
        pantalla(surface)

        Return:
        None
        """
        pantalla.blit(self.imagen, (self.x, self.y))


class Objeto:
    def __init__(self, tipo_objeto: str, x=None, y=None, direccion="vertical") -> None:
        """
        Aca inicializas los valores de objeto determinado

        Args:
        tipo_objeto(str)
        x(int, opcional)
        y(int, opcional)
        direccion(str)

        Return:
        None
        """

        self.x = x if x is not None else random.randint(0, ANCHO - 50)
        self.y = y if y is not None else random.randint(0, ALTO - 50)
        self.tipo = tipo_objeto
        self.direccion = direccion

        if tipo_objeto == "bomba":
            if self.direccion == "vertical":
                self.velocidad_y = random.randint(2, 5)
                self.velocidad_x = 0
            elif self.direccion == "horizontal":
                self.velocidad_x = random.randint(2, 5)
                self.velocidad_y = 0

        if self.tipo == "tesoro":
            self.imagen = pygame.image.load(
                "recursos_juego/imagenes/tesoro.png")
        elif self.tipo == "vida":
            self.imagen = pygame.image.load("recursos_juego/imagenes/vida.png")
        elif self.tipo == "bomba":
            self.imagen = pygame.image.load(
                "recursos_juego/imagenes/bomba.png")

        self.imagen = pygame.transform.scale(self.imagen, (50, 50))

    def mover(self) -> None:
        """
        Aca moveras el objeto

        Args:
        None

        Return:
        None
        """
        if self.tipo == "bomba":
            if self.direccion == "vertical":
                self.y += self.velocidad_y
                if self.y > ALTO:
                    self.y = random.randint(-50, -10)
                    self.x = random.randint(0, ANCHO - 50)
            elif self.direccion == "horizontal":
                self.x += self.velocidad_x
                if self.x > ANCHO:
                    self.x = random.randint(-50, -10)
                    self.y = random.randint(0, ALTO - 50)

    def dibujar(self, pantalla) -> None:
        """
        Aca dibujaras el objeto

        Args:
        pantalla(surface)

        Return:
        None
        """
        
        pantalla.blit(self.imagen, (self.x, self.y))
