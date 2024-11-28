"""
Módulo principal para iniciar el juego.

Este módulo se encarga de cargar la música del menú, configurar el flujo del menú
principal y ejecutar el ciclo de inicio del juego. Utiliza las funciones de los módulos 
`funciones_menu` y `funciones_ciclo_principal` para gestionar la interacción con el 
usuario y el inicio del juego.

Variables:
    opcion (int): Opción seleccionada en el menú, predeterminada en 0.
    ejecutar (bool): Indica si el ciclo del menú debe continuar o no.

El ciclo principal del menú se mantiene activo hasta que `ejecutar` es False, momento 
en el cual el juego termina o se realiza una acción fuera del ciclo.
"""

from funciones_menu import *
from funciones_ciclo_principal import *

pygame.mixer.music.load("recursos_menu/musica/musica_menu/ambient 9.mp3")

opcion = 0

ejecutar = True

while ejecutar:

    ejecutar = menu(ejecutar)
