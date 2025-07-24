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
                ferramenta_ativa = menu.get_ferramenta_atual()
                grid.checar_clique(cursor, ferramenta_ativa)  # ← Mudança aqui: cursor ao invés de mouse_pos

    # Atualizar cursor baseado na ferramenta ativa
    ferramenta_ativa = menu.get_ferramenta_atual()
    cursor.mudar_ferramenta(ferramenta_ativa)
                
    screen.fill(COR_FUNDO)

    # Checar hover
    menu.checar_hover(cursor)
    grid.checar_hover(cursor)

    # Desenhar jogo
    grid.desenhar(screen)
    menu.desenhar(screen)
    cursor.desenhar(screen, mouse_pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()