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

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fundo
    screen.fill((0, 0, 0))

    # Posicao do mouse
    mouse_pos = pygame.mouse.get_pos()
    # Desenhar cursor na posição do mouse
    screen.blit(cursor_img, mouse_pos)
    
    # Atualiza a tela
    pygame.display.flip()
    # Seta Framerate
    clock.tick(30)

pygame.quit()