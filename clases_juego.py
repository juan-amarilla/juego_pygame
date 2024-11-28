"""
Módulo que define las clases del jugador y los objetos del juego.

Este módulo contiene la definición de las clases `Jugador` y `Objeto`, que son esenciales
para la mecánica del juego. La clase `Jugador` maneja la lógica del movimiento, saltos, 
colisiones y dibujo del jugador en pantalla, mientras que la clase `Objeto` define los 
objetos interactivos del juego, como bombas, tesoros y vidas. Cada objeto tiene su propia 
lógica de movimiento y comportamiento según su tipo.

Clases:
    - Jugador: Define las propiedades y comportamientos del jugador, como el movimiento, 
      saltos, colisiones y la actualización de su estado.
    - Objeto: Define los objetos interactivos en el juego, como bombas y tesoros, con 
      comportamientos específicos, como la caída o el movimiento horizontal.
"""

import pygame
import random
from constantes_juego import ANCHO, ALTO


class Jugador:
    def __init__(self):
        """
        Inicializa un nuevo jugador en el juego.

        Establece la posición inicial del jugador en el centro de la pantalla cerca 
        del suelo, y define sus propiedades como la velocidad, el número de vidas y 
        los puntos.
        """
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
        """
        Mueve al jugador según las teclas presionadas y verifica colisiones con objetos.

        Los movimientos se limitan a los bordes de la pantalla. Si el jugador colisiona 
        con algún objeto, se imprime un mensaje con el tipo de objeto con el que colisionó.
        """
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

        # cambiar la imagen del jugador segun la posición
        if dx > 0:  # Movimiento a la derecha
            self.imagen = pygame.transform.flip(pygame.image.load(
                "recursos_juego/imagenes/Explorador.png"), True, False)
            self.imagen = pygame.transform.scale(self.imagen, (200, 200))
        elif dx < 0:  # Movimiento a la izquierda
            self.imagen = pygame.image.load(
                "recursos_juego/imagenes/Explorador.png")
            self.imagen = pygame.transform.scale(self.imagen, (200, 200))

    def colisiona_con(self, objeto):
        """
        Verifica si el jugador colisiona con un objeto.

        Utiliza los rectángulos de colisión de ambos, el jugador y el objeto, para 
        determinar si se superponen.

        Args:
            objeto (Objeto): El objeto con el que el jugador puede colisionar.

        Returns:
            bool: True si el jugador colisiona con el objeto, False en caso contrario.
        """
        jugador_rect = pygame.Rect(self.x, self.y, 200, 200)
        objeto_rect = pygame.Rect(objeto.x, objeto.y, 50, 50)
        return jugador_rect.colliderect(objeto_rect)

    def saltar(self):
        """
        Inicia el salto del jugador si no está ya en el aire.

        Cuando el jugador salta, se establece una velocidad negativa en el eje Y 
        para simular la fuerza del salto.
        """
        if not self.saltando:  # Solo saltar si no está ya en el aire
            self.saltando = True
            self.velocidad_y = -15  # Fuerza inicial del salto

    def aplicar_gravedad(self):
        """
        Aplica la gravedad al jugador.

        Si el jugador está saltando, la gravedad aumenta la velocidad de caída en cada 
        ciclo y mueve al jugador hacia abajo. Si el jugador alcanza el suelo, detiene la 
        caída y restablece las propiedades del salto.

        La gravedad solo se aplica si el jugador no está en el suelo.
        """
        if self.saltando:  # Aplica gravedad si no está en el suelo
            self.velocidad_y += 1  # Aceleración por gravedad
            self.y += self.velocidad_y

        if self.y >= ALTO - 200:  # suelo
            self.y = ALTO - 200
            self.saltando = False
            self.velocidad_y = 0  # Detener la caída
        else:
            self.en_suelo = False  # No está en el suelo si está saltando

    def dibujar(self, pantalla):
        """
        Dibuja al jugador en la pantalla.

        Muestra la imagen del jugador en su posición actual.

        Args:
            pantalla (Surface): La superficie sobre la que se dibujará el jugador.
        """
        pantalla.blit(self.imagen, (self.x, self.y))


class Objeto:
    def __init__(self, tipo_objeto, x=None, y=None, direccion="vertical"):
        """
        Inicializa un nuevo objeto interactivo en el juego.

        Los objetos pueden ser de varios tipos (por ejemplo, bomba, tesoro, vida) y 
        tienen propiedades como su posición, dirección de movimiento y velocidad.
        """
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
        """
        Mueve el objeto según su tipo y dirección.

        Si el objeto es una bomba, se mueve verticalmente o horizontalmente. Si el 
        objeto sale de la pantalla, reaparece en una nueva posición aleatoria.

        La dirección de movimiento se define al crear el objeto y se actualiza 
        cada vez que se llama a esta función.
        """
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
        """
        Dibuja el objeto en la pantalla.

        Muestra la imagen del objeto en su posición actual.

        Args:
            pantalla (Surface): La superficie sobre la que se dibujará el objeto.
        """
        pantalla.blit(self.imagen, (self.x, self.y))
