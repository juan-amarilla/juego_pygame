from funciones_menu import *
from ciclo_principal import *

pygame.mixer.music.load("recursos_menu/musica/musica_menu/ambient 9.mp3")

opcion = 0

ejecutar = True

while ejecutar:

    ejecutar = menu(ejecutar)