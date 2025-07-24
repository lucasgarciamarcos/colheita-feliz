import pygame
from src.config import MENU_ICON_PATH, MENU_FOICE_ICON_PATH, SCREEN_WIDTH, SCREEN_HEIGHT, DEBUG

class Menu:
    def __init__(self):
        # Definir os caminhos das ferramentas
        self.caminhos_ferramentas = [
            MENU_FOICE_ICON_PATH,  # 1: foice
            MENU_ICON_PATH,        # 2: regador
            MENU_ICON_PATH,        # 3: fertilizante
            MENU_ICON_PATH,        # 4: sementes
            MENU_ICON_PATH,        # 4: loja
        ]
        
        # Carregar ícones e criar estrutura similar ao TerrinhaGrid
        self.ferramentas = {}
        y = SCREEN_HEIGHT - 80 // 2
        x = (SCREEN_WIDTH - len(self.caminhos_ferramentas) * 80) // 2 + 20
        
        for i, caminho in enumerate(self.caminhos_ferramentas):
            icone = pygame.image.load(caminho).convert_alpha()
            icone = pygame.transform.scale(icone, (80, 80))
            
            # Rect visual do ícone
            icone_rect = icone.get_rect(center=(x, y))
            
            # Hitbox para detecção de colisão
            hitbox = pygame.Rect(0, 0, 80, 80)
            hitbox.center = (x, y)
            
            self.ferramentas[i] = {
                "icone": icone,
                "rect": icone_rect,
                "hitbox": hitbox
            }
            
            x += 80
        
        # Estados das ferramentas
        self.ferramenta_ativa = 0
        self.hover_index = None

    def checar_clique(self, cursor):
        """Verifica se algum botão foi clicado usando hitbox do cursor"""
        for idx, ferramenta in self.ferramentas.items():
            if cursor.get_hitbox().colliderect(ferramenta["hitbox"]):
                self.ferramenta_ativa = idx
                return idx
        return None
    
    def checar_hover(self, cursor):
        """Verifica se o cursor está sobre algum botão usando hitbox"""
        self.hover_index = None
        for idx, ferramenta in self.ferramentas.items():
            if cursor.get_hitbox().colliderect(ferramenta["hitbox"]):
                self.hover_index = idx
                break

    def desenhar(self, screen):
        for idx, ferramenta in self.ferramentas.items():
            # Desenhar fundo para ferramenta ativa
            if idx == self.ferramenta_ativa:
                pygame.draw.rect(screen, (100, 200, 100), 
                               (ferramenta["rect"].x - 5, ferramenta["rect"].y - 5, 
                                ferramenta["rect"].width + 10, ferramenta["rect"].height + 10), 3)
            
            # Desenhar fundo para hover (se não for a ativa)
            elif idx == self.hover_index:
                pygame.draw.rect(screen, (200, 200, 100), 
                               (ferramenta["rect"].x - 3, ferramenta["rect"].y - 3, 
                                ferramenta["rect"].width + 6, ferramenta["rect"].height + 6), 2)
            
            # Debug: mostrar hitbox
            if DEBUG:
                if idx == self.hover_index:
                    pygame.draw.rect(screen, (0, 255, 0), ferramenta["hitbox"], 2)
            
            # Desenhar ícone
            screen.blit(ferramenta["icone"], ferramenta["rect"])