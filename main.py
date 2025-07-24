import pygame
from src.config import *
from src.menu import Menu
from src.cursor import CursorPersonalizado
from src.terrinhas import TerrinhaGrid

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coleta Feliz")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# Instâncias
menu = Menu()
grid = TerrinhaGrid()
cursor = CursorPersonalizado()

# Mapear índice do botão para ferramenta
ferramentas = {
    0: "cursor",
    1: "pá",
    2: "regador", 
    3: "fertilizante",
    4: "sementes",
    5: "colher"
}

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicado = menu.checar_clique(cursor)
            if clicado is None:
                # Se não clicou no menu, verifica clique no grid
                ferramenta_ativa = ferramentas.get(menu.ferramenta_ativa, "cursor")
                grid.checar_clique(mouse_pos, ferramenta_ativa)
                
    screen.fill(COR_FUNDO)

    # Checar hover no menu e grid
    menu.checar_hover(cursor)
    grid.checar_hover(cursor)

    # Desenhar jogo
    grid.desenhar(screen)
    menu.desenhar(screen)
    cursor.desenhar(screen, mouse_pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()