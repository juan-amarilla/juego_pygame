from ciclo_principal import (pygame, iniciar_con_musica, colocar_titulo, menu)

iniciar_con_musica("musica/musica_menu/ambient 9.mp3")

fuente = pygame.font.Font("fuentes/pixel.ttf", 50)

titulo = colocar_titulo("Las aventuras del buscador")

opcion = 0

ejecutar = True

while ejecutar:

    ejecutar = menu(ejecutar, fuente, titulo)