import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Coleta Feliz")

# Esconder o cursor padrão
pygame.mouse.set_visible(False)

# Carregar imagem do cursor personalizado
cursor_img = pygame.image.load("sprites/cursor.png").convert_alpha()
cursor_img = pygame.transform.scale(cursor_img, (120, 120))
cursor_img.set_colorkey((255, 255, 255))

# Carregar o sprite do terreno
terra_img = pygame.image.load("sprites/terra_seca.png").convert()
terra_img = pygame.transform.scale(terra_img, (200, 200))
terra_img.set_colorkey((255, 255, 255))

def criar_terrinhas(screen, terra_img, linhas=3, colunas=3, pos_inicial_x=200, pos_inicial_y=200):
    terrinhas = {}

    for linha in range(linhas):
        for coluna in range(colunas):
            x = pos_inicial_x + (coluna * 80) + (linha * 80)
            y = pos_inicial_y + (coluna * 35) - (linha * 35)
            rect = terra_img.get_rect(center=(x, y))
            terrinhas[(linha, coluna)] = {
                "rect": rect,
                "estado": "seco"
            }
            screen.blit(terra_img, rect)

    return terrinhas

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fundo
    screen.fill((0, 0, 0))

    # desenhos
    criar_terrinhas(screen, terra_img)

    # Posicao do mouse
    mouse_pos = pygame.mouse.get_pos()
    # Desenhar cursor na posição do mouse
    screen.blit(cursor_img, mouse_pos)
    
    # Atualiza a tela
    pygame.display.flip()
    # Seta Framerate
    clock.tick(30)

pygame.quit()