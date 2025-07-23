import pygame
from src.config import CURSOR_PATH, DEBUG

class CursorPersonalizado:
    def __init__(self):
        self.imagem = pygame.image.load(CURSOR_PATH).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (120, 120))
        self.imagem.set_colorkey((255, 255, 255))
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()

        # Inicializa hitbox
        self.hitbox = pygame.Rect(0, 0, 40, 40)

    def desenhar(self, screen, posicao):
        # Desenha o cursor
        screen.blit(self.imagem, posicao)

        # Atualiza hitbox baseada na posição do mouse
        self.hitbox.topleft = (posicao[0] + 30, posicao[1] + 10)

        if DEBUG:
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def get_hitbox(self):
        return self.hitbox
