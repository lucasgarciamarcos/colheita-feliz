import pygame
from src.config import DEBUG, TERRA_PATH

class TerrinhaGrid:
    def __init__(self, linhas=3, colunas=3, pos_inicial_x=160, pos_inicial_y=300):
        self.linhas = linhas
        self.colunas = colunas
        self.pos_x = pos_inicial_x
        self.pos_y = pos_inicial_y
        self.terra_img = pygame.image.load(TERRA_PATH).convert()
        self.terra_img = pygame.transform.scale(self.terra_img, (200, 200))
        self.terra_img.set_colorkey((255, 255, 255))
        self.terrinhas = self._criar_terrinhas()
        self.hover_index = None

    def _criar_terrinhas(self):
        terrinhas = {}
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                x = self.pos_x + (coluna * 80) + (linha * 80)
                y = self.pos_y + (coluna * 35) - (linha * 35)

                imagem_rect = self.terra_img.get_rect(center=(x, y))

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
            if DEBUG:
                # Highlight da hitbox
                if idx == self.hover_index:
                    pygame.draw.rect(screen, (0, 255, 0), terrinha["hitbox"], 2)

            screen.blit(self.terra_img, terrinha["rect"])

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
                # Aqui você pode implementar a lógica específica de cada ferramenta
                print(f"Clicou na terrinha {idx} com ferramenta: {ferramenta_ativa}")
                
                # Exemplo de lógica por ferramenta:
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