import pygame
from src.config import DEBUG

class TerrinhaGrid:
    def __init__(self, linhas=3, colunas=3, pos_inicial_x=100, pos_inicial_y=400):
        self.linhas = linhas
        self.colunas = colunas
        self.pos_x = pos_inicial_x
        self.pos_y = pos_inicial_y
        
        # Definir caminhos dos sprites por estado
        self.terra_sprites = {
            "seco": "sprites/terra_seca.png",
            "molhado": "sprites/terra_seca.png", 
            "plantado": "sprites/terra_seca.png",
            "fertilizado": "sprites/terra_seca.png",
            "colhido": "sprites/terra_seca.png"
        }
        
        # Carregar sprites normais
        self.sprites = {}
        for estado, caminho in self.terra_sprites.items():
            img = pygame.image.load(caminho).convert()
            img = pygame.transform.scale(img, (200, 200))
            img.set_colorkey((255, 255, 255))
            self.sprites[estado] = img
        
        # Carregar sprites selected (simplificado)
        self.sprites_selected = {}
        for estado, caminho in self.terra_sprites.items():
            caminho_selected = caminho.replace('.png', '_selected.png')
            img_selected = pygame.image.load(caminho_selected).convert()
            img_selected = pygame.transform.scale(img_selected, (200, 200))
            img_selected.set_colorkey((255, 255, 255))
            self.sprites_selected[estado] = img_selected
        
        # Criar overlays brancos usando máscaras (clareada)
        self.hover_overlays = {}
        for estado, sprite in self.sprites.items():
            # Criar máscara do sprite
            mask = pygame.mask.from_surface(sprite)
            # Criar surface do overlay branco para clarear
            mask_surface = mask.to_surface(setcolor=(255, 255, 255, 80), unsetcolor=(0, 0, 0, 0))
            self.hover_overlays[estado] = mask_surface
        
        self.terrinhas = self._criar_terrinhas()
        self.hover_index = None

    def _criar_terrinhas(self):
        terrinhas = {}
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                x = self.pos_x + (coluna * 80) + (linha * 80)
                y = self.pos_y + (coluna * 35) - (linha * 35)

                imagem_rect = self.sprites["seco"].get_rect(center=(x, y))

                hitbox = pygame.Rect(0, 0, 60, 60)
                hitbox.center = (x, y+55)

                terrinhas[(linha, coluna)] = {
                    "rect": imagem_rect,
                    "hitbox": hitbox,
                    "estado": "seco"
                }

        return terrinhas

    def desenhar(self, screen):
        for idx, terrinha in self.terrinhas.items():
            estado = terrinha["estado"]
            
            # Escolher sprite (selected se hover, normal se não)
            if idx == self.hover_index:
                sprite = self.sprites_selected[estado]
            else:
                sprite = self.sprites[estado]
            
            # Desenhar sprite
            screen.blit(sprite, terrinha["rect"])
            
            # Aplicar overlay verde que respeita transparência
            if idx == self.hover_index:
                screen.blit(self.hover_overlays[estado], terrinha["rect"])
            
            if DEBUG:
                # Highlight da hitbox
                if idx == self.hover_index:
                    pygame.draw.rect(screen, (0, 255, 0), terrinha["hitbox"], 2)

    def checar_hover(self, cursor):
        self.hover_index = None
        for idx, terrinha in self.terrinhas.items():
            if cursor.get_hitbox().colliderect(terrinha["hitbox"]):
                self.hover_index = idx
                break

    def checar_clique(self, cursor, ferramenta_ativa):
        """Verifica clique nas terrinhas usando o cursor e aplica a ferramenta"""
        for idx, terrinha in self.terrinhas.items():
            if cursor.get_hitbox().colliderect(terrinha["hitbox"]):
                print(f"Clicou na terrinha {idx} com ferramenta: {ferramenta_ativa}")
                
                # Lógica por ferramenta
                if ferramenta_ativa == "agua":
                    terrinha["estado"] = "molhado"
                elif ferramenta_ativa == "sementes":
                    terrinha["estado"] = "plantado"
                elif ferramenta_ativa == "foice":
                    terrinha["estado"] = "colhido"
                elif ferramenta_ativa == "fertilizante":
                    terrinha["estado"] = "fertilizado"
                
                return idx
        return None