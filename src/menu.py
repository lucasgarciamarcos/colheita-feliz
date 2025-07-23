import pygame
from src.config import MENU_ICON_PATH, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self):
        self.icones = [self._carregar_icone() for _ in range(6)]

    def _carregar_icone(self):
        icone = pygame.image.load(MENU_ICON_PATH).convert_alpha()
        icone = pygame.transform.scale(icone, (80, 80))
        return icone

    def desenhar(self, screen):
        y = SCREEN_HEIGHT - 80 // 2
        x = (SCREEN_WIDTH - len(self.icones) * 80) // 2 + 20

        for icone in self.icones:
            rect = icone.get_rect(center=(x, y))
            screen.blit(icone, rect)
            x += 80
